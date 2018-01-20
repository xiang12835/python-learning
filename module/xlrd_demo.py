# coding=utf-8
import xlrd
import os


def read_excel(file_name):

    # 打开文件
    workbook = xlrd.open_workbook(file_name)
    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
    datas = []

    for row in xrange(1, sheet1.nrows):
        # print row
        data = {
            'order_id': str(sheet1.cell(row, 0).value).strip(),
            'phone': str(int(sheet1.cell(row, 1).value)).strip(),
            'express_code': str(int(sheet1.cell(row, 2).value)).strip(),
        }
        datas.append(data)

    return datas


if __name__ == "__main__":

    f = os.path.join(os.path.dirname(__file__), "excel_for_xlrd.xlsx")

    print read_excel(f)
