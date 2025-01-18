import os
import shutil

def organize_files_by_prefix(root_folder):
    """
    按文件名第一个下划线前的文本在指定目录中整理文件到子文件夹。
    :param root_folder: 需要整理的文件夹路径
    """
    try:
        # 遍历指定文件夹（包括子文件夹中的文件）
        for dirpath, dirnames, filenames in os.walk(root_folder):
            for file in filenames:
                # 获取文件名和完整路径
                file_path = os.path.join(dirpath, file)
                
                # 跳过非文件或特殊文件
                if not os.path.isfile(file_path):
                    continue
                
                # 提取文件名前缀（到第一个下划线为止）
                prefix = file.split("_", 1)[0]
                
                # 如果文件名中没有下划线，跳过
                if "_" not in file:
                    print(f"文件 '{file}' 不包含下划线，跳过。")
                    continue
                
                # 创建子文件夹路径
                subfolder_path = os.path.join(root_folder, prefix)
                
                # 如果子文件夹不存在，则创建
                if not os.path.exists(subfolder_path):
                    os.makedirs(subfolder_path)
                    print(f"创建子文件夹: {subfolder_path}")
                
                # 移动文件到子文件夹
                new_file_path = os.path.join(subfolder_path, file)
                shutil.move(file_path, new_file_path)
                print(f"移动文件 '{file}' 到 '{subfolder_path}'")

        print("\n文件整理完成！")

    except Exception as e:
        print(f"发生错误: {e}")

# 使用示例
# 请将 "your_folder_path_here" 替换为需要整理的大文件夹路径
root_folder = r"******"
organize_files_by_prefix(root_folder)
