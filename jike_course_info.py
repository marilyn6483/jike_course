# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as BS4
import time
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

course_info = {}

def scrapy_course():
    '''
    start to scrab course info
    '''
    for i in range(1, 21):#爬取1到20页的课程信息
        base_url = "http://www.jikexueyuan.com/course/?pageNum={}".format(i)
        print base_url
        response = requests.get(base_url)
        bsobj = BS4(response.text, "lxml")
        course_id = bsobj.find_all("li")
            
        for iterm in course_id:             
            try:
                a = iterm.find_all("a")
                for course in a:
                    course_info[course.text] = course.get("href")
            except Exception as e:
                print e
                continue
                    
if __name__ == "__main__":
    starttime = time.time()
    scrapy_course()
    endtime = time.time()
    totle_time = endtime - starttime
    print totle_time
    print "finished!"
    with open("jike_course.txt", "w+") as jike:
        for items in course_info:
            jike.write(items + ":" + course_info[items])
            jike.write("\n")