# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Item
from scrapy import Field


class PicturespiderItem(Item):
    # define the fields for your item here like:
    # 图片标题
    image_title = Field()
    # 图片路径
    image_src = Field()
    # 图片存储位置
    image_path = Field()

