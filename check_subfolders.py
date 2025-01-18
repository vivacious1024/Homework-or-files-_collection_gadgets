import os

def check_subfolders(folder_path):
    # 获取大文件夹下的所有一级子文件夹
    try:
        subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
        
        # 遍历每个子文件夹
        for subfolder in subfolders:
            # 获取子文件夹内部的所有文件（不包括子文件夹）
            files = [f for f in os.scandir(subfolder) if f.is_file()]
            
            # 判断文件数量是否达到6个
            if len(files) < 6:
                print(f"子文件夹 '{subfolder}' 的文件数量不足6个，当前文件数量：{len(files)}")
    
    except Exception as e:
        print(f"检查过程中出现错误: {e}")

# 设定大文件夹路径
folder_path = r'*******'

# 调用函数检查文件夹
check_subfolders(folder_path)
