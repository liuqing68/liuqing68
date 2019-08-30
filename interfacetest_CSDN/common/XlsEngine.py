# coding=utf-8
import xlrd
import xlwt
import os.path

class XlsEngine_rd():

    def __init__(self, filename):
        self.xls_name = filename
        self.xlrd_object = None
        self.xlwt_object = None
        self.isopenfailed = True

    def xlrd_open(self):
        try:
            #xlrd.Book.encoding="utf-8"
            self.xlrd_object = xlrd.open_workbook(self.xls_name)
            self.isopenfailed = False
        except Exception as e:
            self.isopenfailed = True
            self.xlrd_object = None
            print(e)
        return [self.isopenfailed, self.xlrd_object]










