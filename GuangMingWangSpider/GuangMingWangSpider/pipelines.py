# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class GuangmingwangspiderPipeline(object):
    # 数据写入MySQL数据库
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.1.129', user='root', passwd='2e31685493', port=3306,
                                    db='maocuhui')

    def process_item(self, item, spider):
        print(item['title'])
        self.cur = self.conn.cursor()
        # 1.党建要闻
        sql = (
            "INSERT INTO `tb_comp_news`(`v_title`,`v_source`,`v_publish_time`,`v_desc`,`n_nav_id`,`v_editor`,`v_link`)"
            "VALUES (%s,%s,%s,%s,%s,%s,%s)")
        lis = (item['title'], item['source'], item['pubdate'], item['content'], '19', item['editor'], item['link'])
        self.cur.execute(sql, lis)
        self.conn.commit()
        return item

    def spider_closed(self, spider):
        self.cur.close()
        self.conn.close()
