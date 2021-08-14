# -*- coding: utf-8 -*-
import json
import random
import time

import scrapy
# import requests
from scrapy.spiders import Spider
from .. import *
from ..items import BdSpiderItem
class BdSpider(scrapy.Spider):
    name = 'bd'
    key_word="华为"
    allowed_domains = ['bilibili.com']
    start_urls = ['https://search.bilibili.com/all?keyword={}'.format(key_word)]
    def get_ua(self):
        with open("useragents.data", 'r') as f:
            ua = random.choice(f.readlines())
            ua = ua.strip('\n')
            headers = {
                'User-Agent':ua,
            }
        return headers

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0],callback=self.getMax,headers=self.get_ua())
        # yield  scrapy.Request("https://www.bilibili.com/video/BV1Lz4y1D7mf?from=search&seid=1727607307434091561",
        #                       callback=self.parse_video,headers=self.get_ua(), meta={"middleware": "keyi"})


    def getMax(self,response):#获取所有页
        max_page=(int)(response.xpath("//li[@class='page-item last']/button/text()").get())
        print(type(max_page))
        for i in range(1,max_page-1):
            page_url="https://search.bilibili.com/all?keyword={}&page={}".format(self.key_word,i)
            print(page_url)
            yield scrapy.Request(page_url,callback=self.parse_page,headers=self.get_ua())

    def parse_page(self, response):#获取每页的所有视频链接
        all_video_url=response.xpath("//li[@class='video-item matrix']/a/@href").getall()
        for url in all_video_url:
            nurl="https:"+url
            print(nurl)
            print("===============================================")
            yield scrapy.Request(url=nurl, callback=self.parse_video, meta={"middleware": "keyi"},headers=self.get_ua())


    def parse_video(self,response):
        tit=response.xpath(r"//span[@class='tit']/text()").get()
        print(tit)
        response.text.replace("<br>","")
        comment_list=response.xpath(r"//div[@class='con ']/p").xpath('string(.)').extract()
        save_list=BdSpiderItem(save_list=comment_list)
        return save_list

