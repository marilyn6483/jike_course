# -*- coding: utf8 -*-
from selenium import webdriver
from scrapy.http import HtmlResponse
import time


class JavaScriptMiddleware(object):
    def process_request(self, request, spider):
        if request.meta.has_key("PhantomJS"):
            print "PhantomJS is starting..."
            driver = webdriver.PhantomJS()
            # driver = webdriver.Firefox()
            driver.get(request.url)
            print 'flag1'
            time.sleep(10)
            for i in range(14):
                js = "var q=document.body.scrollTop=100000"
                driver.execute_script(js)
                time.sleep(3)
                body = driver.page_source
                print "aaaaaaaaaaaaaaaaaaaaa"
                print len(body)
            print ("访问" + request.url)
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return
