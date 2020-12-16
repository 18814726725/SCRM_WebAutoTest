# 封装一个自己的日志类，用来进行日志文件的输出
import logging
from logging.handlers import RotatingFileHandler
from common.myconf import conf
from common.constant import LOGS_DIR
import os


logname = conf.get('logs','logname')
level = conf.get('logs','level').upper()
ls_level = conf.get('logs','ls_level').upper()
fs_level = conf.get('logs','ls_level').upper()

class MyLog(object):
    def __new__(cls, *args, **kwargs):
        # 创建日志收集器
        my_log = logging.getLogger(logname)
        # 设置日志收集器收集日志的等级（设置为debug等级）
        my_log.setLevel(level)
        # 创建日志输出渠道，输出在控制台
        l_s = logging.StreamHandler()
        # 设置控制台日志输出的等级（设置为info等级）
        l_s.setLevel(ls_level)
        # 创建日志输出渠道，输出日志文件
        f_s = RotatingFileHandler(os.path.join(LOGS_DIR,logname),
                                  maxBytes=1024*1024,
                                  backupCount=5,
                                  encoding='utf8')
        # 设置日志输出的等级（设置为debug等级）
        f_s.setLevel(fs_level)
        # 将日志收集器添加到日志输出渠道
        my_log.addHandler(f_s)
        my_log.addHandler(l_s)
        # 设置日志输出的格式
        ft = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        ft = logging.Formatter(ft)
        l_s.setFormatter(ft)
        f_s.setFormatter(ft)
        return my_log

log = MyLog()
# log.debug('自己定义的debug等级')
# log.info('自己定义的info等级')
# log.warning('自己定义的warning等级')
# log.error('自己定义的error等级')
# log.critical('自己定义的critical等级')