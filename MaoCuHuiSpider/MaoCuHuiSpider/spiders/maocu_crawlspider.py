# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MaocuhuispiderItem

"""
通过CrawlSpider类临时只实现第一页数据抓取，未实现其它翻页数据抓取
"""


class MaocuSpider(CrawlSpider):
    name = 'maocu_crawlspider'
    allowed_domains = ['www.ccpit.org']
    # 1.贸促通知公告
    start_urls = ['http://www.ccpit.org/gongzuotz/index.htm?ChannelID=4135']

    rules = (
        # 获取详情页链接
        Rule(LinkExtractor(allow='content_\\d+.htm',restrict_xpaths="//div[@class='channel-c-container container']/div[@class='row']/div[@class='bg-new col-xs-12 col-sm-12 col-md-12 col-lg-12']/div[@class='inner']/div[@class='row']/div[@class='right col-xs-12 col-sm-12 col-md-12 col-lg-9']/div[@class='inner']/div[@class='channel-content-list-new']"), callback='parse_item', follow=False),
    )



    def parse_item(self, response):
        item = MaocuhuispiderItem()
        item['title'] = response.xpath("//div[@class='content-container container']/div[@class='row']/div[@class='col-xs-12 col-sm-12 col-md-12 col-lg-12']/div[@class='inner-new']/div[@class='content-new']/h1/text()").extract()[0]
        print(item['title'])
        yield item
