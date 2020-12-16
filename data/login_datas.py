#---*-coding：utf-8-*---
'''
------------------------------
author:WangLe
time:2019/8/elementlocation 0003
E-mail:wangle10@foxmail.com
------------------------------
'''

# 登录成功的数据
success = {'username': '18684720553', 'passwd': 'python','check':'http://120.78.128.25:8765/Index/index'}


# 手机号为空/密码为空/手机号格式不正确、非数字.......的数据
invalid_datas = [
    {'username': '18684720553', 'passwd': '', 'check': '请输入密码'},
    {'username': '', 'passwd': 'python', 'check': '请输入手机号'},
    {'username': '186847205', 'passwd': 'python', 'check': '请输入正确的手机号'},
]
# 密码错误/手机号未注册
invalid_two_datas = [
    {'username': '18684720553', 'passwd': 'python4852', 'check': '帐号或密码错误!'},
    {'username': '18684720558', 'passwd': 'python', 'check': '此账号没有经过授权，请联系管理员!'}
]
