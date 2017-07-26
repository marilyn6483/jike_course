# -*- coding: utf8 -*-
import json
import scrapy
import re
import uuid
from bs4 import BeautifulSoup


class Meituanspider(scrapy.Spider):
    name = "meituan"
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
    }

    def start_requests(self):
        self.avg_price = dict()
        urls = self.get_pages()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;htq=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "nj.meituan.com",
            "Upgrade-Insecure-Requests": 1,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36 QQBrowser/4.1.4132.400"
        }
        for url in urls:
            req = scrapy.Request(url=url, callback=self.parse, method="GET", headers=headers)
            req.meta['PhantomJS'] = True
            yield req

    def parse(self, response):
        print "scraping"
        print response.url
        html = response.body
        html = re.sub("&lt;", "<", html)
        html = re.sub("&gt;", ">", html)
        soup = BeautifulSoup(html, 'lxml')
        all_a = soup.find_all(name="a", attrs={"class": "poi-tile__head J-mtad-link"})
        for a in all_a:
            shop_url = a['href']
            p = a.findNext(name='span', attrs={"class": "price"}).text
            p = re.sub("^.", "", p)
            shop_id = uuid.uuid4()
            self.avg_price[shop_id] = p
            req = scrapy.Request(url=shop_url, callback=self.parse_shop)
            req.meta['uid'] = shop_id
            yield req  # 商家网址

    def parse_shop(self, response):
        print "scraping"
        print response.url
        dic = dict()
        html = response.body
        html = re.sub("&lt;", "<", html)
        html = re.sub("&gt;", ">", html)
        soup = BeautifulSoup(html, 'lxml')
        dic["name"] = soup.find(name="span", attrs={"class": "title"}).text
        dic["addr"] = soup.find(name="span", attrs={"class": "geo"}).text
        dic['phone'] = soup.find_all(name="p", attrs={"class": "under-title"})[1].text
        dic['score'] = soup.find(name="span", attrs={"class": "biz-level"}).find(name="strong").text
        dic['cat'] = soup.find(name="a", attrs={"class": "tag"}).text
        dic['commit'] = soup.find(name="a", attrs={"class": "num rate-count"}).text
        dic['price'] = self.avg_price[response.meta['uid']]
        print dic
        with open('/Users/xuting/test/chenyanyan/tutorial/tutorial/out/info.txt', 'ab') as a:
            json.dump(dic, a, indent=4)

    def get_pages(self):
        urls = []
        for i in range(1, 10):
            url = "http://nj.meituan.com/category/meishi/all/page{}".format(i)
            print url
            urls.append(url)
        return urls
