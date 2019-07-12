# -*- coding: utf-8 -*-
import scrapy

# 模拟登录人人网
class RenrenSpider(scrapy.Spider):
    name = 'renren1'
    allowed_domains = ['renren.com']
    # start_urls = ['http://www.renren.com/SysHome.do']

    # 源码解析：遍历start_urls，发送请求
    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        yield scrapy.FormRequest(url=url,formdata={
            "email":"***********",
            "password":"############"
        },callback=self.parse_page)

    def parse_page(self, response):
        with open("index-renren.html", "w",encoding="utf-8") as filename:
            filename.write(response.body.decode("utf-8"))
