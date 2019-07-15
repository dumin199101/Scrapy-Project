# -*- coding:utf-8 -*-

# python的测试模块
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


class newsSelenium(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(executable_path=path, options=options)

    # 具体的测试用例方法，一定要以test开头
    def testNews(self):
        self.driver.get('http://www.12371.cn/special/xxgc18szqh/zyjs/')
        i = 1
        while True:
            # 指定xml解析
            soup = BeautifulSoup(self.driver.page_source, 'xml')
            # 返回当前页面所有新闻
            li_elements = soup.find(id="SUBD1384397203874929").find_all('li', {'class': 'zdy','style':"display: block;"})
            for li in li_elements:
                print(i,li.find('a').get_text())
                i = i + 1

            # page_source.find()未找到内容则返回-1
            if self.driver.page_source.find('下一页') < 0:
                break
            # 模拟下一页点击
            self.driver.find_element_by_link_text('下一页').click()

            # 向下滚动到页面底部
            # self.driver.execute_script("$(document).scrollTop($(document).height());")

    # 退出时的清理方法
    def tearDown(self):
        print('加载完成...')
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
