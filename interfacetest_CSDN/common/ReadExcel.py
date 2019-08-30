# -*- coding:utf-8 -*-
import xlrd
import xlwt
import os.path


class ReadExcel():
    def get_xls(self, xls_name, sheet_name):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        # 获取用例文件路径
        filepath = os.path.dirname(os.path.abspath('.'))
        filename = os.path.join(filepath + "/Date/" + xls_name)
        # print(filepath)
        # print(filename)
        cls = []
        file = xlrd.open_workbook(filename)  # 打开用例Excel
        sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
        # 获取这个sheet内容行数
        nrows = sheet.nrows
        # api = sheet.cell_value(1, 1)
        # header_temp = sheet.cell_value(1, 3)
        # header = eval(header_temp)
        # data=sheet.cell_value(1,4)
        # code=sheet.cell_value(1,5)
        # expect=sheet.cell_value(1,6)
        for i in range(nrows):  # 根据行数做循环
            if sheet.row_values(i)[0] != 'case_name':  # 如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
                cls.append(sheet.row_values(i))
        return cls


if __name__ == '__main__':  # 我们执行该文件测试一下是否可以正确获取Excel中的值
    print(ReadExcel().get_xls('check_paper.xlsx', 'checkPaper'))
    print(ReadExcel().get_xls('check_paper.xlsx', 'checkPaper')[1][1])
    print(ReadExcel().get_xls('check_paper.xlsx', 'checkPaper')[1][2])