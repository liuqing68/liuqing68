import requests
import json
import unittest
class DoStartTime(unittest.TestCase):     #封装测试环境的初始化和还原的类
    def setUp(self):                 #放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！
        print("start test")
        pass
    def tearDown(self):             #与setUp()相对
        print("end test")
        pass

    def test_newPaper(self):
        #对正常的卷子开始计时
        url = "https://betaedu.csdn.net/api/app/doStartTime"
        payload = {'userId': 'cpongo4', 'paperId': '95'}
        doStartTime = requests.post(url=url, data=payload)
        results = json.loads(doStartTime.text)
        print(results)
        self.assertEqual("ok",results['msg'])

    
    def test_start_doneTime(self):
        #开始已经开始计时的卷子
        url = "https://betaedu.csdn.net/api/app/doStartTime"
        payload = {'userId': 'cpongo4', 'paperId': '95'}
        doStartTime = requests.post(url=url, data=payload)
        results = json.loads(doStartTime.text)
        print(results)
        self.assertEqual("ok",results['msg'])
    
    def test_losePaper(self):
        #开始已经失效的卷子
        url= "https://betaedu.csdn.net/api/app/doStartTime"
        payload = {'userId': 'cpongo1', 'paperId': '91'}
        doStartTime = requests.post(url=url, data=payload)
        results = json.loads(doStartTime.text)
        print(results)
        self.assertEqual("该卷子已失效", results['msg'])
    
    def test_deletePaper(self):
        #开始已经删除的卷子
        url= "https://betaedu.csdn.net/api/app/doStartTime"
        payload = {'userId': 'cpongo1', 'paperId': '86'}
        doStartTime = requests.post(url=url, data=payload)
        results = json.loads(doStartTime.text)
        print(results)
        self.assertEqual("该卷子已删除", results['msg'])
    
    def test_NonExistentPaper(self):
        #开始不存在的卷子
        url= "https://betaedu.csdn.net/api/app/doStartTime"
        payload = {'userId': 'cpongo1', 'paperId': '10000'}
        doStartTime = requests.post(url=url, data=payload)
        results = json.loads(doStartTime.text)
        print(results)
        self.assertEqual("该卷子不存在", results['msg'])

    def test_submitPaper(self):
        #开始已经提交的卷子
        url = "https://betaedu.csdn.net/api/app/doStartTime"
        payload = {'userId': 'cpongo1', 'paperId': '93'}
        doStartTime = requests.post(url=url, data=payload)
        results = json.loads(doStartTime.text)
        print(results)
        self.assertEqual("你已提交", results['msg'])

    def test_nologin(self):
        #没有登录的学员开始计时做卷子
        url = "https://betaedu.csdn.net/api/app/doStartTime"
        payload = {'userId': '', 'paperId': '93'}
        data_json=json.dumps(payload)
        doStartTime = requests.post(url=url, data=data_json)
        results = json.loads(doStartTime.text)
        print(results)
        self.assertEqual("请先登录", results['msg'])

    
    def test_no_paperID(self):
       #不填写卷子ID
       url = "https://betaedu.csdn.net/api/app/doStartTime"
       payload = {'userId': 'cpongo1', 'paperId': ''}
       doStartTime = requests.post(url=url, date=payload)
       results = json.loads(doStartTime.text)
       print(results)
       self.assertEqual("非法操作", results['msg'])

if __name__=="__main__":
    unittest.main()