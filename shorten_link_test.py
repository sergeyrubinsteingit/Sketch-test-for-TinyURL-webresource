###################################################################
# Test for TinyURL web resource. The purpose of this test is to
# ensure the links are shortened as expected also
# in case of multiple repetitions of the process

from os.path import abspath
import os
import time
# import win32clipboard
# import kwargs as kwargs
# import kwargs
# from certisfi.__main__ import args
from selenium.webdriver.support import expected_conditions as expect_conds_
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


default_wbd_: webdriver
links_list_: list
links_list_doubles_: list
# Opens some arbitrary web resource to copy its links
# to use them in testing.
links_url_: str = 'https://www.techjob.co.il/salary-survey'
drv_path_: str = abspath('../read_clipboard/driver_').replace('/', os.path.sep)
drv_name_: str = 'chromedriver.exe'
servc_ = Service(drv_path_ + os.path.sep + drv_name_)
drv_chrome_ops_ = webdriver.ChromeOptions()
drv_chrome_ops_.add_experimental_option("detach", True)  # Preventing the browser from closing automatically:
default_wbd_ = webdriver.Chrome(service=servc_, options=drv_chrome_ops_)
links_list_ = []
links_list_doubles_ = []


# Checks for connection, if it is okay then navigates to the site
try:
    send_request_ = requests.get(links_url_)
    time.sleep(1)
    if send_request_.status_code == 200:
        default_wbd_.get(links_url_)
        print(
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'  # Upper border
            'Successfully connected!\n\n'
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')  # Lower border

except requests.ConnectionError:
    print(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'  # Upper border
        'No server connection.\n'
        'The test is shut down.\n\n'
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')  # Lower border

# Creates list of links
waiting_ = WebDriverWait(default_wbd_, 100).until(expect_conds_.presence_of_element_located((By.TAG_NAME, 'a')))
# Links on page as web elements
links_on_pg_: list = default_wbd_.find_elements(By.TAG_NAME, 'a')
# Extracts link hrefs into string list
links_list_ = [next_lnk.get_attribute('href') for next_lnk in links_on_pg_]
# Creates link list with each link doubled.
# It is needed to ensure that repetitive shortening
# returns the same shorten link
# links_list_doubles_ = []
for i in range(0, links_list_.__len__()):
    links_list_doubles_.append(links_list_[i])
    links_list_doubles_.append(links_list_[i])

# Opens TinyURS for testing
default_wbd_.get('https://tinyurl.com/app/')
default_wbd_.implicitly_wait(11)

# Testing begins here
print(
    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'  # Upper border
    'Testing is started.\n\n'
    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')  # Lower border
from test_part_2 import test_part_two
test_part_two()


if __name__ == '__main__':
    # noinspection PyArgumentList
    super().__init__(service=servc_)
