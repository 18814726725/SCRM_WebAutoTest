import configparser
from common.constant import CONF_DIR
import os

class ReadConf(configparser.ConfigParser):
    def __init__(self):
        super().__init__()
        # 创建加载开关文件env.ini的对象
        r = configparser.ConfigParser()
        # 读取开关文件中switch的值
        r.read(os.path.join(CONF_DIR,'env.ini'),encoding='utf-8')
        switch = r.get('env','switch')
        # 判断环境开关的值，读取对应的配置文件
        if switch == '0':
            self.read(os.path.join(CONF_DIR,'production_conf.ini'),encoding='utf8')
        elif switch == '1':
            self.read(os.path.join(CONF_DIR,'qiushi6_d.ini'),encoding='utf8')
        elif switch == '2':
            self.read(os.path.join(CONF_DIR,'qiushi6_q.ini'),encoding='utf8')

conf = ReadConf()


# filename = conf.get('excel','filename')
# print(filename)
# level = conf.get('logs','level').upper()
# ls_level = conf.get('logs','ls_level').upper()
# fs_level = conf.get('logs','ls_level').upper()
# logname = conf.get('logs','logname')
# logpath = conf.get('logs','logpath')
# maxBytes = conf.get('logs','maxBytes')
# backupCount = conf.get('logs','backupCount')
# print(level,ls_level,fs_level,logname,logpath,maxBytes,backupCount)