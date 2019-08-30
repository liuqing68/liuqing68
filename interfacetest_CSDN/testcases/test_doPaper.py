import requests
import json
import unittest

class DoPaper(unittest.TestCase):     #封装测试环境的初始化和还原的类
    def setUp(self):                 #放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！
        print("start test")
        pass
    def tearDown(self):
        print("end test")
        pass

    def test_doNewPaper(self):
        #做已经生成的正常卷子
        #调用getPaper接口生成卷子
        self.url1 = "https://betaedu.csdn.net/api/app/getPaper"
        self.content = {'userId': 'cpongo2', 'paperId': '93'}
        getPaper = requests.get(url=self.url1, params=self.content)
        results = json.loads(getPaper.text)
        print(results)
        #答题
        self.url = "https://betaedu.csdn.net/api/app/doPaper"
        self.data= {'userId': 'cpongo2',
                   'paperId': 93,
                   "data":json.dumps({
                       "79_1": "153_1",
                       "80_2": [
                           "156_1",
                           "157_2"
                       ],
                       "81_6": "160_1",
                       "82_4": "测试填空",
                       "78_5": "测试课后练习"
                   })
                   }

        doPaper = requests.post(url=self.url, data=self.data)
        results = json.loads(doPaper.text)
        print(results)
        self.assertEqual("ok",results['msg'])

    def doingPaper(self):
        #做正在考试中的卷子
        self.url = "https://betaedu.csdn.net/api/app/doPaper"
        self.data1 = {'userId': 'cpongo5', 'paperId': 95, "data": json.dumps({"79_1": "153_1"})}
        doPaper = requests.post(url=self.url, data=self.data1)
        results = json.loads(doPaper.text)
        print(results)
        self.assertEqual("考试中", results['msg'])
    
    def test_losePaper(self):
        #做已经失效的卷子
        self.url = "https://betaedu.csdn.net/api/app/doPaper"
        self.data1 = {'userId': 'cpongo1', 'paperId': 91, "data": json.dumps({"79_1": "153_1"})}
        doPaper = requests.post(url=self.url, data=self.data1)
        results = json.loads(doPaper.text)
        print(results)
        self.assertEqual("该卷子已失效", results['msg'])
    
    def test_deletePaper(self):
        #做已经已删除的卷子
        self.url= "https://betaedu.csdn.net/api/app/doPaper"
        self.data1 = {'userId': 'cpongo1', 'paperId': 86, "data": json.dumps({"79_1": "153_1"})}
        doPaper = requests.post(url=self.url, data=self.data1)
        results = json.loads(doPaper.text)
        print(results)
        self.assertEqual("该卷子已删除", results['msg'])
    
    def test_NonExistentPaper(self):
        #做不存在的卷子
        self.url= "https://betaedu.csdn.net/api/app/doPaper"
        self.data1 = {'userId': 'cpongo1', 'paperId': 10000, "data": json.dumps({"79_1": "153_1"})}
        doPaper = requests.post(url=self.url, data=self.data1)
        results = json.loads(doPaper.text)
        print(results)
        self.assertEqual("该卷子不存在", results['msg'])
    
    def test_submitPaper(self):
        self.url = "https://betaedu.csdn.net/api/app/doPaper"
        self.data1 = {'userId': 'cpongo5', 'paperId': 95, "data": json.dumps({"79_1": "153_1"})}
        doPaper= requests.post(url=self.url, data=self.data1)
        results = json.loads(doPaper.text)
        print(results)
        self.assertEqual("你已提交", results['msg'])
    
    def test_nologin(self):
        #没有登录的学员做题
        url = "https://betaedu.csdn.net/api/app/doPaper"
        payload = {'userId': '',
                   'paperId': '93',
                   'date': {"79_1": "153_1"}
                   }
        doPaper = requests.post(url=url, date=payload)
        results = json.loads(doPaper.text)
        print(results)
        self.assertEqual("请先登录", results['msg'])
    
    def test_no_paperID(self):
        #不填写卷子ID
        url = "https://betaedu.csdn.net/api/app/doPaper"
        payload = {'userId': 'cpongo1',
                   'paperId': '',
                   'date': {"79_1": "153_1"}
                   }
        doPaper = requests.post(url=url, date=payload)
        results = json.loads(doPaper.text)
        print(results)
        self.assertEqual("非法操作", results['msg'])

if __name__=="__main__":
    unittest.main()