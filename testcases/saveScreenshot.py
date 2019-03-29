import time
from utils.Browsers import init_webdriver
from utils.AccountUrlData import *

browsers = ['IE']
env = 'QA'
partner = 'SOCN'
foldername = 'QA'

g = GetRelatedUrls(env, partner)
g.get_related_urls()
user = g.account
product_url = g.url_list


def login_etwon(driver, user, env):
    if env == 'QA':
        driver.get('https://qa.englishtown.com/partner/englishcenters/cn?')
    elif env == 'UAT':
        driver.get('https://smartuat2.englishtown.com/partner/englishcenters/cn?')
    time.sleep(3)

    username = driver.find_element_by_id('username')
    password = driver.find_element_by_id('password')
    login = driver.find_element_by_class_name('etc-login-btn')

    username.clear()
    username.send_keys(user)
    password.clear()
    password.send_keys(1)
    login.click()
    time.sleep(5)

def get_screenshot(foldername):
    for broswer in browsers: #all browsers
        driver = init_webdriver(broswer)
        login_etwon(driver, user, env)
        for k, v in product_url.items():  #all prducts
            filename = r'%s%s%s.png' % (broswer,user, k)
            driver.get(v)
            time.sleep(10)
            driver.save_screenshot(r'../' + foldername +'/' + filename)
            time.sleep(5)
        driver.close()

if __name__ == '__main__':
    #save screenshot to UAT folder
    get_screenshot(foldername)


