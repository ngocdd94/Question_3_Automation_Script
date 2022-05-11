import os.path
from src.helper.helper import Helper
import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
# import elements page
from src.pages.home_page import HomePage
from src.pages.franchising_page import FranchisingPage
from src.pages.promotion_page import PromotionPage

driver = None
browser_name = ""


@pytest.fixture(scope="class", autouse=True)
def init_driver(request, browser):
    global driver
    global browser_name

    # list supported browser
    supported_browser = ["chrome", "edge"]

    # check browser parameter
    if not browser:
        raise Exception('please add --browser argument when run test')
    if browser not in supported_browser:
        raise Exception(f"browser: {browser} is not supported" + f"\n System only supported {supported_browser}")


    # install and run Chrome
    if browser in supported_browser and browser == "chrome":
        print("chrome is running...")
        driver = webdriver.Chrome(service=(ChromeService(ChromeDriverManager().install())))
    # install and run Edge
    if browser in supported_browser and browser == "edge":
        print("edge is running...")
        driver = webdriver.Edge(service=(EdgeService(EdgeChromiumDriverManager().install())))

    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(Helper.get_config("implicit_wait_time_out"))
    # init driver
    browser_name = driver.name
    request.cls.driver = driver
    request.cls.WebDriverWait = WebDriverWait

    # init pages
    request.cls.home_page = HomePage(driver=driver, WebDriverWait=WebDriverWait)
    request.cls.franchising_page = FranchisingPage(driver=driver, WebDriverWait=WebDriverWait)
    request.cls.promotion_page = PromotionPage(driver=driver, WebDriverWait=WebDriverWait)

    yield
    driver.quit()

# add option when run pytest via cli
def pytest_addoption(parser):
    # add --browser option for command line
    parser.addoption("--browser")


# create browser option
@pytest.fixture(scope='class')
def browser(request):
    # get option and return to request when run test function
    return request.config.getoption("--browser")

# @pytest.fixture(scope="function", autouse=True)
# def go_to_home_page(request):
#     request.cls.driver.get(Helper.get_config("base_url"))


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config._metadata["Browser"] = browser_name


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url(Helper.get_config("base_url")))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # add directory
            report_directory = os.path.dirname(os.path.abspath(__file__)) + "\\images\\"
            # get test name
            file_name = report.nodeid.split("::")[-1]
            # take screenshot
            destination_file = os.path.join(report_directory, file_name)
            driver.save_screenshot(destination_file + ".png")
            # add image to html
            extra.append(pytest_html.extras.image(destination_file + ".png"))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = Helper.get_config("report title")
