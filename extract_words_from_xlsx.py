import openpyxl

def read_excel_and_write_to_txt(input_excel, output_txt, exclude_words=None):
    """
    读取 .xlsx 文件的内容，并将每个单元格的内容写入到 .txt 文件，每个词语用双引号包裹。
    可选功能：排除指定的词语。
    
    :param input_excel: 输入的 .xlsx 文件路径
    :param output_txt: 输出的 .txt 文件路径
    :param exclude_words: 排除的词语列表（可选）
    """
    if exclude_words is None:
        exclude_words = []

    try:
        count = 0
        # 打开 .xlsx 文件
        workbook = openpyxl.load_workbook(input_excel)
        sheet = workbook.active  # 默认读取第一个工作表

        # 打开 .txt 文件以写入模式
        with open(output_txt, 'w', encoding='utf-8') as txt_file:
            for row in sheet.iter_rows():
                for cell in row:
                    if cell.value:  # 确保单元格有内容
                        word = str(cell.value).strip()
                        if word not in exclude_words:  # 排除指定词语
                            txt_file.write(f'"{word}",')  # 加上双引号并加上逗号
                            count+=1
        print(f"内容已成功写入 {output_txt}")
        print(f"总计词汇{count}个")
    except Exception as e:
        print(f"发生错误：{e}")

# 示例用法
input_excel_path = r"******"  # 替换为你的 .xlsx 文件路径
output_txt_path = r"******"    # 输出的 .txt 文件路径
exclude_list = ["排除词1", "排除词2"]  # 需要排除的词语列表（可选）

read_excel_and_write_to_txt(input_excel_path, output_txt_path, exclude_words=exclude_list)
