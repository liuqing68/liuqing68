# -*- coding:utf-8 -*-
from common.XlsEngine import XlsEngine_rd
import os
from common.ReadConfig import ReadConfig
from common.Logger import Log

log=Log()
class Get_Date():

    '''获取url'''
    def get_url(self, api):
        host = ReadConfig()
        url = host.get_config("host", "online") + '/' + api
        log.info("获取URL为："+url)
        return url


    #获取用例
    def getCase(self):
        filepath = os.path.abspath('.')
        filename = os.path.join(filepath + "/interfacetest_CSDN/Data/")
        data = XlsEngine_rd(filename)
        data.xlrd_open()
        sheet = data.xlrd_object.sheet_by_index(0)
        rows = sheet.nrows
        domain = sheet.cell_value(1, 1)
        header_temp = sheet.cell_value(2, 1)
        header = eval(header_temp)
        case_list = []
        for i in range(2, rows):
            # cell_velue=table
            case_list.append(sheet.row_values(i))
        return domain, case_list, header

    #结果检查

    def resultCheck(self,actual_result, expect_result):
        result = "Failed"
        actualre = actual_result.content
        area = (expect_result.split(':'))[0]
        expect = (expect_result.split(':'))[1]
        if area == "response_code":
            if str(actual_result.status_code) == expect:
                result = "Pass"
                actualre = "response_code:" + expect
        if area == "content":
            expect = expect_result.replace("content:", "").encode('utf-8')
            actual = actual_result.content
            if expect in str(actual):
                result = "Pass"
                actualre = expect
        return result, actualre

    #结果统计
    def countResult(self,resultlist):
        passcount = 0
        failcount = 0
        for result in resultlist:
            if result[5] == 'Pass':
                passcount += 1
            else:
                failcount += 1
        return passcount, failcount


if __name__ == '__main__':
    date=Get_Date()
    url=date.get_url('api/app/checkPaper')
    print(url)

