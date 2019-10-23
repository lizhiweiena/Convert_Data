# coding: utf-8
# @Time    : 2019/10/15 16:10
# @Author  : 李志伟
# @Email   : lizhiweiena@163.com


import pandas as pd

# ========================== offline 数据集转换 .data和.solution -> csv ========================

TRAIN_DATA = 'O4_train.data'
TRAIN_SOLUTION = 'O4_train.solution'
TRAIN_CSV_DATA = 'O4_train_data.csv'
TRAIN_XLSX_DATA = 'O4_train_data.xlsx'

with open(TRAIN_DATA, 'r', encoding='utf-8') as data_file:  # 读取 .data 文件
    with open(TRAIN_SOLUTION, 'r', encoding='utf-8') as solution_file:  # 读取 .solution 文件（.data 文件中文本对应的索引）
        with open(TRAIN_CSV_DATA, 'w', encoding='utf-8') as O5_train_data:  # 将数据以需要的格式写入到O5_train_data文件中
            train_data_temp = data_file.readlines()  # content
            train_data_file = [train_data_temp[index].strip('\n').replace(',', '，') for index in range(len(train_data_temp))]

            solution = solution_file.readlines()  # label
            solution_to_label_index = [solution[index].replace(' ', '').find('1') for index in range(len(solution))]

            result = zip(train_data_file, solution_to_label_index)  # 将content和label 合并成 (content, label) 格式

            result_list = list(result)
            result_len = len(result_list)
            for index in range(result_len):
                elem = result_list[index]
                # 将元组中的元素拼接起来，中间用","隔开，即转成 csv 格式的数据
                train_data_elem = ",".join(str(data) for data in elem)  # 由于label是int类型，而join()操作仅支持str类型
                O5_train_data.write(train_data_elem + '\n')

# ========================== offline 数据集转换 .csv -> .xlsx ==================================

data = pd.read_csv(TRAIN_CSV_DATA, encoding='utf-8', names=['content', 'label'])
result = pd.DataFrame(data)
result.to_excel(TRAIN_XLSX_DATA, index=False)
print("end!")
