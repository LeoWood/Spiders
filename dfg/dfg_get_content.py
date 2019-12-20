#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2019/11/26 15:54

import requests
from bs4 import BeautifulSoup
import time
import random
from tqdm import tqdm
import json
import os

def save_source(year):
    source_dir = 'source_{year}'.format(year=year)
    if not os.path.exists(source_dir):
        os.mkdir(source_dir)
    with open('urls_{year}.txt'.format(year=year), 'r', encoding='utf-8') as f:
        for line in tqdm(f.readlines()):
            url = line.strip() + '?language=en'
            id = line.strip().split('/')[-1]
            html = BeautifulSoup(requests.get(url).content, "html.parser")
            with open(source_dir + '/' + id + '.txt', 'w', encoding='utf-8') as fw:
                fw.write(str(html.prettify()))
            # exit()
            time.sleep(random.randint(0, 3))

def get_content(year):
    source_dir = 'source_{year}'.format(year=year)
    if not os.path.exists(source_dir):
        os.mkdir(source_dir)
    with open('results_{year}.txt'.format(year=year), 'w', encoding='utf-8') as fw:
        with open('urls_{year}.txt'.format(year=year), 'r', encoding='utf-8') as f:
            for line in tqdm(f.readlines()):
                data = {}
                url = line.strip() + '?language=en'
                # url = 'https://gepris.dfg.de/gepris/projekt/354841670?language=en'
                data['url'] = url
                html = BeautifulSoup(requests.get(url).content, "html.parser")

                id = line.strip().split('/')[-1]
                ## save source
                with open(source_dir + '/' + id + '.txt', 'w', encoding='utf-8') as fs:
                    fs.write(str(html.prettify()))

                detail = html.find('div',class_="details")
                data['title'] = detail.find('h3').get_text().strip()
                # data[]
                for table in detail.find_all('div'):
                    if table.find('span'):
                        spans = table.find_all('span')
                        k = spans[0].get_text().strip()
                        v = [s for s in spans[1].stripped_strings]
                        if len(v) == 1:
                            v = v[0]
                        # if '\n' in v:
                        #     v = [s for s in spans[1].stripped_strings]
                        data[k] = v
                        # print(k)
                data['Project Description'] = html.find('div',id='projekttext').get_text().strip()
                for table in html.find('div',id = 'projektbeschreibung').find_all('div'):
                    if table.find('span'):
                        spans = table.find_all('span')
                        k = spans[0].get_text().strip()
                        v = [s for s in spans[1].stripped_strings]
                        if len(v) == 1:
                            v = v[0]
                        # if '\n' in v:
                        #     v = [s for s in spans[1].stripped_strings]
                        data[k] = v
                fw.write(json.dumps(data) + '\n')
                # print(data)
                # exit()
                time.sleep(random.randint(0,3))

if __name__ == '__main__':
    for year in range(2012,2013):
        get_content(year)
    # exit()



