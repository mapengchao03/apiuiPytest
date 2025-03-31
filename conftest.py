# import pytest
# from base.basepage import WebPage
# @pytest.fixture(scope="session")
# def browser():
#     driver = WebPage()
#     yield driver
#     driver.quit_browser()
#
# @pytest.fixture(autouse=True)
# def cleanup(browser):
#     yield
#     # 清理cookies并返回空白页
#     browser.del_all_cookies()
#     browser.get_url("about:blank")