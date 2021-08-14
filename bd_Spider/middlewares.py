# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver import ActionChains


class all_comment(object):
    def __init__(self):
        # options=webdriver.ChromeOptions()
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # options.add_experimental_option("prefs", prefs)
        # self.drive = webdriver.Chrome(
        #     executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",options=options)
        self.drive=webdriver.Edge(executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
    def process_request(self, request, spider):
        if request.meta.get("middleware")=="keyi":
            self.drive.get(request.url)
            time.sleep(3)
            self.drive.execute_script("window.scrollBy(0, 1440)")
            time.sleep(1)
            self.drive.execute_script("window.scrollBy(0, 1440)")
            time.sleep(1)
            try:
                page_num=(int)((self.drive.find_element_by_xpath(r'//div[@class="page-jump"]/span')).text)
                all_source = self.drive.page_source
                for i in range(page_num-1):
                    next_page=self.drive.find_element_by_xpath(r"//div[@id='comment']//a[@class='next']")
                    ActionChains(self.drive).click(next_page).perform()
                    time.sleep(1)
                    all_source = self.drive.page_source+all_source
                response = HtmlResponse(url=self.drive.current_url, body=all_source, request=request, encoding='utf-8')
            except:
                all_source = self.drive.page_source
                response = HtmlResponse(url=self.drive.current_url, body=all_source, request=request, encoding='utf-8')
            return response
            # for i in range(page_num):
            #     if i==0:
            #         all_source = self.drive.page_source
            #         response = HtmlResponse(url=self.drive.current_url, body=all_source, request=request,
            #                                 encoding='utf-8')
            #         return response
            #
            #     next_page=self.drive.find_element_by_xpath(r"//*[@id='comment']/div/div[2]/div/div[4]/a[2]")
            #     ActionChains(self.drive).click(next_page).perform()
            #     all_source = self.drive.page_source
            #     response = HtmlResponse(url=self.drive.current_url, body=all_source, request=request, encoding='utf-8')
            #     return response

class BdSpiderSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BdSpiderDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
