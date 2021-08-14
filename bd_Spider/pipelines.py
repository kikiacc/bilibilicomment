# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymysql
class BdSpiderPipeline:
    # def __init__(self):
    #     conn = pymysql.connect(
    #         host='localhost',
    #         port=3306,
    #         user='root',
    #         password='1234',
    #         database='data_analyze',
    #         charset='utf8'
    #     )
    #     cursor = conn.cursor()
    def process_item(self, item, spider):
        # save_list=item["save_list"]
        # with open("bytedance_comment.csv","a",encoding='utf8') as f:
        #     for s in save_list:
        #         f.write(s)
        #         f.write("\n")
        # return item
        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='1234',
            database='data_analyze',
            charset='utf8mb4'
        )
        cursor = conn.cursor()
        save_list=item["save_list"]
        sql="insert into bytedance_bilibili(comment) values(%s);"
        cursor.executemany(sql,save_list)
        conn.commit()
        cursor.close()
        conn.close()
        return item