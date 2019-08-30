import requests
import json
import unittest
class GetPaper(unittest.TestCase):     #封装测试环境的初始化和还原的类
    def setUp(self):                 #放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！
        print("start test")
        pass
    def tearDown(self):             #与setUp()相对
        print("end test")
        pass

    def test_getNewPaper(self):
        '''获取新创建的卷子'''
        url = "https://betaedu.csdn.net/api/app/getPaper"
        content = {'userId': 'cpongo1', 'paperId': '95'}
        getPaper = requests.get(url=url, params=content)
        results = json.loads(getPaper.text)
        print(results)
        self.assertEqual("ok",results['msg'])     #断言判断接口返回是否符合要求，可以写多个断言！

    def test_losePaper(self):
        '''获取已经已失效的卷子'''
        url= "https://betaedu.csdn.net/api/app/getPaper"
        content = {'userId': 'cpongo1', 'paperId': '91'}
        getPaper = requests.get(url=url, params=content)
        results = json.loads(getPaper.text)
        print(results)
        self.assertEqual("该卷子已失效", results['msg'])

    def test_deletePaper(self):
        '''获取已经已删除的卷子'''
        url= "https://betaedu.csdn.net/api/app/getPaper"
        content = {'userId': 'cpongo1', 'paperId': '86'}
        getPaper = requests.get(url=url, params=content)
        results = json.loads(getPaper.text)
        print(results)
        self.assertEqual("该卷子已删除", results['msg'])

    def test_NonExistentPaper(self):
        '''获取不存在的卷子'''
        url= "https://betaedu.csdn.net/api/app/getPaper"
        content = {'userId': 'cpongo1', 'paperId': '10000'}
        getPaper = requests.get(url=url, params=content)
        results = json.loads(getPaper.text)
        print(results)
        self.assertEqual("该卷子不存在", results['msg'])

    def test_submitPaper(self):
        '''获取已经提交的卷子'''
        url = "https://betaedu.csdn.net/api/app/getPaper"
        content = {'userId': 'cpongo1', 'paperId': '93'}
        getPaper = requests.get(url=url, params=content)
        results = json.loads(getPaper.text)
        print(results)
        self.assertEqual("你已提交", results['msg'])

    def test_nologin(self):
        '''没有登录的学员获取卷子'''
        url = "https://betaedu.csdn.net/api/app/getPaper"
        content = {'userId': '', 'paperId': '93'}
        getPaper = requests.get(url=url, params=content)
        results = json.loads(getPaper.text)
        print(results)
        self.assertEqual("请先登录", results['msg'])

    def test_no_paperID(self):
        '''不填写卷子ID'''
        url = "https://betaedu.csdn.net/api/app/getPaper"
        content = {'userId': 'cpongo1', 'paperId': ''}
        getPaper = requests.get(url=url, params=content)
        results = json.loads(getPaper.text)
        print(results)
        self.assertEqual("非法操作", results['msg'])

if __name__=="__main__":
    unittest.main()