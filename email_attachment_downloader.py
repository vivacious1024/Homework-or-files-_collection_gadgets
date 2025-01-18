import chardet  # 自动检测编码库
import imaplib
import email
from email.header import decode_header
import os
import re  # 引入正则库用于文件名清理

def decode_content(payload, default="utf-8"):
    """
    解码邮件正文或附件名，如果编码为 None 则自动检测。
    """
    try:
        if isinstance(payload, bytes):
            # 自动检测编码
            detected = chardet.detect(payload)
            encoding = detected.get("encoding") or default  # 如果检测失败则使用默认编码
            confidence = detected.get("confidence", 0)
            
            # 如果置信度较低，提示并使用默认编码
            if confidence < 0.5:
                print(f"检测到的编码置信度较低 ({confidence:.2f})，使用默认编码: {default}")
                encoding = default
            
            print(f"检测到编码: {encoding} (置信度: {confidence:.2f})")
            return payload.decode(encoding)
        else:
            return payload
    except Exception as e:
        print(f"解码失败，错误: {e}")
        return payload.decode(default, errors="replace")

def sanitize_filename(filename):
    """
    清理文件名，移除或替换非法字符以确保文件名合法。
    """
    # 定义非法字符（Windows）
    illegal_chars = r'<>:"/\|?*\r\n'
    # 使用下划线替换非法字符
    sanitized = re.sub(f'[{re.escape(illegal_chars)}]', '_', filename)
    # 去除多余的空白字符
    sanitized = re.sub(r'\s+', ' ', sanitized).strip()
    return sanitized

def download_filtered_attachments(email_user, email_password, imap_server, folder="INBOX", save_path="./attachments", keywords=None):
    """
    从邮箱中下载附件，条件是邮件的主题或内容包含给定关键词中的任意一个，并根据是否包含关键词重命名附件。
    
    - 如果包含关键词，则将附件命名为 "关键词_原始文件名"。
    - 如果不包含任何关键词，则将附件命名为 "发件人邮箱_原始文件名"。
    - 如果邮件没有附件，则打印相应信息。
    
    :param email_user: 邮箱地址
    :param email_password: 邮箱密码或授权码
    :param imap_server: IMAP 服务器地址
    :param folder: 搜索的邮箱文件夹（默认 "INBOX"）
    :param save_path: 保存附件的文件夹路径
    :param keywords: 关键词列表
    """
    try:
        # 检查输入
        if not keywords:
            print("必须提供关键词列表。")
            return

        # 连接到 IMAP 服务器
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_user, email_password)

        # 选择邮箱文件夹
        mail.select(folder)

        # 搜索所有邮件（可按需求调整搜索条件）
        status, messages = mail.search(None, "ALL")
        if status != "OK":
            print("未能找到符合条件的邮件。")
            return

        # 获取邮件编号列表
        email_ids = messages[0].split()
        if not email_ids:
            print("没有符合条件的邮件。")
            return

        # 确保保存路径存在
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # 遍历每封邮件
        for idx, email_id in enumerate(email_ids, start=1):  # 添加序号
            print(f"\n处理第 {idx} 封邮件（ID: {email_id.decode()}）...")

            # 获取邮件内容
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            if status != "OK":
                print(f"无法获取邮件 ID {email_id.decode()}")
                continue

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    # 解析邮件
                    msg = email.message_from_bytes(response_part[1])

                    # 获取发件人邮箱
                    from_header = msg.get("From", "")
                    sender_email = email.utils.parseaddr(from_header)[1]

                    # 获取邮件主题并解码
                    subject, encoding = decode_header(msg.get("Subject", ""))[0]
                    if isinstance(subject, bytes):
                        subject = decode_content(subject, default=encoding or "utf-8")

                    # 获取邮件正文
                    body = ""
                    try:
                        if msg.is_multipart():
                            for part in msg.walk():
                                content_type = part.get_content_type()
                                content_disposition = part.get_content_disposition()
                                if content_type in ["text/plain", "text/html"] and content_disposition != "attachment":
                                    charset = part.get_content_charset() or "utf-8"
                                    print(f"尝试解码正文，推测编码: {charset}")
                                    payload = part.get_payload(decode=True)
                                    body += decode_content(payload, default=charset)
                        else:
                            charset = msg.get_content_charset() or "utf-8"
                            print(f"尝试解码正文，推测编码: {charset}")
                            payload = msg.get_payload(decode=True)
                            body = decode_content(payload, default=charset)
                    except Exception as e:
                        print(f"邮件正文解码过程中出错: {e}")

                    # 检查主题和正文是否包含任意关键词
                    matched_keyword = next((kw for kw in keywords if kw in subject or kw in body), None)
                    
                    if matched_keyword:
                        print(f"找到匹配关键词: {matched_keyword}")
                        rename_prefix = matched_keyword
                    else:
                        print("未找到匹配关键词，使用发件人邮箱作为前缀。")
                        rename_prefix = sender_email.replace("@", "_").replace(".", "_")  # 替换特殊字符以适应文件名

                    # 遍历邮件的附件部分
                    attachment_found = False  # 标记是否找到附件
                    for part in msg.walk():
                        if part.get_content_disposition() == "attachment":
                            attachment_found = True
                            filename = part.get_filename()
                            if filename:
                                # 解码附件名
                                try:
                                    decoded_filename, encoding = decode_header(filename)[0]
                                    if isinstance(decoded_filename, bytes):
                                        filename = decode_content(decoded_filename, default=encoding or "utf-8")
                                except Exception as e:
                                    print(f"附件文件名解码失败: {e}, 文件名: {filename}")
                                    continue

                                # 清理文件名
                                sanitized_filename = sanitize_filename(filename)

                                # 构造新文件名
                                new_filename = f"{rename_prefix}_{sanitized_filename}"
                                print(f"保存附件为: {new_filename}")

                                # 保存附件，添加错误处理以跳过问题文件
                                try:
                                    filepath = os.path.join(save_path, new_filename)
                                    with open(filepath, "wb") as f:
                                        f.write(part.get_payload(decode=True))
                                    print(f"已下载附件：{filepath}")
                                except OSError as oe:
                                    print(f"无法保存附件 '{new_filename}': {oe}. 跳过此附件。")
                                except Exception as e:
                                    print(f"保存附件过程中发生未知错误: {e}. 跳过此附件。")
                    
                    # 检查是否没有找到任何附件
                    if not attachment_found:
                        print("此邮件没有附件。")

        # 关闭连接
        mail.close()
        mail.logout()

    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    # 示例用法
    email_user = "******"      # 替换为你的邮箱地址
    email_password = "******"     # 替换为你的邮箱密码或授权码
    imap_server = "******"             # 替换为你的 IMAP 服务器地址
    keywords = ["关键词1","关键词2","关键词3"] 
    # 替换为实际关键词列表

    download_filtered_attachments(
        email_user=email_user,
        email_password=email_password,
        imap_server=imap_server,
        folder="INBOX",
        save_path=r"******",    # 保存文件地址记得改
        keywords=keywords
    )
