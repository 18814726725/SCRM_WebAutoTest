from selenium.webdriver.remote.webdriver import WebDriver
from element_location.user_page_locator import UserPageLocator as mpl
from pageobject.basepage import BasePage

class UserPage:
    def __init__(self,driver:WebDriver):
        self.driver = driver
    # 获取用户的可用余额
    def uaser_available_userpage(self):
        return BasePage(self.driver).get_text_ele(mpl.user_available_balance_loc,'用户中心页面-获取用户的可用余额').strip("元")
    # 切换进个人页面的投资项目页签中
    def switch_invest_bookmark_click(self):
        BasePage(self.driver).click_ele(mpl.invest_bookmark,'用户中心页面-切换进投资项目页签中')
    # 获取第一条投资记录的标名
    def get_first_invest_name(self):
        return BasePage(self.driver).get_text_ele(mpl.last_bid_record_name_loc, '投资项目页签-获取第一条投资记录的标名')
    # 获取第一条投资记录的投资金额
    def get_first_invest_amount(self):
        return BasePage(self.driver).get_text_ele(mpl.last_bid_record_amount_loc, '投资项目页签-获取第一条投资记录的投资金额')