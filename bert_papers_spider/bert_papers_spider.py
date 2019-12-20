#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2019/12/19 15:37

import requests
from bs4 import BeautifulSoup
import os
import time
import random

if __name__ == '__main__':
    with open('source_code.html','r',encoding='utf-8') as f:
        html = BeautifulSoup(f,"html.parser")
        # print(html.find('div',class_="Box-body"))
        body = html.find('div',class_="Box-body")
        h2 = body.find('h2')
        dir_name_1 = h2.get_text().strip()
        if not os.path.exists(dir_name_1):
            os.mkdir(dir_name_1)

        for ne in h2.next_siblings:
            if ne.name == 'h3' or ne.name == 'h2':
                dir_name_2 = ne.get_text().strip()
                if not os.path.exists(dir_name_1 + '/' + dir_name_2):
                    os.mkdir(dir_name_1 + '/' + dir_name_2)
            if ne.name == 'ul':
                for li in ne.find_all('li'):
                    a = li.find('a')
                    url = a['href'].replace('abs', 'pdf') + '.pdf'
                    f_name = li.get_text().strip().replace('\n','').replace('\r','').replace(':','--').replace('"', '').replace('?',' ').replace("'","") + '.pdf'

                    if not os.path.exists(dir_name_1 + '/' + dir_name_2 + '/' + f_name):
                        r = requests.get(url)
                        try:
                            with open(dir_name_1 + '/' + dir_name_2 + '/' + f_name, 'wb') as pdf:
                                pdf.write(r.content)
                        except:
                            print('error-------------------------------------------')
                            print(f_name)
                            print()

                        time.sleep(random.randint(1,5))
                    print(f_name, 'Done')
