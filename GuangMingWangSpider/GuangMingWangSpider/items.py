# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item
from scrapy import Field


class GuangmingwangspiderItem(Item):
    # 新闻标题
    title = Field()
    # 新闻发布时间
    pubdate = Field()
    # 新闻来源
    source = Field()
    # 新闻链接
    link = Field()
    # 新闻编辑
    editor = Field()
    # 新闻内容
    content = Field()



