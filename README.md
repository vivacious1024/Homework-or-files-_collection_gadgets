# 【当助教收作业】一些没啥用的整理文件的代码
当了一门课程的助教，平时作业有六份，由于初来不很熟练，采用让学生交到我个人邮箱的方式，也没有作过多要求，导致收集到的东西都非常抽象，整理起来十分麻烦，这些代码便是我企图提高一点效率的中间产物，主要涉及文件整理等等。当然不一定有用，但放出来，主要还是为了传授教训：**收集文件一定要有所规范，或者说各种事情都应如此，现在就是十分推荐那些线上收集文件的好用的在线工具**

以下是各个代码的介绍。先放个目录：
- [check\_subfolders.py 检查每个子文件夹中的文件数量](#check_subfolderspy-检查每个子文件夹中的文件数量)
  - [功能说明](#功能说明)
  - [使用方法](#使用方法)
  - [输出示例](#输出示例)
  - [错误处理](#错误处理)
  - [注意事项](#注意事项)
  - [定制与扩展](#定制与扩展)
    
- [create\_docx.py 自动创建 Word 文档](#create_docxpy-自动创建-word-文档)
  - [功能说明](#功能说明-1)
  - [依赖环境](#依赖环境)
  - [使用方法](#使用方法-1)
  - [参数说明](#参数说明)
  - [输出示例](#输出示例-1)
  - [错误处理](#错误处理-1)
  - [定制与扩展](#定制与扩展-1)
    
- [create\_subfolders.py 按给定词自动创建子文件夹](#create_subfolderspy-按给定词自动创建子文件夹)
  - [功能说明](#功能说明-2)
  - [使用方法](#使用方法-2)
  - [输出示例](#输出示例-2)
  - [定制与扩展](#定制与扩展-2)
    
- [email\_attachment\_downloader.py 邮箱附件下载与过滤脚本](#email_attachment_downloaderpy-邮箱附件下载与过滤脚本)
  - [功能简介](#功能简介)
  - [功能特点](#功能特点)
  - [环境要求](#环境要求)
  - [使用方法](#使用方法-3)
  - [输出示例](#输出示例-3)
  - [注意事项](#注意事项-1)
    
- [extract\_words\_from\_xlsx.py 将excel表格中的文本输出到txt中（带点格式还方便写代码）](#extract_words_from_xlsxpy-将excel表格中的文本输出到txt中带点格式还方便写代码)
  - [功能简介](#功能简介-1)
  - [环境要求](#环境要求-1)
  - [使用方法](#使用方法-4)
  - [输出示例](#输出示例-4)
  - [注意事项](#注意事项-2)
  
- [find\_missing\_keywords.py 看哪些给定词在所有子文件夹中都没有出现](#find_missing_keywordspy-看哪些给定词在所有子文件夹中都没有出现)
  - [功能简介](#功能简介-2)
  - [使用方法](#使用方法-5)
  - [输出示例](#输出示例-5)
  - [注意事项](#注意事项-3)

- [find\_unused\_words.py 看哪些给定词在所有文件（不包含子文件夹）名中都没出现](#find_unused_wordspy-看哪些给定词在所有文件不包含子文件夹名中都没出现)
  - [功能简介](#功能简介-3)
  - [使用方法](#使用方法-6)
  - [输出示例](#输出示例-6)
  - [注意事项](#注意事项-4)

- [move\_file\_to\_root.py 将所有文件移动到根目录](#move_file_to_rootpy-将所有文件移动到根目录)
  - [功能简介](#功能简介-4)
  - [使用方法](#使用方法-7)
  - [输出示例](#输出示例-7)
  - [注意事项](#注意事项-5)
  - [扩展功能](#扩展功能)

- [organize\_file\_by\_keywords(all).py 将文件夹中（包括子文件夹）所有文件按给定关键词组合](#organize_file_by_keywordsallpy-将文件夹中包括子文件夹所有文件按给定关键词组合)
  - [功能简介](#功能简介-5)
  - [使用方法](#使用方法-8)
  - [输出示例](#输出示例-8)
  - [注意事项](#注意事项-6)

- [organize\_file\_by\_keywords(current).py 将文件夹中所有文件按给定词组合，但仅限当前一级（不检查子文件夹）](#organize_file_by_keywordscurrentpy-将文件夹中所有文件按给定词组合但仅限当前一级不检查子文件夹)

- [organize\_file\_by\_prefix.py 按文件名第一个下划线前的文本在指定目录中整理文件到子文件夹](#organize_file_by_prefixpy-按文件名第一个下划线前的文本在指定目录中整理文件到子文件夹)
  - [功能简介](#功能简介-6)
  - [使用方法](#使用方法-9)
  - [输出示例](#输出示例-9)
  - [注意事项](#注意事项-7)
  - [扩展功能](#扩展功能-1)

- [结论](#结论)

# check_subfolders.py 检查每个子文件夹中的文件数量

## 功能说明

本脚本的作用是检查指定文件夹下的所有一级子文件夹，统计每个子文件夹内的文件数量（仅统计文件，不包括子文件夹）。如果某个子文件夹内的文件数量少于 6 个（当然可以变），脚本会打印警告信息，提示该子文件夹的文件数量不足。

## 使用方法

1. 找到以下代码中的 `folder_path` 变量：
   ```python
   folder_path = r'*******'
   ```
2. 将 `*******` 替换为您目标文件夹的绝对路径。例如：
   ```python
   folder_path = r'C:\Users\YourName\Documents\TargetFolder'
   ```

## 输出示例

假设目标文件夹结构如下：
```
C:\TestFolder
├── Subfolder1 (包含 3 个文件)
├── Subfolder2 (包含 7 个文件)
├── Subfolder3 (包含 2 个文件)
```

运行脚本后，输出如下：
```
子文件夹 'C:\TestFolder\Subfolder1' 的文件数量不足6个，当前文件数量：3
子文件夹 'C:\TestFolder\Subfolder3' 的文件数量不足6个，当前文件数量：2
```

## 错误处理

如果脚本运行过程中出现错误，例如目标路径不存在或权限不足，脚本会捕获异常并打印错误信息。例如：
```
检查过程中出现错误: [WinError 3] 系统找不到指定的路径: 'C:\\InvalidPath'
```

## 注意事项

1. **路径格式**：确保在 `folder_path` 中使用正确的路径格式。对于 Windows 用户，建议使用原始字符串（`r'路径'`）或双斜杠（`\\`）来避免转义问题。
2. **权限问题**：运行脚本时，确保对目标文件夹及其子文件夹具有读取权限。
3. **文件夹层级**：脚本仅检查目标文件夹下的 **一级子文件夹**，不会递归检查子文件夹中的子文件夹。

## 定制与扩展

如果您需要修改文件数量的阈值（默认是 6 个），可以调整以下代码中的数字：
```python
if len(files) < 6:
```
例如，将其改为检查是否少于 10 个文件：
```python
if len(files) < 10:
```
如果您需要对文件夹进行更多操作（例如删除不符合要求的子文件夹），可以在代码中扩展逻辑。


---

# create_docx.py 自动创建 Word 文档

## 功能说明

此脚本的功能是**在指定文件夹中自动创建指定数量的 `.docx` 文件**。文件命名格式为 `1.docx`, `2.docx`，以此类推。每个生成的文件中都会包含一个标题和一段简单的段落文字。此功能适用于批量创建测试文档或初始化文档结构。

---

## 依赖环境

如果尚未安装 `python-docx`，可以运行以下命令进行安装：
```bash
pip install python-docx
```

---

## 使用方法

打开脚本文件，找到以下代码：
```python
base_directory = r"******"
```
将其中的 `******` 修改为您目标文件夹的绝对路径。例如：
```python
base_directory = r"C:\Users\YourName\Documents\GeneratedDocs"
```

## 参数说明

### 函数 `create_docx_files(base_path, num_files=6)`
该函数的作用为在指定路径 `base_path` 下创建指定数量的 `.docx` 文件，具体参数说明如下：
- **`base_path`**：目标文件夹路径，必须为有效的绝对路径。如果路径不存在，脚本会打印提示信息并终止运行。
- **`num_files`**：要创建的 `.docx` 文件数量，默认为 6。您可以根据需要修改此值（例如 10 或 20）。

示例调用：
```python
create_docx_files(r"C:\MyFolder", num_files=10)
```

---

## 输出示例

假设指定的路径为 `C:\TestFolder`，并且运行脚本后：
1. 如果目标文件夹为空，脚本会创建以下文件：
   ```
   C:\TestFolder\1.docx
   C:\TestFolder\2.docx
   C:\TestFolder\3.docx
   C:\TestFolder\4.docx
   C:\TestFolder\5.docx
   C:\TestFolder\6.docx
   ```
2. 如果文件夹中已经存在某些文件（例如 `1.docx` 和 `2.docx`），脚本会跳过这些文件，仅创建缺失的文件。
   输出示例：
   ```
   文件已存在: C:\TestFolder\1.docx, 跳过创建。
   文件已存在: C:\TestFolder\2.docx, 跳过创建。
   已创建文件: C:\TestFolder\3.docx
   已创建文件: C:\TestFolder\4.docx
   已创建文件: C:\TestFolder\5.docx
   已创建文件: C:\TestFolder\6.docx
   ```

---

## 错误处理

1. **路径不存在**：如果指定的基础路径不存在，脚本会打印以下错误信息：
   ```
   指定的基础路径不存在: C:\InvalidPath
   ```
2. **文件保存失败**：如果由于权限问题或其他错误无法保存文件，脚本会捕获异常并提示：
   ```
   创建文件失败: C:\TestFolder\3.docx. 错误: [错误详细信息]
   ```

---

## 定制与扩展

1. **修改 Word 文档内容**：  
   您可以调整脚本中添加标题和段落文字的部分。例如：
   ```python
   doc.add_heading(f"文档 {i}", level=1)
   doc.add_paragraph(f"这是第 {i} 个生成的文档。")
   ```
   更改为：
   ```python
   doc.add_heading(f"My Custom Title {i}", level=1)
   doc.add_paragraph(f"This is document number {i}.")
   ```

2. **调整文件数量**：  
   您可以通过修改函数调用时的 `num_files` 参数控制生成文件的数量。例如，生成 10 个文件：
   ```python
   create_docx_files(base_directory, num_files=10)
   ```

3. **文件命名规则**：  
   如果需要更改文件命名规则，可以修改以下代码：
   ```python
   file_name = f"{i}.docx"
   ```
   例如，将文件名改为 `Doc_1.docx`, `Doc_2.docx`：
   ```python
   file_name = f"Doc_{i}.docx"
   ```

---

# create_subfolders.py 按给定词自动创建子文件夹

## 功能说明

此脚本的功能是**在指定的基础文件夹路径下，按照给定的关键词列表自动创建子文件夹**。每个子文件夹以关键词命名，用于批量初始化目录结构。

---

## 使用方法

### 步骤 1：修改基础路径
打开脚本文件，找到以下代码：
```python
base_directory = r"******"
```
将其中的 `******` 修改为您的目标文件夹的绝对路径。例如：
```python
base_directory = r"C:\Users\YourName\Documents\MyProject"
```

### 步骤 2：配置关键词列表
找到以下代码：
```python
keywords = ["关键词1","关键词2","关键词3"]
```
将其中的 `关键词1`、`关键词2` 等内容替换为您需要用作子文件夹名称的关键词。例如：
```python
keywords = ["项目A", "项目B", "项目C"]
```

---

## 输出示例

假设设置的基础路径为 `C:\TestFolder`，关键词列表为 `["项目A", "项目B", "项目C"]`，运行脚本后将会在路径 `C:\TestFolder` 下创建以下文件夹：
```
C:\TestFolder\项目A
C:\TestFolder\项目B
C:\TestFolder\项目C
```

终端输出示例：
```
已创建文件夹: C:\TestFolder\项目A
已创建文件夹: C:\TestFolder\项目B
已创建文件夹: C:\TestFolder\项目C
```

如果某个文件夹已存在，脚本不会覆盖它，仍会显示成功信息：
```
已创建文件夹: C:\TestFolder\项目A
```

---

## 定制与扩展

1. **修改文件夹命名规则**
   如果需要调整子文件夹的命名规则，例如为每个关键词添加前缀或后缀，可以修改以下代码：
   ```python
   folder_path = os.path.join(base_path, keyword)
   ```
   例如，为每个文件夹添加 "目录_" 前缀：
   ```python
   folder_path = os.path.join(base_path, f"目录_{keyword}")
   ```

2. **支持多级文件夹**
   如果需要创建多级文件夹（例如 `C:\TestFolder\项目A\子目录1`），可以直接在关键词中包含路径分隔符：
   ```python
   keywords = ["项目A\\子目录1", "项目B\\子目录2"]
   ```

3. **文件夹已存在时的处理**
   目前脚本使用 `os.makedirs(folder_path, exist_ok=True)`，如果文件夹已存在会直接跳过创建。如果需要标记这些文件夹为已存在，可以添加如下逻辑：
   ```python
   if os.path.exists(folder_path):
       print(f"文件夹已存在: {folder_path}")
   ```


---

# email_attachment_downloader.py 邮箱附件下载与过滤脚本

## 功能简介

此脚本通过 IMAP 协议连接邮箱，自动筛选邮件，**下载符合条件的附件并重命名**。  
下载条件为：邮件的**主题**或**正文**中包含指定的关键词。  
附件保存时会根据匹配的关键词或发件人邮箱进行重命名，避免文件名冲突。

---

## 功能特点

1. **关键词过滤**：脚本会检查邮件的主题和正文，判断是否包含指定关键词。
2. **自动解码**：支持邮件正文和附件文件名的编码自动识别与解码（通过 `chardet` 检测编码）。
3. **文件名处理**：自动清理文件名中的非法字符，确保文件名合法。
4. **保存路径指定**：可以自定义附件保存的目标文件夹。
5. **安全性**：支持使用邮箱授权码，确保脚本运行安全。

---

## 环境要求

所需第三方库：
    - `imaplib`：用于通过 IMAP 协议连接邮箱（Python 内置）。
    - `email`：用于解析邮件内容（Python 内置）。
    - `chardet`：自动检测编码。
    - `re`：用于正则处理非法字符（Python 内置）。

## 使用方法

在脚本的 `__main__` 部分，按照以下说明修改配置参数：

- **邮箱地址**：替换 `email_user` 为您的邮箱地址，例如：
  ```python
  email_user = "your_email@example.com"
  ```

- **邮箱密码或授权码**：替换 `email_password` 为您的邮箱密码或授权码（建议使用授权码）：
  ```python
  email_password = "your_email_password"
  ```

- **IMAP 服务器地址**：根据您的邮箱服务提供商填写 IMAP 服务器地址。例如：
  - QQ 邮箱：`imap.qq.com`
  - 163 邮箱：`imap.163.com`
  - Gmail 邮箱：`imap.gmail.com`
  ```python
  imap_server = "imap.qq.com"
  ```

- **关键词列表**：将 `keywords` 替换为您需要筛选的关键词。例如：
  ```python
  keywords = ["订单", "发票", "合同"]
  ```

- **保存路径**：设置附件保存的文件夹路径。例如：
  ```python
  save_path = r"C:\Users\YourName\Documents\EmailAttachments"
  ```
---

## 输出示例

假设您配置了以下参数：
- 邮箱地址：`example@example.com`
- 关键词列表：`["项目A", "合同"]`
- 保存路径：`C:\Attachments`

运行脚本后：

1. 如果邮件的主题或正文包含关键词 `项目A` 或 `合同`，附件将被下载并重命名为：
   ```
   C:\Attachments\项目A_文件名.docx
   C:\Attachments\合同_文件名.pdf
   ```

2. 如果未匹配任何关键词，将以发件人邮箱命名：
   ```
   C:\Attachments\sender_email_文件名.xlsx
   ```

3. 如果邮件没有附件，将提示：
   ```
   此邮件没有附件。
   ```

终端输出示例：
```
处理第 1 封邮件（ID: 1234）...
检测到编码: utf-8 (置信度: 0.99)
找到匹配关键词: 项目A
保存附件为: 项目A_合同.docx
已下载附件：C:\Attachments\项目A_合同.docx

处理第 2 封邮件（ID: 5678）...
未找到匹配关键词，使用发件人邮箱作为前缀。
保存附件为: sender_email_报告.xlsx
已下载附件：C:\Attachments\sender_email_报告.xlsx

此邮件没有附件。
```

---

## 注意事项

1. **邮箱授权码**：大多数邮箱（如 QQ 邮箱、Gmail）不支持直接使用邮箱密码登录，需要使用授权码。
   - QQ 邮箱：[如何获取授权码](https://service.mail.qq.com/cgi-bin/help?subtype=1&&no=1001256&&id=28)。
   - Gmail：[启用 IMAP 并获取授权码](https://support.google.com/mail/answer/7126229)。

2. **IMAP 协议**：确保您的邮箱已开启 IMAP 协议。可以在邮箱的设置中启用：

   - QQ 邮箱：
     ```
     设置 -> 账户 -> POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV 服务 -> 开启 IMAP 服务
     ```

   - Gmail 邮箱：
     ```
     设置 -> 转发和 POP/IMAP -> 启用 IMAP
     ```

3. **附件保存路径**：确保目标路径存在或脚本具有创建文件夹的权限。

4. **关键词匹配**：脚本会检查邮件的**主题**和**正文**，如果文本中包含关键词的任意一个，即认为匹配成功。


---

# extract_words_from_xlsx.py 将excel表格中的文本输出到txt中（带点格式还方便写代码）

## 功能简介

此脚本旨在从指定的 `.xlsx` 格式的 Excel 文件中读取数据，并将每个单元格的内容写入到一个 `.txt` 文件中。每个单元格的内容会被双引号包裹，后面跟随逗号。脚本还提供了排除指定词语的功能，用户可以根据需要排除特定内容。

---

## 环境要求

**所需第三方库**：
   - `openpyxl`：用于读取 Excel 文件。

---

## 使用方法

打开脚本，找到以下示例用法部分，并根据您的需求修改相应的路径和设置：

- **输入 Excel 文件路径**：替换 `input_excel_path` 为您的 Excel 文件路径。例如：
  ```python
  input_excel_path = r"C:\Users\YourName\Documents\data.xlsx"
  ```

- **输出文本文件路径**：替换 `output_txt_path` 为输出 `.txt` 文件的路径。例如：
  ```python
  output_txt_path = r"C:\Users\YourName\Documents\output.txt"
  ```

- **排除词语列表**：可选功能，用于指定不需要写入输出文件的词语列表。例如：
  ```python
  exclude_list = ["无效词", "排除词语"]
  ```

---
## 输出示例

假设您配置了以下参数：
- 输入文件：`C:\Data\input.xlsx`
- 输出文件：`C:\Data\output.txt`
- 排除词语：`["排除词1", "排除词2"]`

运行脚本后，程序将读取 `input.xlsx` 中的所有单元格，将内容写入 `output.txt`。输出示例：
```plaintext
"内容1","内容2","Content3",
...
```
而这样的输出结果可以直接复制粘贴到python的列表中。

终端输出示例：
```
内容已成功写入 C:\Data\output.txt
总计词汇100个
```

---

## 注意事项

1. **文件路径格式**：确保路径使用正确的格式。对于 Windows 用户，建议在路径字符串前加 `r`，防止转义问题：
   ```python
   input_excel_path = r"C:\Users\YourName\Documents\data.xlsx"
   ```

2. **Excel 文件格式**：当前脚本支持 `.xlsx` 格式的 Excel 文件。如果使用其他格式，可能需要转换或使用其他库读取。

3. **排除词语功能**：请确保 `exclude_list` 中的词语与 Excel 中的内容完全匹配（区分大小写），否则无法正确排除。

4. **输出内容格式**：每个单元格内容后面会添加逗号，如果需要其他格式，请修改相关代码部分。

---

# find_missing_keywords.py 看哪些给定词在所有子文件夹中都没有出现

## 功能简介

此脚本用于在指定的主文件夹中查找各个子文件夹的名称，判断指定的关键词是否存在于这些子文件夹的名称中。脚本将返回未出现的关键词列表，并统计遍历的子文件夹数量。这在管理大量文件夹时非常实用，特别是当您需要确保某些关键词已在文件夹命名中使用时。

---

## 使用方法

在脚本中找到以下示例用法部分，并根据您的需求修改相关路径和关键词设置：

- **关键词列表**：替换 `keywords` 为您需要检查的关键词列表。例如：
  ```python
  keywords = ["项目A", "数据分析"]
  ```

- **主文件夹路径**：替换 `main_folder` 为您的实际主文件夹路径。例如：
  ```python
  main_folder = r"C:\Users\YourName\Documents\Projects"
  ```

---

## 输出示例

假设您配置了以下参数：
- 主文件夹路径：`C:\Projects`
- 关键词列表：`["项目A", "项目B"]`

运行脚本后，您将看到如下输出：
```
已遍历 5 个子文件夹。
以下关键词未在任何子文件夹名称中找到：
"项目A",
```

如果所有关键词都在子文件夹名称中找到：
```
已遍历 5 个子文件夹。
所有关键词都已在子文件夹名称中找到。
```

---
## 注意事项

**关键词匹配**：关键词匹配不区分大小写。确保关键词列表中的词语与子文件夹的命名规则一致。
**文件夹结构**：脚本只会遍历主文件夹中的直接子文件夹，而不会递归遍历更深层次的文件夹。


---

# find_unused_words.py 看哪些给定词在所有文件（不包含子文件夹）名中都没出现

## 功能简介

此脚本用于检查指定文件夹下的文件名是否包含给定的关键词列表，并输出未出现在任何文件名中的关键词。通过该脚本，您可以快速识别哪些内容未被正确标记或分类。

---

## 使用方法

在脚本中找到以下代码部分，并根据您的需求修改相关参数：

- **关键词列表**：将 `keywords` 替换为您需要检查的关键词列表。例如：
  ```python
  keywords = ["项目A", "报告", "数据"]
  ```

- **文件夹路径**：将 `root_folder_path` 替换为您需要遍历的文件夹路径。例如：
  ```python
  root_folder_path = r"C:\Users\YourName\Documents\Files"
  ```

---
## 输出示例

假设您配置了以下参数：
- 文件夹路径：`C:\Documents\Reports`
- 关键词列表：`["项目A", "项目B", "项目C"]`

脚本会检查该文件夹下的所有文件名，并输出以下结果：

### 示例 1：部分关键词未匹配
```
以下关键词没有出现在任何文件名中：
"项目B",
"项目C",
```

### 示例 2：所有关键词均匹配
```
所有关键词都出现在文件名中！
```

---

## 注意事项

**仅检查文件**：脚本默认忽略文件夹，只会检查指定路径下的文件名。如果需要包括文件夹名，请修改代码中的逻辑：
   ```python
   if os.path.isfile(file_path):  # 替换为 os.path.isdir(file_path) 来检查子文件夹
   ```

**递归查找**：当前脚本只会检查指定文件夹的文件名。如果需要递归遍历子文件夹，请考虑使用 `os.walk`：
   示例代码修改：
   ```python
   for root, _, files in os.walk(root_folder):
       for file_name in files:
           file_path = os.path.join(root, file_name)
           # 检查关键词
   ```

---

# move_file_to_root.py 将所有文件移动到根目录

## 功能简介

此脚本用于整理指定目录（大文件夹）下的所有子文件夹中的文件，**将所有文件移动到根目录**（大文件夹的主目录）。同时，脚本提供一个可选功能，用于删除整理完成后的空文件夹。

主要特点：
1. 自动将子文件夹中的文件移动到大文件夹的根目录。
2. 避免因文件名冲突导致覆盖，通过在文件名后添加数字后缀解决冲突。
3. 可选地删除整理后产生的空文件夹。

---

## 使用方法

在脚本中找到以下代码部分，并根据您的需求替换文件夹路径：
```python
root_folder_path = "******"  # 替换为你的大文件夹路径
```

例如，将其替换为：
```python
root_folder_path = r"C:\Users\YourName\Documents\MyFolder"
```

---

## 输出示例

运行脚本后，您会在终端中看到以下输出：

### 示例 1：文件移动
```
Moved: C:\Users\YourName\Documents\MyFolder\Subfolder1\file1.txt -> C:\Users\YourName\Documents\MyFolder\file1.txt
Moved: C:\Users\YourName\Documents\MyFolder\Subfolder2\file2.jpg -> C:\Users\YourName\Documents\MyFolder\file2.jpg
Moved: C:\Users\YourName\Documents\MyFolder\Subfolder1\file1.txt -> C:\Users\YourName\Documents\MyFolder\file1_1.txt
文件整理完成！
```

### 示例 2：删除空文件夹
```
Removed empty folder: C:\Users\YourName\Documents\MyFolder\Subfolder1
Removed empty folder: C:\Users\YourName\Documents\MyFolder\Subfolder2
```

---

## 注意事项

**文件名冲突**：如果子文件夹中存在同名文件，脚本会通过添加数字后缀（如 `_1`, `_2`）来避免覆盖。
**移动非文件夹内容**：脚本仅移动文件，不会移动文件夹。如果需要处理文件夹，请自行调整逻辑。
**删除空文件夹**：默认会删除整理完成后的空文件夹。如果不需要此功能，可以注释掉 `remove_empty_folders(root_folder_path)` 调用。
**不可逆操作**：在移动文件和删除文件夹之前，请确保您有备份，避免误操作导致数据丢失。

---
## 扩展功能

如果需要额外功能，可以根据以下建议修改：
**过滤特定文件类型**：如果只想移动特定文件类型（如 `.txt` 文件），可以在文件遍历时添加过滤条件，例如：
   ```python
   if filename.endswith(".txt"):
   ```

---

# organize_file_by_keywords(all).py 将文件夹中（包括子文件夹）所有文件按给定关键词组合

## 功能简介

此脚本用于遍历指定目录下的所有文件，根据文件名中的关键词，将文件分类到相应的子文件夹中。这在文件管理和组织中非常有用，能够帮助您快速整理大量文件。

主要功能包括：
1. 自动识别文件名中的关键词。
2. 为每个关键词创建对应的子文件夹（如果不存在）。
3. 将匹配的文件移动到相应的子文件夹。

---

## 使用方法

在脚本中找到以下代码部分，并根据您的需求进行修改：

- **文件夹路径**：将 `root_folder_path` 替换为您需要整理的文件夹路径。例如：
  ```python
  root_folder_path = r"C:\Users\YourName\Documents\MyFolder"
  ```

- **关键词列表**：将 `keywords` 替换为您希望检查的关键词列表。例如：
  ```python
  keywords = ["项目A", "报告", "数据"]
  ```
---

## 输出示例

运行脚本后，您会在终端中看到以下输出：

### 示例 1：文件整理
```
创建文件夹：C:\Users\YourName\Documents\MyFolder\项目A
移动文件：C:\Users\YourName\Documents\MyFolder\file1_项目A.txt -> C:\Users\YourName\Documents\MyFolder\项目A\file1_项目A.txt
创建文件夹：C:\Users\YourName\Documents\MyFolder\报告
移动文件：C:\Users\YourName\Documents\MyFolder\file2_报告.docx -> C:\Users\YourName\Documents\MyFolder\报告\file2_报告.docx
文件整理完成！
```

---

## 注意事项

**一个文件一个关键词**：如果一个文件名中包含多个关键词，脚本将文件移动到匹配的第一个关键词对应的子文件夹。
**文件夹创建**：如果目标子文件夹不存在，脚本会自动创建。

---

# organize_file_by_keywords(current).py 将文件夹中所有文件按给定词组合，但仅限当前一级（不检查子文件夹）
同上，略。


---

# organize_file_by_prefix.py 按文件名第一个下划线前的文本在指定目录中整理文件到子文件夹

## 功能简介

此脚本用于遍历指定目录及其子目录下的所有文件，**根据文件名第一个下划线 (`_`) 之前的文字，将文件整理到对应的子文件夹中**。如果文件名中没有下划线，脚本会跳过该文件。

主要功能包括：
1. 根据文件名前缀分类文件。
2. 自动创建子文件夹（以前缀命名）。
3. 将文件移动到对应的子文件夹。

---

## 使用方法

在脚本中找到以下代码部分，并根据您的需求进行修改：

- **文件夹路径**：将 `root_folder` 替换为您需要整理的文件夹路径。例如：
  ```python
  root_folder = r"C:\Users\YourName\Documents\MyFolder"
  ```

---

## 输出示例

运行脚本后，您会在终端中看到类似以下的输出：

### 示例 1：文件整理
```
创建子文件夹: C:\Users\YourName\Documents\MyFolder\ProjectA
移动文件 'ProjectA_Report1.txt' 到 'C:\Users\YourName\Documents\MyFolder\ProjectA'
创建子文件夹: C:\Users\YourName\Documents\MyFolder\ProjectB
移动文件 'ProjectB_Data.csv' 到 'C:\Users\YourName\Documents\MyFolder\ProjectB'
文件 'Notes.txt' 不包含下划线，跳过。
移动文件 'ProjectA_Summary.docx' 到 'C:\Users\YourName\Documents\MyFolder\ProjectA'

文件整理完成！
```

---
## 注意事项

**支持子文件夹中的文件**：
   - 脚本会递归遍历指定目录及其所有子目录的文件，但**子文件夹本身不会被移动或改名**。

---

## 扩展功能

如果需要增加功能，可以根据以下建议进行修改：
1. **自定义分隔符**：
   - 当前脚本使用下划线 `_` 作为分隔符。如果需要使用其他分隔符（如 `-` 或 `#`），可以修改以下代码：
     ```python
     prefix = file.split("_", 1)[0]
     ```
     替换为：
     ```python
     prefix = file.split("-", 1)[0]
     ```

2. **支持文件复制而不是移动**：
   - 如果需要保留原始文件，可以将 `shutil.move` 替换为 `shutil.copy`：
     ```python
     shutil.copy(file_path, new_file_path)
     ```

3. **日志输出到文件**：
   - 将脚本的所有输出保存到日志文件中，方便后续查看。可以使用以下代码：
     ```python
     with open("organize_log.txt", "a") as log_file:
         log_file.write(f"移动文件 '{file}' 到 '{subfolder_path}'\n")
     ```

---


# 结论
我现在的想法就是未来科技发展AI一定要具象化，不是现在打开一个聊天框的简单交互，而是通过多模态信息直接交互的实物，比如当一整个电脑都是AI时，让它成为真正的电脑管家。当然这也会涉及安全伦理问题了。