# -*- coding:utf-8 -*-
import os.path
import  configparser

#logger = Logger(logger="readconfig").getlog()

class ReadConfig():

    def __init__(self,filepath=None):
        if filepath:
            configpath = filepath
        else:
            # dir = os.path.dirname(os.path.realpath(__file__))#获取根目录
            dir = os.path.dirname(os.path.abspath('.'))  # 获取当前文件夹所在目录
            #configpath = dir + '/common/config.conf'
            configpath = os.path.join(dir + '/common/config.conf')
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def get_config(self,configKey,hostname):
        self.configKey=configKey
        self.hostname=hostname
        hostVelue = self.cf.get(self.configKey, self.hostname)
        # logger.info("获取测试环境域名" % test)
        return hostVelue





if __name__ == '__main__':
    test = ReadConfig()
    t = test.get_config("host", "online")
    print(t)


