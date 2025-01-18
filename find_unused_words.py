# -*- coding: utf-8 -*-
import os

def find_unused_keywords(root_folder, keywords):
    """
    在指定文件夹中查找未使用的关键词。

    :param root_folder: 要遍历的文件夹路径
    :param keywords: 包含关键词的列表
    """
    if not os.path.isdir(root_folder):
        print(f"{root_folder} 不是有效的文件夹路径")
        return

    # 初始化一个集合，用于记录已找到的关键词
    matched_keywords = set()

    # 遍历文件夹中的所有文件
    for file_name in os.listdir(root_folder):
        file_path = os.path.join(root_folder, file_name)

        # 确保只针对文件（忽略子文件夹）
        if os.path.isfile(file_path):
            # 检查文件名中包含哪些关键词
            for keyword in keywords:
                if keyword in file_name:
                    matched_keywords.add(keyword)

    # 计算未使用的关键词
    unused_keywords = set(keywords) - matched_keywords

    # 打印结果
    if unused_keywords:
        print("以下关键词没有出现在任何文件名中：")
        for keyword in sorted(unused_keywords):
            print(f'"{keyword}",')
    else:
        print("所有关键词都出现在文件名中！")

# 示例：使用该函数
root_folder_path = r"******"  # 替换为你的文件夹路径
keywords = ["关键词1","关键词2"]  # 替换为你的关键词列表
find_unused_keywords(root_folder_path, keywords)
