#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/3/15 10:29

from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup
import requests

def get_driver():
    chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver)
    return driver

def get_driver_ph():
    driver = webdriver.PhantomJS(executable_path=r"F:\LiuHuan\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    return driver


def get_headers():
    driver = get_driver()
    driver.get(
        'https://kns.cnki.net/kns/brief/result.aspx?dbprefix=SCDB&crossDbcodes=CJFQ,CDFD,CMFD,CPFD,IPFD,CCND,CCJD')
    time.sleep(5)
    driver.find_element_by_id('E').click()
    time.sleep(5)
    cookies = driver.get_cookies()
    # print(cookies)
    cookie = [item["name"] + "=" + item["value"] for item in cookies]
    cookie_str = ';'.join(item for item in cookie)
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    cookie = cookie_str
    headers = {'User-Agent': User_Agent, 'cookie': cookie}
    return headers



def get_urls():
    with open('urls_101.txt','a',encoding='utf-8') as f:
        # headers = get_headers()
        # print(headers)
        for page_id in range(121,151):
            if page_id % 10 == 1:
                print('time to refresh..')
                # time.sleep(30)
                headers = get_headers()
                time.sleep(300)
            url = 'https://kns.cnki.net/kns/brief/brief.aspx?curpage={page_id}&RecordsPerPage=50&QueryID=3&ID=&turnpage=1&tpagemode=L&dbPrefix=SCDB&Fields=&DisplayMode=listmode&SortType=(%E5%8F%91%E8%A1%A8%E6%97%B6%E9%97%B4%2c%27TIME%27)+desc&PageName=ASP.brief_result_aspx&isinEn=1&'.format(page_id=page_id)
            response = requests.get(url, headers=headers)
            if '服务器上不存在此用户' in response.text:
                print('cookie失效，刷新cookie...')
                time.sleep(30)
                headers = get_headers()
                response = requests.get(url,headers=headers)
            if '请输入验证码' in response.text:
                print('需要输入验证码，延时刷新')
                time.sleep(300)
                headers = get_headers()
                response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, "html.parser")
            # print(soup.prettify())
            html_links = soup.find_all('a', title="HTML阅读")
            print(html_links)
            for link in html_links:
                f.write('https://kns.cnki.net' + link['href'] + '\n')
            print(page_id, ' Done')
            secs = random.randint(30,90)
            print(secs, 'later...')
            time.sleep(secs)


if __name__ == '__main__':
    # driver = get_driver_ph()
    # driver.get("http://www.baidu.com")
    # data = driver.title
    # print(data)
    # exit()
    # home_url = "https://kns.cnki.net/kns/brief/result.aspx?dbprefix=SCDB&crossDbcodes=CJFQ,CDFD,CMFD,CPFD,IPFD,CCND,CCJD"
    # get_html(home_url)
    get_urls()