import os
import shutil

def organize_files_by_keywords(folder_path, keywords):
    """
    遍历指定文件夹中的文件（仅限当前一级），如果文件名包含任意一个关键词，
    则将文件移动到一个以匹配的关键词命名的子文件夹中。

    :param folder_path: 要遍历的文件夹路径
    :param keywords: 用于筛选文件的关键词列表
    """
    try:
        # 确保文件夹路径有效
        if not os.path.isdir(folder_path):
            print(f"错误：路径 '{folder_path}' 不是一个有效的文件夹。")
            return

        # 确保关键词是列表
        if not isinstance(keywords, list):
            print("错误：关键词参数必须是一个列表。")
            return

        # 遍历文件夹中的一级文件
        files_moved = 0  # 记录移动的文件数
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)

            # 确保是文件而不是文件夹
            if os.path.isfile(item_path):
                # 检查文件名是否包含任意一个关键词
                for keyword in keywords:
                    if keyword in item:
                        # 创建关键词命名的子文件夹
                        keyword_folder = os.path.join(folder_path, keyword)
                        if not os.path.exists(keyword_folder):
                            os.makedirs(keyword_folder)

                        # 移动文件到关键词文件夹
                        shutil.move(item_path, os.path.join(keyword_folder, item))
                        files_moved += 1
                        print(f"已移动文件：{item} -> {keyword_folder}")
                        break  # 如果找到一个匹配的关键词，就停止检查其他关键词

        if files_moved == 0:
            print(f"未找到包含任意关键词的文件。")
        else:
            print(f"操作完成，共移动 {files_moved} 个文件。")

    except Exception as e:
        print(f"发生错误：{e}")

# 示例用法
folder_to_organize = "******"  # 替换为目标文件夹路径
search_keywords = ["关键词1","关键词2","关键词3"]  # 替换为关键词列表

organize_files_by_keywords(folder_to_organize, search_keywords)
