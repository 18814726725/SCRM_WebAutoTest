from selenium.webdriver.common.by import By
# 帐户中心页面的元素定位
class UserPageLocator:
    # 定位可用余额元素
    user_available_balance_loc = (By.XPATH,'//li[@class="color_sub"]')
    # 定位投资项目页签
    invest_bookmark = (By.XPATH,'//div[text()="投资项目"]')
    # 定位最近一次的投标记录的标名
    last_bid_record_name_loc = (By.XPATH, '//div[@class="deal_tab_font1"]//a')
    # 定位最近一次的投标记录的投资金额
    last_bid_record_amount_loc = (By.XPATH, '//div[text()="本金"]/preceding-sibling::div[@class="deal_tab_font1"]')
