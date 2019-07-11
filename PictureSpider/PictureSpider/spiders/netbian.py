# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import PicturespiderItem


class NetbianSpider(CrawlSpider):
    name = 'netbian'
    allowed_domains = ['netbian.com']
    start_urls = ['http://www.netbian.com/meinv/']

    rules = (
        Rule(LinkExtractor(allow='meinv/index_\\d+.htm')),
        Rule(LinkExtractor(allow='desk/\\d+.htm'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = PicturespiderItem()
        # 图片标题
        item['image_title'] = response.xpath("//div[@class='wrap clearfix']/div[@id='main']/div[@class='action']/h1/text()").extract()[0]
        # print(item['image_title'])
        # 图片路径
        item['image_src'] = response.xpath("/html/body/div[@class='wrap clearfix']/div[@id='main']/div[@class='endpage']/div[@class='pic']/p/a/img/@src").extract()[0]
        # print(item['image_src'])

        yield item
