import os

def create_subfolders(base_path, keywords):
    """
    在指定的基础路径下创建以关键词命名的子文件夹。

    :param base_path: 指定的基础文件夹路径
    :param keywords: 关键词列表
    """
    if not os.path.exists(base_path):
        print(f"指定的基础路径不存在: {base_path}")
        return

    for keyword in keywords:
        # 生成子文件夹的完整路径
        folder_path = os.path.join(base_path, keyword)
        try:
            os.makedirs(folder_path, exist_ok=True)
            print(f"已创建文件夹: {folder_path}")
        except Exception as e:
            print(f"创建文件夹失败: {folder_path}. 错误: {e}")

if __name__ == "__main__":
    # 指定基础文件夹路径
    base_directory = r"******"  # 修改为你的目标路径

    # 给定的一组关键词
    keywords = ["关键词1","关键词2","关键词3"]  # 修改为你的关键词列表

    create_subfolders(base_directory, keywords)
