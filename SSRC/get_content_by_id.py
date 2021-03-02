# -*- coding:utf-8 -*-
# Author: Liu Huan
# Mail: liuhuan@mail.las.ac.cn
# Datetime: 2019/3/12 18:02

from bs4 import BeautifulSoup
import os
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
import requests
import time
import random
import json


# def init_driver():
#     iedriver = "IEDriverServer.exe"
#     os.environ["webdriver.ie.driver"] = iedriver
#     driver = webdriver.Ie(iedriver)
#     return driver

def get_soup(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    return soup


def get_content(soup):
    data = {}
    trs1 = soup.find_all('tr',class_='TitreColonne')
    trs2 = soup.find_all('tr',class_='Impair')
    trs3 = soup.find_all('tr',class_='Pair')
    for tr in trs1 + trs2 + trs3:
        key = tr.find_all('td')[0].get_text()
        value = tr.find_all('td')[1].get_text()
        data[key] = value
    return data


if __name__ == "__main__":
    with open('results(1-1w).txt','a',encoding='utf-8') as fw:
        for i in range(1,100000):
            url = 'http://www.outil.ost.uqam.ca/CRSH/Detail.aspx?Cle=' + str(i) + '&Langue=2'
            id_ = ''
            for c in url:
                if c >= '\u0030' and c <= '\u0039':
                    id_ += c
            id_ = id_[:-1]
            try:
                soup = get_soup(url)
            except:
                print('Requests Error ~~~')
                time.sleep(600)
                soup = get_soup(url)
            data = get_content(soup)
            if 'Fiscal Year' not in data:
                print(id_,' Not Found~~~')
                # print(url)
                time.sleep(random.randint(1,3))
                i += 1
                print(i, 'Done')
                continue
            data['id'] = id_
            data['url'] = url
            # print(id_)
            # print(data)
            data = json.dumps(data)
            fw.write(data + '\n')
            with open('html\\' + id_ + '_html.txt','w',encoding='utf-8') as f:
                f.write(soup.prettify())
            time.sleep(random.randint(1,3))
            i += 1
            print(i, ' Done')
