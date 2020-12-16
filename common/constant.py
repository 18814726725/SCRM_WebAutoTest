import os
# 框架项目顶层目录
# 获取项目的根目录路径
base_dir = os.path.dirname(os.path.dirname(__file__))
# 测试数据存放目录
datas_dir =  os.path.join(base_dir,"datas")
# 测试用例存放目录
testcase_dir =  os.path.join(base_dir,"testcase")
# 测试报告存放目录
htmlreport_dir =  os.path.join(base_dir,"outputs/reports")
# 测试日志存放目录
logs_dir =  os.path.join(base_dir,"outputs/logs")
# 配置文件存放目录
config_dir =  os.path.join(base_dir,"config")
# 屏幕截图存放目录
screenshot_dir = os.path.join(base_dir,"outputs/imgs")
