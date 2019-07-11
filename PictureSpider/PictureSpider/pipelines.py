# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import os
import random

class PicturespiderPipeline(ImagesPipeline):

    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        image_src = item['image_src']
        yield Request(image_src)


    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok,x in results if ok]
        os.rename(self.IMAGES_STORE+"\\"+image_path[0],self.IMAGES_STORE+"\\"+item['image_title'] + "_" + str(random.randint(100000,999999))+".jpg")
        item['image_path'] = self.IMAGES_STORE + "\\" + item['image_title']
        return item

