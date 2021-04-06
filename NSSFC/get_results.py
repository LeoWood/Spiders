#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Time    :   2021/04/06 16:25:40
@Author  :   Leo Wood 
@Contact :   leowood@foxmail.com
'''

import requests
from bs4 import BeautifulSoup
import time
import random
from tqdm import tqdm
import json


def get_results(year,page_num):
    with open('result_nssfc_{year}.txt'.format(year=year), 'w', encoding='utf-8') as f:
        for page in tqdm(range(page_num)):
            url = "http://fz.people.com.cn/skygb/sk/index.php/index/seach/{}?pznum=&xmtype=0&xktype=0&xmname=&lxtime=2019&xmleader=&zyzw=0&gzdw=&dwtype=0&szdq=0&ssxt=0&cgname=&cgxs=0&cglevel=0&jxdata=0&jxnum=&cbs=&cbdate=0&zz=&hj=".format(page+1)

            html = BeautifulSoup(requests.get(url).content,"html.parser")
            
            ## 表头
            thead = html.find('div',class_='jc_a').find('thead')
            table_dict = {}
            i = 0
            for th in thead.find_all('th'):
                label = th.string.strip()
                table_dict[i] = label
                i += 1
            print("table_dict: ",table_dict)


            ## 表格内容
            table = html.find('div',class_='jc_a').find('table')
            result = {}
            tr_list = table.find_all('tr')[1:] # 第一行为表头
            for tr in tr_list:
                td_list = tr.find_all('td')
                assert len(td_list) == len(table_dict)
                for i in range(len(td_list)):
                    result[table_dict[i]] = td_list[i].get_text().strip()

            f.write(json.dumps(result) + '\n')

        print(page+1 ," Done.")
        time.sleep(random.randint(2,8))


if __name__ == '__main__':
    get_results(2019,277)
