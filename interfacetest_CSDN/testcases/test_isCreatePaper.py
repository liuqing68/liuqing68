import requests
import json
import unittest
class IsCreatePaper(unittest.TestCase):     #封装测试环境的初始化和还原的类
    def setUp(self):                 #放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！
        print("start test")
        pass
    def tearDown(self):
        print("end test")
        pass

    def test_newPaper(self):
        '''查看已经生成的正常卷子'''
        url = "https://betaedu.csdn.net/api/app/isCreatePaper"
        content = {'userId': 'cpongo1', 'paperId': '95'}
        isCreatePaper = requests.get(url=url, params=content)
        results = json.loads(isCreatePaper.text)
        print(results)
        self.assertEqual("ok",results['msg'])

    def test_waitPaper(self):
        '''查看等待生成卷子'''
        url = "https://betaedu.csdn.net/api/app/isCreatePaper"
        content = {'userId': 'cpongo2', 'paperId': '95'}
        isCreatePaper = requests.get(url=url, params=content)
        results = json.loads(isCreatePaper.text)
        print(results)
        self.assertEqual("waiting",results['msg'])

    def test_losePaper(self):
        '''生成已经已失效的卷子'''
        url= "https://betaedu.csdn.net/api/app/isCreatePaper"
        content = {'userId': 'cpongo1', 'paperId': '91'}
        isCreatePaper = requests.get(url=url, params=content)
        results = json.loads(isCreatePaper.text)
        print(results)
        self.assertEqual("该卷子已失效", results['msg'])

    def test_deletePaper(self):
        '''生成已经已删除的卷子'''
        url= "https://betaedu.csdn.net/api/app/isCreatePaper"
        content = {'userId': 'cpongo1', 'paperId': '86'}
        isCreatePaper = requests.get(url=url, params=content)
        results = json.loads(isCreatePaper.text)
        print(results)
        self.assertEqual("该卷子已删除", results['msg'])

    def test_NonExistentPaper(self):
        '''生成不存在的卷子'''
        url= "https://betaedu.csdn.net/api/app/isCreatePaper"
        content = {'userId': 'cpongo1', 'paperId': '10000'}
        isCreatePaper = requests.get(url=url, params=content)
        results = json.loads(isCreatePaper.text)
        print(results)
        self.assertEqual("该卷子不存在", results['msg'])

    def test_submitPaper(self):
        '''生成已经提交的卷子'''
        url = "https://betaedu.csdn.net/api/app/isCreatePaper"
        content = {'userId': 'cpongo1', 'paperId': '93'}
        isCreatePaper = requests.get(url=url, params=content)
        results = json.loads(isCreatePaper.text)
        print(results)
        self.assertEqual("你已提交", results['msg'])

    def test_nologin(self):
        '''没有登录的学员生成卷子'''
        url = "https://betaedu.csdn.net/api/app/isCreatePaper"
        content = {'userId': '', 'paperId': '93'}
        isCreatePaper = requests.get(url=url, params=content)
        results = json.loads(isCreatePaper.text)
        print(results)
        self.assertEqual("请先登录", results['msg'])

    def test_no_paperID(self):
        '''不填写卷子ID'''
        url = "https://betaedu.csdn.net/api/app/isCreatePaper"
        content = {'userId': 'cpongo1', 'paperId': ''}
        isCreatePaper = requests.get(url=url, params=content)
        results = json.loads(isCreatePaper.text)
        print(results)
        self.assertEqual("非法操作", results['msg'])

if __name__=="__main__":
    unittest.main()