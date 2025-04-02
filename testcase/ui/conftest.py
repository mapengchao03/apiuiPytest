import pytest
from selenium import webdriver
from common.logger import logger
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="session")
def chrome_options():
    options = Options()
    # chrome_options.add_argument("--headless")  # 无头模式
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--ignore-certificate-errors")
    return options

@pytest.fixture(scope="session")
def driver(chrome_options):
    service = webdriver.ChromeService(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service, options=chrome_options)
    chrome_driver.maximize_window()
    chrome_driver.set_page_load_timeout(60)  # 设置页面加载超时时间
    chrome_driver.implicitly_wait(10)  # 隐式等待时间
    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture(autouse=True)
def cleanup(driver):
    # 清理cookies并返回空白页
    driver.delete_all_cookies()
    # 访问空白页并等待清理完成
    driver.get("about:blank")
    try:
        WebDriverWait(driver, 5).until(
            lambda d: d.execute_script("return document.readyState") == "complete")
    except Exception as e:
        logger.error(f"清理页面失败,错误信息: {e}")
    yield driver
