import os

import pytest
from selenium import webdriver

driver = None

def pytest_addoption(parser):
    parser.addoption( "--browser", action="store", default="chrome", help="Browser option: chrome, firefox, edge" )
    parser.addoption("--env", action="store", default="qa", help="URL Environment option: qa, dev, prod")

@pytest.fixture
def setup_teardown_(request):
    global driver

    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--incognito")
        driver = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--incognito")
        driver = webdriver.Edge(options=options)

    driver.maximize_window()
    driver.implicitly_wait(5)

    web_url_env = request.config.getoption("--env")
    if web_url_env == "qa":
        driver.get("https://qa.primeroedge.co/login.aspx")
    elif web_url_env == "dev":
        driver.get("https://dev.primeroedge.co/login.aspx")
    elif web_url_env == "prod":
        driver.get("https://primeroedge.co/login.aspx")

    yield driver
    driver.quit()





@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in HTML report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
