# 前置和后置操作，只执行一次
# @pytest.fixture(scope="session", autouse=True)
# def open_browser():
#     web_page.get_url(conf_manager.host)
#     log.info("前置操作打开浏览器")
#     yield
#     web_page.quit_browser()
#     log.info("后置操作关闭浏览器")
