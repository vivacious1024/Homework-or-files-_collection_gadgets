# -*- coding: utf-8 -*-

import os

def find_missing_keywords(main_folder, keywords):
    """
    在主文件夹中的子文件夹名称中查找关键词，并返回未出现的关键词列表。
    同时统计遍历的子文件夹数量。

    :param main_folder: 主文件夹的路径
    :param keywords: 关键词列表
    :return: 未出现的关键词列表, 遍历的子文件夹数量
    """
    # 使用集合来存储未找到的关键词，初始时包含所有关键词
    missing_keywords = set(keywords)
    
    # 初始化子文件夹计数器
    subfolder_count = 0

    try:
        # 遍历主文件夹中的所有项
        for item in os.listdir(main_folder):
            item_path = os.path.join(main_folder, item)
            # 检查是否是文件夹
            if os.path.isdir(item_path):
                subfolder_count += 1  # 增加计数
                # 遍历所有关键词，检查是否包含在子文件夹名称中
                for keyword in keywords:
                    if keyword.lower() in item.lower():
                        if keyword in missing_keywords:
                            missing_keywords.remove(keyword)
    except FileNotFoundError:
        print(f"错误: 指定的主文件夹路径 '{main_folder}' 不存在。")
        return [], 0
    except PermissionError:
        print(f"错误: 无权限访问主文件夹路径 '{main_folder}'。")
        return [], 0
    except Exception as e:
        print(f"发生错误: {e}")
        return [], 0

    return list(missing_keywords), subfolder_count

if __name__ == "__main__":
    # 示例关键词列表
    keywords = ["关键词1","关键词2"]

    # 指定主文件夹路径
    main_folder = r"******"  # 请将此路径替换为你的实际路径

    # 检查主文件夹是否存在
    if not os.path.exists(main_folder):
        print(f"错误: 主文件夹路径 '{main_folder}' 不存在。请检查路径是否正确。")
    else:
        # 调用函数查找缺失的关键词，并获取遍历的子文件夹数量
        missing, count = find_missing_keywords(main_folder, keywords)

        # 输出结果
        print(f"已遍历 {count} 个子文件夹。")
        if missing:
            print("以下关键词未在任何子文件夹名称中找到：")
            for kw in missing:
                print(f'"{kw}",')
        else:
            print("所有关键词都已在子文件夹名称中找到。")
