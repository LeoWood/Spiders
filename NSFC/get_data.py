#-*- coding:utf-8 -*-
# Author: Liu Huan
# Mail: liuhuan@mail.las.ac.cn
# Datetime: 2019/8/4 15:28
import pandas as pd
import requests
import json
import time
import random


if __name__ == '__main__':
    df = pd.read_excel('NSFC_abs_liuhuan.xlsx')
    # print(df.head())
    with open('results_nsfc(40000_60000).txt','w',encoding='utf-8') as f:
        for i in range(40000,60000):
            grantNo = df.iloc[i]['grantNo']
            # grantNo = '11421091'
            # grantNo = '61421091'
            url = 'http://output.nsfc.gov.cn/baseQuery/data/conclusionProjectInfo/' + str(grantNo)
            try:
                data = requests.get(url).text
            except:
                time.sleep(600)
                data = requests.get(url).text
            # print(data)
            try:
                data = json.loads(data)
                data = json.dumps(data,ensure_ascii=False)
                f.write(data + '\n')
                print(data)
            except:
                print('error.')
            time.sleep(random.randint(0,3))
            print(i, 'done')
