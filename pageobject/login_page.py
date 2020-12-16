from element_location.login_page_locator import LoginPageLocator as loc
from pageobject.basepage import BasePage

# 登录页面的元素定位
class LoginPage(BasePage):
    # 管理端登录
    def admin_web_login(self,tenantname,username,passwd):
        # 等待页面元素出现
        self.input_text_ele(loc.user_loc, tenantname,'登录页面—输入微世界租户名称')
        self.input_text_ele(loc.user_loc,username,'登录页面—输入用户名')
        self.input_text_ele(loc.passwd_loc, passwd, '登录页面—输入密码')
        self.click_ele(loc.login_button_loc,'登陆页面-点击【登陆】按钮')

    # 客服端登录
    def kefu_web_login(self,tenantname,username,passwd):
        # 等待页面元素出现
        self.input_text_ele(loc.user_loc, tenantname,'登录页面—输入微世界租户名称')
        self.input_text_ele(loc.user_loc,username,'登录页面—输入用户名')
        self.input_text_ele(loc.passwd_loc, passwd, '登录页面—输入密码')
        self.click_ele(loc.login_button_loc,'登陆页面-点击【登陆】按钮')

    # 获取用户名、密码为空的提示
    def get_from_error_info(self):
        return self.get_text_ele(loc.form_error_info_loc,'登录页面-获取用户名、密码为空的提示')

    # 获取中间页的提示信息
    def get_page_content_error(self):
        return self.get_text_ele(loc.page_content_error_loc,'登录页面-获取中间页的提示信息')