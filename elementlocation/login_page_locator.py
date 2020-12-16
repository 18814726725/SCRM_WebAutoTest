from selenium.webdriver.common.by import By
# 定位元素
class LoginPageLocator:
    # 用户名定位
    user_loc = (By.XPATH, '// input[@name="phone"]')
    # 密码输入框定位
    passwd_loc = (By.XPATH, '//input[@name="password"]')
    # 登录按钮的定位
    login_button_loc = (By.XPATH, '//button[@class="btn btn-special"]')
    # 用户名、密码错误时的提示信息
    form_error_info_loc = (By.XPATH, '//div[@class="form-error-info"]')
    # 中间页的错误提示信息（账户未注册、账户或密码错误）
    page_content_error_loc = (By.XPATH, '//div[@class ="layui-layer-content"]')