# coding=utf-8
import scrapy
from ..items import MaocuhuispiderItem
from bs4 import BeautifulSoup
import re


class MaocuHuiSpider(scrapy.Spider):
    name = 'maocu'
    allowed_domains = ['www.ccpit.org']
    url = 'http://www.ccpit.org/gongzuotz/index.htm?ChannelID=4135'
    start_urls = [url]

    def parse(self, response):
        # 查看response响应体数据
        # print(response.body.decode("utf-8"))
        # with open("response.txt","w",encoding="utf-8") as f1:
        #     f1.write(response.body.decode("utf-8"))
        # 改进版
        # 指定xml解析:指定解析库为lxml
        soup = BeautifulSoup(response.body, 'lxml')
        links = soup.select(".title > a")
        # 迭代发送每个请求，调用parse_item方法处理
        print(len(links))
        for link in links:
            # print(link['href'])
            yield scrapy.Request(link['href'],callback=self.parse_item)

    # 处理每个条目
    def parse_item(self,response):
        item = MaocuhuispiderItem()
        # 标题
        item['title'] = response.xpath("//div[@class='content-container container']/div[@class='row']/div[@class='col-xs-12 col-sm-12 col-md-12 col-lg-12']/div[@class='inner-new']/div[@class='content-new']/h1/text()").extract()[0]
        # 发布时间
        item['pubdate'] = response.xpath("//div[@class='content-container container']/div[@class='row']/div[@class='col-xs-12 col-sm-12 col-md-12 col-lg-12']/div[@class='inner-new']/div[@class='content-new']/div[@class='content-meta-new']/span[1]/text()").extract()[0]
        # 来源
        item['source'] = response.xpath("//div[@class='content-container container']/div[@class='row']/div[@class='col-xs-12 col-sm-12 col-md-12 col-lg-12']/div[@class='inner-new']/div[@class='content-new']/div[@class='content-meta-new']/span[@class='hidden-xs hidden-sm']/span[1]/text()").extract()[0]
        # 链接
        item['link'] = response.url
        # 简介: 取正文的第一行内容
        desc =  response.xpath("/html/body/div[@class='content-container container']/div[@class='row']/div[@class='col-xs-12 col-sm-12 col-md-12 col-lg-12']/div[@class='inner-new']/div[@class='content-new']/div[@class='content-body-new']")
        item['desc'] = "".join((desc.xpath("string(.)").extract()[0]).split())
        # 内容
        item['content'] = response.xpath("//div[@class='content-container container']/div[@class='row']/div[@class='col-xs-12 col-sm-12 col-md-12 col-lg-12']/div[@class='inner-new']/div[@class='content-new']/div[@class='content-body-new']").extract()[0]

        yield item