# -*- coding: utf-8 -*-
import scrapy

# 模拟登录人人网
class RenrenSpider(scrapy.Spider):
    name = 'renren_2'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/PLogin.do']

    def parse(self, response):
        # _xsrf = response.xpath("//_xsrf").extract()[0]
        yield scrapy.FormRequest.from_response(
            response,
            formdata={"email": "*********", "password": "##########"},  # , "_xsrf" = _xsrf},
            callback=self.parse_page
        )

    # 由个人主页定位到好友主页
    def parse_page(self, response):
        print("=========1===" + response.url)
        url = "http://www.renren.com/422167102/profile"
        yield scrapy.Request(url, callback=self.parse_newpage)

    # 好友主页信息
    def parse_newpage(self, response):
        print("===========2====" + response.url)
        with open("index-renren2.html", "w",encoding="utf-8") as filename:
            filename.write(response.body.decode("utf-8"))
