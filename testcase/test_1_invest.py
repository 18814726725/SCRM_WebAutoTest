from pageobject.index_page import IndexPage
from pageobject.bid_page import BidPage
from pageobject.user_page import UserPage
import pytest
import logging
from datas import invest_datas as id


@pytest.fixture
def init(login_web):
    logging.info("测试用例类的前置，打开浏览器会话，访问网址")
    IndexPage(login_web).get_first_bid()
    bid_page = BidPage(login_web)
    yield (login_web,bid_page)
    logging.info("测试用例类的后置，关闭浏览器会话")

# fixture的执行顺序：login_web 包含了 init_driver的前置后置条件
# init_driver的前置
#   login_web的前置
#     init 的前置
#     init 的后置
#   login_web的后置
# init_driver的后置

# 测试用例的三部曲：前置后置、步骤、断言
@pytest.mark.usefixtures('init')
class TestInvest:
    def test_invest_sucess(self,init):
        logging.info("--------投资操作：正常场景-投资成功---------")
        # 标页面：获取投资前的用户金额
        user_balance_before = init[1].uaser_available()
        # 标页面：投资操作
        init[1].invest(id.success['money'])
        # 标页面：在投资成功的窗口中—点击查看并激活
        init[1].view_and_activate_button_clcik()
        # 断言 投资前的钱 - 投资后的钱 = 投资的金额
        # 个人页面：获取用户余额
        user_balance_after = UserPage(init[0]).uaser_available_userpage()
        # 断言--投资前的金额 - 投资后的金额 = 投资金额
        assert id.success['money'] == int(eval(user_balance_before) - eval(user_balance_after))

