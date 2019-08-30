# -*- coding:utf-8 -*-
# import requests
# import json
# import unittest
# from common.XlsEngine import XlsEngine_rd
# from common.DateEngine import getCase
# from common.HttpEngine import getData
from common.ReadConfig import ReadConfig

class CheckPaper():     #封装测试环境的初始化和还原的类
    # def setUp(self):                 #放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！
    #     print("start test")
    #     pass
    # def tearDown(self):             #与setUp()相对
    #     print("end test")
    #     pass

    # def test_newPaper(self):
    #     '''检查正常的卷子'''
    #     url = "https://betaedu.csdn.net/api/app/checkPaper"
    #     content = {'userId': 'cpongo1', 'paperId': '95'}
    #     checkPaper = requests.get(url=url, params=content)
    #     results = json.loads(checkPaper.text)
    #     print(results)
    #     self.assertEqual("ok",results['msg'])     #断言判断接口返回是否符合要求，可以写多个断言！
    #
    # def test_losePaper(self):
    #     '''检查已经已失效的卷子'''
    #     url= "https://betaedu.csdn.net/api/app/checkPaper"
    #     content = {'userId': 'cpongo1', 'paperId': '91'}
    #     checkPaper = requests.get(url=url, params=content)
    #     results = json.loads(checkPaper.text)
    #     print(results)
    #     self.assertEqual("该卷子已失效", results['msg'])
    #
    # def test_deletePaper(self):
    #     '''检查已经已删除的卷子'''
    #     url= "https://betaedu.csdn.net/api/app/checkPaper"
    #     content = {'userId': 'cpongo1', 'paperId': '86'}
    #     checkPaper = requests.get(url=url, params=content)
    #     results = json.loads(checkPaper.text)
    #     print(results)
    #     self.assertEqual("该卷子已删除", results['msg'])
    #
    # def test_NonExistentPaper(self):
    #     '''检查不存在的卷子'''
    #     url= "https://betaedu.csdn.net/api/app/checkPaper"
    #     content = {'userId': 'cpongo1', 'paperId': '10000'}
    #     checkPaper = requests.get(url=url, params=content)
    #     results = json.loads(checkPaper.text)
    #     print(results)
    #     self.assertEqual("该卷子不存在", results['msg'])
    #
    # def test_submitPaper(self):
    #     '''检查已经提交的卷子'''
    #     url = "https://betaedu.csdn.net/api/app/checkPaper"
    #     content = {'userId': 'cpongo1', 'paperId': '93'}
    #     checkPaper = requests.get(url=url, params=content)
    #     results = json.loads(checkPaper.text)
    #     print(results)
    #     self.assertEqual("你已提交", results['msg'])
    #
    # def test_nologin(self):
    #     '''没有登录的学员查看卷子'''
    #     url = "https://betaedu.csdn.net/api/app/checkPaper"
    #     content = {'userId': '', 'paperId': '93'}
    #     checkPaper = requests.get(url=url, params=content)
    #     results = json.loads(checkPaper.text)
    #     print(results)
    #     self.assertEqual("请先登录", results['msg'])
    #
    # def test_no_paperID(sef):
    #     '''不填写卷子ID'''
    #     url = "https://betaedu.csdn.net/api/app/checkPaper"
    #     content = {'userId': 'cpongo1', 'paperId': ''}
    #     checkPaper = requests.get(url=url, params=content)
    #     results = json.loads(checkPaper.text)
    #     print(results)
    #     self.assertEqual("非法操作", results['msg'])


    def testpaper(self):
        readconfig=ReadConfig()
        url=readconfig.get_testhost()



if __name__=="__main__":
    # unittest.main()
    test=CheckPaper()
    ceshi=test.testpaper()
    print(ceshi)