from selenium import webdriver
from datas import common_datas as cd
import pytest
from pageobject.login_page import LoginPage
from pageobject.index_page import IndexPage
from pageobject.bid_page import BidPage
import logging

# 调用定义好的fixtrue
# 在测试类\测试用例的前面，使用@pytest.mark.usefixtures("定义好的fixtrue函数名称")
# 如果有返回值，那么fixtrue的函数名称，作为测试用例的参数，将返回值传递测试用例。fixtrue的函数名称==返回值

# 登陆操作的前置:打开浏览器、访问网址
@pytest.fixture   # 声明他之下的函数是一个pytest的前置、后置条件
def init_driver():
    # 定义前置
    driver = webdriver.Chrome()
    driver.get(cd.login_url)
    driver.maximize_window()
    yield driver # common.隔开前置、后置条件 data.返回值
    # 后置
    driver.quit()

# 投资操作的前置:打开浏览器、访问网址、登陆网站
@pytest.fixture
def login_web(init_driver):   # 将init_driver的前置、后置条件进行调用
    LoginPage(init_driver).login(cd.username,cd.passwd)
    yield init_driver


# fixture的执行顺序：login_web 包含了 init_driver的前置后置条件
# init_driver的前置
#   login_web的前置
#   login_web的后置
# init_driver的后置

