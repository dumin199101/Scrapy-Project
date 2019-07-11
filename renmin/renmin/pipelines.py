# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import pymysql


class RenminPipeline(object):
    # 1.数据写入json文件
    # def __init__(self):
    #     # 创建一个只写文件，指定文本编码格式为utf-8
    #     self.filename = codecs.open('renmin.json', 'w', encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #     content = json.dumps(dict(item), ensure_ascii=False) + "\n"
    #     self.filename.write(content)
    #     return item
    #
    # def spider_closed(self, spider):
    #     self.filename.close()

    # 2.数据写入MySQL数据库
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.1.129', user='root', passwd='2e31685493', port=3306, db='maocuhui')

    def process_item(self, item, spider):
        self.cur = self.conn.cursor()
        sql = (
            "INSERT INTO `tb_comp_news`(`v_title`,`v_source`,`v_publish_time`,`v_desc`,`n_nav_id`,`v_editor`,`v_link`)"
            "VALUES (%s,%s,%s,%s,%s,%s,%s)")
        lis = (item['title'], item['source'], item['pubdate'], item['content'], '20', item['editor'], item['link'])
        self.cur.execute(sql, lis)
        self.conn.commit()
        return item

    def spider_closed(self, spider):
        self.cur.close()
        self.conn.close()
