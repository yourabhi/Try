from behave import *
from selenium import webdriver
@given(u'Launch Chrome Browser')
def launch_chrome(context):
    driver = webdriver.Chrome(executable_path="/home/global/Desktop/Softwares/ChromeDriver/chromedriver")
    driver.maximize_window()


@when(u'open the homepage of orangeHRM')
def homepage_open(context):
    driver.get('')
    wait = WebDriverWait(driver, 3)

@then(u'Verify Logo is present there')
def jhghdsilfjg(context):



@then(u'Close the browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Close the browser')
