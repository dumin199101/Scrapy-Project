# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import RenminItem


class RenminnewsSpider(CrawlSpider):
    name = 'renminnews'
    # 去除非党建域下新闻
    allowed_domains = ['dangjian.people.com.cn']
    start_urls = ['http://dangjian.people.com.cn/GB/394443/']

    rules = (
        Rule(LinkExtractor(allow='index\\d+.html')),
        # 去除48小时新闻排行链接
        Rule(LinkExtractor(allow='c\\d+-\\d+.html',restrict_xpaths="//div[@class='p2j_con02 clearfix w1000']/div[@class='fl']/ul/li/a"), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = RenminItem()
        # 标题
        if len(response.xpath(
                "//div[@class='p2j_con03 clearfix w1000']/div[@class='text_con text_con01']/div[@class='text_c']/h1")) > 0:
            item['title'] = response.xpath(
                "//div[@class='p2j_con03 clearfix w1000']/div[@class='text_con text_con01']/div[@class='text_c']/h1/text()").extract()[0]
        elif len(response.xpath("//div[@id='main']/div[@class='w1000 txtCon clearfix']/h1")) > 0:
            item['title'] = response.xpath("//div[@id='main']/div[@class='w1000 txtCon clearfix']/h1/text()").extract()[0]
        # print(item['title'])
        # 发布时间
        if(len(response.xpath(
            "//div[@class='p2j_con03 clearfix w1000']/div[@class='text_con text_con01']/div[@class='text_c']/p[@class='sou']")))>0:
            pubdate = response.xpath(
                "//div[@class='p2j_con03 clearfix w1000']/div[@class='text_con text_con01']/div[@class='text_c']/p[@class='sou']/text()").extract()[
                0]
        elif len(response.xpath("//div[@id='main']/div[@class='w1000 txtCon clearfix']/div[@class='editor time1 clearfix']"))>0:
            pubdate = response.xpath("//div[@id='main']/div[@class='w1000 txtCon clearfix']/div[@class='editor time1 clearfix']/text()").extract()[0]

        item['pubdate'] = pubdate[:pubdate.rfind("来源")].strip().replace("年", "-").replace("月", "-").replace("日",
                                                                                                            " ") + ":00"
        # 来源
        if len(response.xpath(
            "//div[@class='p2j_con03 clearfix w1000']/div[@class='text_con text_con01']/div[@class='text_c']/p[@class='sou']/a"))>0:
            item['source'] = response.xpath(
                "//div[@class='p2j_con03 clearfix w1000']/div[@class='text_con text_con01']/div[@class='text_c']/p[@class='sou']/a/text()").extract()[0]
        elif len(response.xpath("//div[@id='main']/div[@class='w1000 txtCon clearfix']/div[@class='editor time1 clearfix']/a"))>0:
            item['source'] = response.xpath("//div[@id='main']/div[@class='w1000 txtCon clearfix']/div[@class='editor time1 clearfix']/a/text()").extract()[0]
        # 链接
        item['link'] = response.url
        # 编辑
        if len(response.xpath(
            "//div[@class='p2j_con03 clearfix w1000']/div[@class='text_con text_con01']/div[@class='text_c']/div[@class='edit']"))>0:
            item['editor'] = response.xpath(
                "//div[@class='p2j_con03 clearfix w1000']/div[@class='text_con text_con01']/div[@class='text_c']/div[@class='edit']/text()").extract()[0]
        elif len(response.xpath("//div[@id='main']/div[@class='w1000 txtCon clearfix']/div[@class='edit clearfix']"))>0:
            item['editor'] = response.xpath("//div[@id='main']/div[@class='w1000 txtCon clearfix']/div[@class='edit clearfix']/text()").extract()[0]
        # 内容
        if len(response.xpath(
            "//div[@class='p2j_con03 clearfix w1000']/div[@class='text_con text_con01']/div[@class='text_c']/div[@class='show_text']"))>0:
            item['content'] = response.xpath(
                "//div[@class='p2j_con03 clearfix w1000']/div[@class='text_con text_con01']/div[@class='text_c']/div[@class='show_text']").extract()[0]
        elif len(response.xpath("//div[@id='main']/div[@class='w1000 txtCon clearfix']/p"))>0:
            content = ''
            for i in range(0,len(response.xpath("//div[@id='main']/div[@class='w1000 txtCon clearfix']/p"))):
                 content += response.xpath("//div[@id='main']/div[@class='w1000 txtCon clearfix']/p").extract()[i]
            item['content'] = content

        yield item
