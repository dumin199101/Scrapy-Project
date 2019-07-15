# coding=utf-8
"""
谷歌无头浏览器测试
谷歌浏览器版本：V75.0
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def chrome():
    """
    测试谷歌无头浏览器
    :return:
    """
    # 这个是一个用来控制chrome以无界面模式打开的浏览器
    # 创建一个参数对象，用来控制chrome以无界面的方式打开
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # 驱动路径 谷歌的驱动存放路径,或者将此路径放入环境变量
    path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

    # 创建浏览器对象
    # chrome_options参数已过时，使用opitons参数代替
    # browser = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
    browser = webdriver.Chrome(executable_path=path,options=chrome_options)

    url = "https://www.baidu.com"
    browser.get(url)
    time.sleep(3)
    browser.save_screenshot('baidu.png')

    browser.quit()




def main():
    chrome()

if __name__ == '__main__':
    main()