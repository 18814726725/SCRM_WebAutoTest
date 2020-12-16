from pageobject.basepage import BasePage
from element_location.bid_page_locator import BidPageLocator as tpl
from  element_location.user_page_locator import UserPageLocator as mpl

class BidPage(BasePage):
    # 获取用户的可用余额
    def uaser_available(self):
        return self.get_attribute_ele(tpl.available_balance_loc,'data-amount','投标页面-获取用户的可用余额')
    # 投资操作 - 输入投资金额为2000元，点击【投标】按钮
    def invest(self,amount):
        self.input_text_ele(tpl.available_balance_loc,amount,'投资页面-输入投资金额')
        BasePage(self.driver).click_ele(tpl.bid_button_loc,'投资页面-点击【投标】按钮')
    # 投资成功后，点击查看并激活按钮
    def view_and_activate_button_clcik(self):
        BasePage(self.driver).click_ele(tpl.view_and_activate_button_loc, '投资成功页面-点击【查看并激活】按钮')

































    def bidpage(self):
        # 获取投标前的可用余额
        tender_before_balance = mpl.myaccount_available_balance_loc.text
        # 等待投标页面元素的出现，在可用余额处输入投标金额为2000
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(tpl.available_balance_loc))
        self.driver.find_element(*tpl.available_balance_loc).send_keys("2000")
        # 点击【投标】按钮
        self.driver.find_element(*tpl.tender_button_loc).click()
        # 等待投标成功消息框的元素出现，点击【查看并激活】按钮
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(tpl.view_and_activate_button_loc))
        self.driver.find_element(*tpl.view_and_activate_button_loc).click()
        # 获取投标后的可用余额
        tender_after_balance = mpl.myaccount_available_balance_loc.text
        # 根据判断投标之前的余额和投标之后的余额是否相差投标金额，来确定是否投标成功  ---断言
        self.assertEquals(tender_before_balance,(int(tender_after_balance)+2000))






