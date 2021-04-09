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

def get_proxy():
    url = "http://124.16.154.110:8888/monitor-server/gather/getip"
    response = requests.get(url)
    return response.text


def get_results(year,page_num):
    with open('result_nssfc_{year}.txt'.format(year=year), 'w', encoding='utf-8') as f:
        for page in tqdm(range(page_num)):
            url = "http://fz.people.com.cn/skygb/sk/index.php/index/seach/{}?pznum=&xmtype=0&xktype=0&xmname=&lxtime={}&xmleader=&zyzw=0&gzdw=&dwtype=0&szdq=0&ssxt=0&cgname=&cgxs=0&cglevel=0&jxdata=0&jxnum=&cbs=&cbdate=0&zz=&hj=".format(page+1,year)
            
            proxy = {'https': get_proxy()}
            header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
            response=requests.get(url,headers=header,proxies=proxy,timeout=5)

            print(response.status_code)

            if response.status_code == 200:
                html = BeautifulSoup(response.content,"html.parser")

                print(html.pretiffy())
                
                ## 表头
                thead = html.find('div',class_='jCarouselLite').find('thead')
                table_dict = {}
                i = 0
                for th in thead.find_all('th'):
                    label = th.string.strip()
                    table_dict[i] = label
                    i += 1
                # print("table_dict: ",table_dict)


                ## 表格内容
                table = html.find('div',class_='jCarouselLite').find('table')
                result = {}
                tr_list = table.find_all('tr')[1:] # 第一行为表头
                for tr in tr_list:
                    td_list = tr.find_all('td')
                    assert len(td_list) == len(table_dict)
                    for i in range(len(td_list)):
                        result[table_dict[i]] = td_list[i].get_text().strip()
                    f.write(json.dumps(result) + '\n')
            else:
                time.sleep(40)
                exit()



            print(page+1 ," Done.")
            time.sleep(random.randint(10,20))


if __name__ == '__main__':
    get_results(2018,267)
