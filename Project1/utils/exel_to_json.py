import json
from collections import OrderedDict

import xlrd

excel_file_path = "C:\\Users\\82105\\Desktop\\2021.1학기 수업시간표.xls"

excel_file = xlrd.open_workbook(excel_file_path)
sheet = excel_file.sheet_by_index(0)

data_list = list()

for row_num in range(1, sheet.nrows):
    data = OrderedDict()
    row_values = sheet.row_values(row_num)
    data['구분'] = row_values[0]
    data['과목코드'] = row_values[1]
    data['과목명'] = row_values[3]
    data['담당교수'] = row_values[11]

    data_list.append(data)

j = json.dumps(data_list, ensure_ascii=False)

with open('data.json', 'w+', encoding='utf-8') as f:
    f.write(j)
