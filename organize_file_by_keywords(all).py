import os
import shutil

def organize_files_by_keywords(root_folder, keywords):
    """
    遍历文件夹下所有文件（包括各子文件夹）名，根据给定的关键词将文件分类到对应子文件夹中。

    :param root_folder: 要遍历的文件夹路径
    :param keywords: 包含关键词的列表，用于匹配文件名
    """
    if not os.path.isdir(root_folder):
        print(f"{root_folder} 不是有效的文件夹路径")
        return

    # 遍历根文件夹下所有文件和子文件夹
    for file_name in os.listdir(root_folder):
        file_path = os.path.join(root_folder, file_name)

        # 确保只针对非文件夹的文件进行处理
        if os.path.isfile(file_path):
            # 检查文件名是否包含关键词
            for keyword in keywords:
                if keyword in file_name:
                    # 创建以关键词命名的子文件夹（如果还没有）
                    keyword_folder = os.path.join(root_folder, keyword)
                    if not os.path.exists(keyword_folder):
                        os.makedirs(keyword_folder)
                        print(f"创建文件夹：{keyword_folder}")

                    # 将文件移动到对应的子文件夹
                    new_file_path = os.path.join(keyword_folder, file_name)
                    shutil.move(file_path, new_file_path)
                    print(f"移动文件：{file_path} -> {new_file_path}")
                    break  # 一个文件只匹配一个关键词，找到后停止匹配

    print("文件整理完成！")

# 示例：使用该函数
root_folder_path = "******"  # 替换为你的文件夹路径
keywords = ["关键词1","关键词2","关键词3"]  # 替换为你需要匹配的关键词列表
organize_files_by_keywords(root_folder_path, keywords)
