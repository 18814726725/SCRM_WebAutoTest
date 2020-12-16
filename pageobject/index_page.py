# 新建包名为pageobject，新建index_page.py文件
from element_location.index_page_locator import IndexPageLocator as ioc
from pageobject.basepage import BasePage

# 登录之后首页的元素定位
class IndexPage(BasePage):
    def check_userName_exists(self):
        try:
            self.find_ele(ioc.account_loc,'首页-用户名账户是否存在')
            return True
        except:
            return False

    # 在首页获取第一个标
    def get_first_bid(self):
        # 等待首页页面元素的出现，选择某一项目，点击【抢投标】按钮
        self.click_ele(ioc.grab_bid_loc,'首页-点击【抢投标】按钮')
        return self
    # 获取第一个标的标名
    def get_first_bid_name(self):
        # 等待首页页面元素的出现，选择某一项目,获取标名并返回
        return self.get_text_ele(ioc.bid_name,'首页-选择某一项目,返回标名')

