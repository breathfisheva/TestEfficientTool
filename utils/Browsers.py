from  selenium import webdriver

def init_webdriver(broswer):
    if broswer == 'Firefox':
        return webdriver.Firefox()
    elif broswer == 'Chrome':
        return webdriver.Chrome()
    elif broswer == 'IE':
        return  webdriver.Ie()
    elif broswer == 'Edge':
        return webdriver.Edge()


