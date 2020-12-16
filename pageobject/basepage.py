from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.constant import screenshot_dir
from common import mylog
import logging
import time
import datetime
import os

class BasePage:
    def __init__(self, driver:WebDriver):
        self.driver = driver
    # 等待元素可见
    def wait_ele_visiable(self,loc,img_desc,timeout=30,frequency=0.5):
        try:
            WebDriverWait(self.driver, timeout,frequency).until(EC.visibility_of_element_located(loc))
        except:
            # 输出日志
            logging.exception("等待{}元素可见失败".format(loc))
            # 截图
            self.save_img(img_desc)
            raise # 抛出异常，让用例识别到异常使测试用例执行失败
        else:
            logging.info("在{}页面等待{}元素可见成功".format(img_desc,loc))
    # 等待元素存在
    def wait_ele_exists(self, loc, img_desc, timeout=30, frequency=0.5):
        start = datetime.datetime.now()  # 用datetime模块获取时间
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_element_located(loc))
        except:
            # 日志
            logging.exception("等待元素 {} 存在 失败！".format(loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。
        else:
            end = datetime.datetime.now()  # 用datetime模块获取当前时间
            logging.info("等待 {}  元素  {} 存在成功。耗时：{}".format(img_desc, loc, end - start))
    # 查找元素
    def find_ele(self,loc,img_desc):
        start = datetime.datetime.now()  # 用datetime模块获取时间
        self.wait_ele_visiable(loc,img_desc)
        try:
            ele = self.driver.find_element(*loc)
        except:
            logging.exception("在{}查找{}元素失败".format(img_desc,loc))
            self.save_img(img_desc)
            raise
        else:
            # 获取结束时间
            end = datetime.datetime.now()
            logging.info("在{}查找{}元素成功，耗时为{}".format(img_desc,loc,(end-start)))
            return ele
    # 点击元素（前提条件：等待元素可见、查找到元素）
    def click_ele(self,loc,img_desc,timeout=30,frequency=0.5):
        # 等待元素可见
        self.wait_ele_visiable(loc,img_desc,timeout=30,frequency=0.5)
        # 查找到元素
        ele = self.find_ele(loc,img_desc)
        try:
            ele.click()
        except:
            logging.exception("在{}点击{}元素失败".format(img_desc,loc))
            raise
        else:
            # 获取结束时间
            end = datetime.datetime.now()
            logging.info("在{}点击{}元素成功".format(img_desc,loc))
    # 在元素输入文本值（前提条件：等待元素可见、查找到元素）
    def input_text_ele(self,loc,value,img_desc,timeout=30,frequency=0.5):
        # 等待元素可见
        self.wait_ele_visiable(loc,img_desc,timeout=30,frequency=0.5)
        # 查找到元素
        ele = self.find_ele(loc,img_desc)
        try:
            ele.send_keys(value)
        except:
            logging.exception("在{}页面{}元素输入{}失败".format(img_desc,loc,value))
            raise
        else:
            logging.info("在{}页面{}元素输入{}成功".format(img_desc,loc,value))
            return self

    # 获取元素的文本值（前提条件：等待元素可见、查找到元素）
    def get_text_ele(self, loc,img_desc, timeout=30, frequency=0.5):
        # 等待元素可见
        self.wait_ele_visiable(loc, img_desc, timeout=30, frequency=0.5)
        # 查找到元素
        ele = self.find_ele(loc, img_desc)
        try:
            text = ele.text
        except:
            logging.exception("在{}页面获取{}元素的文本值失败".format(img_desc, loc))
            raise
        else:
            logging.info("在{}页面获取{}元素的文本值成功".format(img_desc, loc))
            return text

    # 获取元素的属性（前提条件：等待元素可见、查找到元素）
    def get_attribute_ele(self,loc,attr_name,img_desc,timeout=30,frequency=0.5):
        # 等待元素可见
        self.wait_ele_visiable(loc,img_desc,timeout=30,frequency=0.5)
        # 查找到元素
        ele = self.find_ele(loc,img_desc)
        try:
            atter_value = ele.get_attribute(attr_name)
        except:
            logging.exception("在{}页面获取{}元素的{}属性失败".format(img_desc,loc,attr_name))
            raise
        else:
            logging.info("在{}页面获取{}元素的{}属性成功".format(img_desc,loc,attr_name))
            return atter_value

    # 封装iframe切换
    def switch_iframe(self,refrence,img_desc):
        """
        :param refrence: 识别iframe，可以通过iframe的name属性、下标（index）、webelement对象、元组形式的定位表达式(By.XPATH,'//input[@name="password"]')
        :return:无
        """
        try:
            WebDriverWait(self.driver,20).until(EC.frame_to_be_available_and_switch_to_it(refrence))
        except:
            # 输出日志
            logging.exception("切换到{}的iframe{}失败".format(img_desc,refrence))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常使测试用例执行失败
        else:
            logging.info("切换到{}的iframe{}成功".format(img_desc,refrence))

    # 存放截图
    def save_img(self, img_description):
        """
        :param img_description:图片的描述 格式为 页面名称_功能名
        :return:
        """
        # 时间戳
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        print(now)
        # 图片路径 img_path = "图片存放目录" + img_description + "时间戳.png"
        filepath = "{}_{}.png".format(img_description,now)
        img_path = os.path.join(screenshot_dir,filepath)
        try:
            self.driver.save_screenshot(img_path)
        except:
            logging.exception("当前页面{}截图失败".format(img_description))
            raise  # 抛出异常，让用例识别到异常使测试用例执行失败
        else:
            logging.exception("截图成功，截图存放在{}".format(img_path))
# 封装上传文件操作、alter切换、下载操作、下拉列表操作
# window切换（先保留，学习完robot的切换之后再封装）

