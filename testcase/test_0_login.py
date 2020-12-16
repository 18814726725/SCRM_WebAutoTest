#---*-coding：utf-8-*---
'''
------------------------------
author:WangLe
time:2019/8/common 0001
E-mail:wangle10@foxmail.com
------------------------------
'''

# 打开网页 - 登录 - 断言
from pageobject.login_page import LoginPage
from pageobject.index_page import IndexPage
from datas import login_datas as ld
import pytest

# 测试用例的三步曲：前置+后置、步骤、断言
@pytest.mark.usefixtures("init_driver")   # 表示调用名为init_driverde前置、后置条件
class TestLogin:
    # 正常用例 - 登陆+首页
    @pytest.mark.smoke
    def test_login_success(self,init_driver):  # fixture的函数名称，作为参数传给测试用例。函数名称等于fixture执行后的返回值
        # 用例 =  登录页的登陆功能 + 首页的检查用户昵称存在的功能
        # 操作步骤
        LoginPage(init_driver).login(ld.success['username'],ld.success['passwd'])
        # 断言 -页面是否存在  我的账户 元素   元素定位 + 元素操作
        assert IndexPage(init_driver).check_userName_exists()   # 测试对象+测试数据
        # 断言
        assert  init_driver.current_url == ld.success['check']
        # print("跳转的url为{}".format(init_driver.current_url))

    # 将所有无效的数据都存放在invalid_datas列表中，每一个元素存放在字典中
    @pytest.mark.parametrize('data',ld.invalid_datas)   # 参数化实现ddt
    def test_login_nopasswd(self,data,init_driver):
        # 操作步骤
        LoginPage(init_driver).login(data["username"], data["passwd"])
        # 断言
        assert data["check"] == LoginPage(init_driver).get_from_error_info()

    @pytest.mark.parametrize('data',ld.invalid_two_datas)
    def test_login_wrongpawwsd(self,data,init_driver):
        # 操作步骤
        LoginPage(init_driver).login(data["username"],data["passwd"])
        # 断言
        assert data["check"] == LoginPage(init_driver).get_page_content_error()
