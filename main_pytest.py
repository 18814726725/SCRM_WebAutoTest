# pip install pytest -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
import pytest
if __name__ == '__main__':
    # 执行smoke标签的测试用例
    # pytest.main(["-m","smoke","--html=outputs/reports/pytest.html","--alluredir=outputs/allure"])
    # 执行所有的测试用例
    pytest.main(["--html=outputs/reports/pytest.html", "--alluredir=outputs/allure"])