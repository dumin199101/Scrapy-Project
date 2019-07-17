# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class MaocuhuispiderPipeline(object):
        # 数据写入MySQL数据库
        def __init__(self):
            self.conn = pymysql.connect(host='192.168.1.129', user='root', passwd='2e31685493', port=3306,
                                        db='maocuhui')

        def process_item(self, item, spider):
            self.cur = self.conn.cursor()
            sql = (
                "INSERT INTO `tb_building_notice`(`v_title`,`v_source`,`v_publish_time`,`v_desc`,`v_intro`,`v_link`)"
                "VALUES (%s,%s,%s,%s,%s,%s)")
            lis = (item['title'], item['source'], item['pubdate'], item['content'], item['desc'], item['link'])
            self.cur.execute(sql, lis)
            self.conn.commit()
            return item

        def spider_closed(self, spider):
            self.cur.close()
            self.conn.close()
