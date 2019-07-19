# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import GuangmingwangspiderItem


class GuangmingSpider(CrawlSpider):
    name = 'guangming'
    allowed_domains = ['gmw.cn']
    # 1.党建要闻
    # start_urls = ['http://dangjian.gmw.cn/node_11941.htm']
    # 2.新思想
    start_urls = ['http://dangjian.gmw.cn/node_11929.htm']

    rules = (
        # 分页
        Rule(LinkExtractor(allow='node_\\d+_\\d+.htm')),
        # 详情
        Rule(LinkExtractor(allow='content_\\d+.htm',restrict_xpaths="//ul[@class='channel-newsGroup']/li/span[@class='channel-newsTitle']/a"), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = GuangmingwangspiderItem()
        # print(response.body.decode("utf-8"))
        # 标题
        if len(response.xpath("//h1[@class='u-title']")) > 0:
            title = response.xpath("//h1[@class='u-title']/text()").extract()[0]
        elif len(response.xpath("//h1[@id='articleTitle']")) > 0:
            title = response.xpath("//h1[@id='articleTitle']/text()").extract()[0]

        item['title'] = title.strip()

        # 发布日期
        if len(response.xpath("//div[@class='m_tips']/span[@class='m-con-time']")) > 0:
            item['pubdate'] = response.xpath("//div[@class='m_tips']/span[@class='m-con-time']/text()").extract()[0]
        elif len(response.xpath("//div[@id='contentMsg']/span[@id='pubTime']")) > 0:
            item['pubdate'] = response.xpath("//div[@id='contentMsg']/span[@id='pubTime']/text()").extract()[0]
        elif len(response.xpath("//div[@class='m-con-info']/span[@class='m-con-time']")) > 0:
            item['pubdate'] = response.xpath("//div[@class='m-con-info']/span[@class='m-con-time']/text()").extract()[0]

        # 来源
        if len(response.xpath("//div[@class='m_tips']/span[@class='m-con-source']/a")) > 0:
            item['source'] = response.xpath("//div[@class='m_tips']/span[@class='m-con-source']/a/text()").extract()[0]
        elif len(response.xpath("//div[@id='contentMsg']/span[@id='source']/a")) > 0:
            item['source'] = response.xpath("//div[@id='contentMsg']/span[@id='source']/a/text()").extract()[0]
        elif len(response.xpath("//div[@class='m-con-info']/span[@class='m-con-source']/a")) > 0:
            item['source'] = response.xpath("//div[@class='m-con-info']/span[@class='m-con-source']/a/text()").extract()[0]

        # 链接
        item['link']= response.url

        # 编者
        if len(response.xpath("//div[@class='m-zbTool liability']/span[@class='liability']")) > 0:
            editor = response.xpath("//div[@class='m-zbTool liability']/span[@class='liability']/text()").extract()[0]
            item['editor'] = editor[editor.find("：")+1:]
        elif len(response.xpath("//div[@class='u-mainText']/div[@class='m-zbTool']/span[@class='liability']")) > 0:
            editor = response.xpath("//div[@class='u-mainText']/div[@class='m-zbTool']/span[@class='liability']/text()").extract()[0]
            item['editor'] = editor[editor.find("：")+1:]
        elif len(response.xpath("//div[@id='contentMain']/div[@id='contentLiability']")) > 0:
            editor = response.xpath("//div[@id='contentMain']/div[@id='contentLiability']/text()").extract()[0]
            item['editor'] = editor[editor.find(":")+1:-1]
        elif len(response.xpath("//div[@class='u-mainText']/p/span[@class='liability']")) > 0:
            editor = response.xpath("//div[@class='u-mainText']/p/span[@class='liability']/text()").extract()[0]
            item['editor'] = editor[editor.find("：")+1:-1]


        # 内容
        if len(response.xpath("//div[@id='article_inbox']/div[@class='u-mainText']")) > 0:
            item['content'] = response.xpath("//div[@id='article_inbox']/div[@class='u-mainText']").extract()[0]
        elif len(response.xpath("//div[@class='contentLeft']/div[@id='contentMain']")) > 0:
            item['content'] = response.xpath("//div[@class='contentLeft']/div[@id='contentMain']").extract()[0]

        yield item
