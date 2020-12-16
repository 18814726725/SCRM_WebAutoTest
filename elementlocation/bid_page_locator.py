from selenium.webdriver.common.by import By

# 投标页面的元素定位
class BidPageLocator:
    # 金额输入框   //div[@class="clearfix left"]  //input[@class="form-control invest-unit-investinput"]
    available_balance_loc = (By.XPATH,'//input[@class="form-control invest-unit-investinput"]')
    # 投标按钮的定位
    bid_button_loc = (By.XPATH, '//button[@class="btn btn-special height_style"]')
    # 查看并激活按钮的定位
    view_and_activate_button_loc = (By.XPATH, '//div[@class="layui-layer-content"]//button[text()="查看并激活"]')
