#用openpyxl读取excel文件
import openpyxl

#读取第一列的数据，逐行添加入列表
def read_excel(file_name):
    wb = openpyxl.load_workbook(file_name)
    sheet = wb.active
    rows = sheet.rows
    col = []
    for row in rows:
        col.append(row[0].value)
    return col


TOPIC=read_excel("新建 XLSX 工作表.xlsx")
print(TOPIC)
