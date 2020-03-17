#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/3/17 17:15

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random

def get_driver():
    chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver)
    return driver

def get_soup_from_url(url):
    driver = get_driver()
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source,"html.parser")
    return soup


def get_soup_from_file(path):
    with open(path,'r',encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(),"html.parser")
        # print(soup.prettify())
    return soup

def get_content(soup):
    content = []
    paras = soup.find_all('div',class_="p1")
    for pa in paras:
        [s.extract() for s in pa('citation')]
        print(pa.get_text())
        content.append(pa.get_text())
    return content

if __name__ == '__main__':
    # get_content(get_soup_from_file('cnki_full.html'))

    with open('urls.txt','r',encoding='utf-8') as f:
        i = 0
        for line in f.readlines():
            i += 1
            url = line.strip()
            soup = get_soup_from_url(url)
            content = get_content(soup)
            with open(str(i) + '.txt','w',encoding='utf-8') as fw:
                [fw.write(con + '\n') for con in content]
            print(i, 'Done')
            time.sleep(random.randint(30,90))