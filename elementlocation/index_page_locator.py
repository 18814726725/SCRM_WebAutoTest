from selenium.webdriver.common.by import By

# 首页的元素定位
class IndexPageLocator:
    # 定位投标页签
    indexpage_bookmark = (By.XPATH,'//a[text()="投标"]')
    # 定位第一个抢投标按钮
    grab_bid_loc = (By.XPATH,'//a[@class="btn btn-special"]')
    # 定位第一个标名
    bid_name = (By.XPATH,'//span[@class="fs-22"]')
    # 定位【我的帐户xxx】元素
    account_loc = (By.XPATH, '//a[text()="我的帐户[python10]"]')