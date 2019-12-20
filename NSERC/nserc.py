#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-30 14:24:41
# @Author  : Leo Wood (leowood@foxmail.com)
import requests
from bs4 import BeautifulSoup
import random
import time
import os
from selenium import webdriver
import json

# with open('urls(80001-179600).txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
# i = 22188

# User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# cookie = 'ASPSESSIONIDCQSCRQBT=LEPHDIBABMLJMDGDHIGEEGPD; __utmt=1; nojs=False; __utma=268634606.1530201212.1504870893.1506827013.1506846124.19; __utmb=268634606.3.9.1506846129977; __utmc=268634606; __utmz=268634606.1504870893.1.1.utmcsr=mail.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _we_wk_ss_lsf_=true; ASESearchId=721367D2%2DB756%2D4928%2DA527%2DB61819E9CFDA; ASEId=%7B154EDC37%2D7FB2%2D4D47%2D835B%2D1C0C21F0E911%7D'
# headers = {'User-Agent': User_Agent, 'cookie': cookie}

chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Ie(chromedriver)

with open('result.txt', 'a', encoding='utf-8') as f:
    for i in range(643276, 643276 + 26753):
        data = {}
        url = 'http://www.nserc-crsng.gc.ca/ase-oro/Details-Detailles_eng.asp?id=' + str(i)
        # 获取具体页面
        driver.get(url)
        # html = requests.get(url, headers=headers)
        # soup = BeautifulSoup(html.content, "html.parser")
        soup = BeautifulSoup(driver.page_source, "html.parser")

        data['title'] = soup.find('div',id='main-container-1col').find('h2').string
        # 解析表格
        tds = soup.find_all('td')
        for j in [2, 4, 6, 8, 10, 12, 14,
                 16, 18, 20, 22, 24, 26, 28]:
            key = tds[j-2].text.strip()[:-1]
            value = tds[j-1].text.strip()
            data[key] = value
        data['Award Summary'] = soup.find('div', id= 'RightColDetails').find('p').string
        data = json.dumps(data)
        f.write(data + '\n')
        print(i, ' done.')
        #exit()
        s = random.randint(1, 5)
        time.sleep(s)
