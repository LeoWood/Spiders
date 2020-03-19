#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/3/17 17:15

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random
import requests

def get_driver():
    chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver)
    return driver

def get_soup_from_url(url):
    driver = get_driver()
    # driver.get('https://www.cnki.net/')
    driver.get(url)
    time.sleep(300)
    soup = BeautifulSoup(driver.page_source,"html.parser")

    response = requests.get(url,headers=get_headers())
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup.prettify())
    return soup

def get_headers():
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    cookie = 'Ecp_notFirstLogin=AzXq62; Ecp_ClientId=4181222183002402076; RsPerPage=20; cnkiUserKey=0113e248-5877-5e3a-44ed-4454172a87f7; _pk_ref=%5B%22%22%2C%22%22%2C1581927027%2C%22https%3A%2F%2Fwww.cnki.net%2F%22%5D; LID=WEEvREcwSlJHSldRa1FhdXNzY2Z1UmVhR2xtaVVvUWNRNDBZd0tzZldQND0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; Ecp_session=1; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"zky342001","ShowName":"%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E9%99%A2%E6%AD%A6%E6%B1%89%E6%96%87%E7%8C%AE%E6%83%85%E6%8A%A5%E4%B8%AD%E5%BF%83","UserType":"bk","BUserName":"","BShowName":"","BUserType":"","r":"AzXq62"}; ASP.NET_SessionId=nz2yddyqs5whc1metnhors4b; SID_kns=123112; SID_kxreader_new=011122; SID_kns_kdoc=015011121; Hm_lvt_6e967eb120601ea41b9d312166416aa6=1584439716; SID_klogin=125142; c_m_LinID=LinID=WEEvREcwSlJHSldRa1FhdXNzY2Z1UmVhR2xtaVVvUWNRNDBZd0tzZldQND0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=03/17/2020 18:32:21; c_m_expire=2020-03-17 18:32:21; Hm_lpvt_6e967eb120601ea41b9d312166416aa6=1584439941'
    headers = {'User-Agent': User_Agent, 'cookie': cookie}
    return headers


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

    with open('urls_1_60.txt','r',encoding='utf-8') as f:
        i = 0
        for line in f.readlines():
            i += 1
            url = line.strip()
            soup = get_soup_from_url(url)
            content = get_content(soup)
            with open(str(i) + '.txt','w',encoding='utf-8') as fw:
                [fw.write(con) for con in content]
            print(i, 'Done')
            time.sleep(random.randint(30,90))