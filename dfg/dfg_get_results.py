#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2019/11/26 14:39

import requests
from bs4 import BeautifulSoup
import time
import random
from tqdm import tqdm

# class pySpider:
#
#     def __init__(self):
#         self.url = url

def get_results(year,page_num):
    with open('urls_{year}.txt'.format(year=year), 'w', encoding='utf-8') as f:
        for page in tqdm(range(page_num)):
            index = page*50
            url = "https://gepris.dfg.de/gepris/OCTOPUS?beginOfFunding={year}&bewilligungsStatus=&context=projekt&continentId=%23&countryKey=%23%23%23&einrichtungsart=-1&fachlicheZuordnung=%23&findButton=historyCall&gefoerdertIn=&hitsPerPage=50&index={index}&keywords_criterion=&location=&nurProjekteMitAB=false&oldContinentId=%23&oldCountryId=%23%23%23&oldSubContinentId=%23%23&pemu=%23&person=&subContinentId=%23%23&task=doSearchExtended&teilprojekte=true&zk_transferprojekt=false".format(year=year,index=index)
            # print(url)
            # exit()
            html = BeautifulSoup(requests.get(url).content,"html.parser")
            result_lists = []
            for result in html.find_all('div',class_="results"):
                f.write('https://gepris.dfg.de' + result.find('a')['href'] + '\n')
        print(page," Done.")
        time.sleep(random.randint(0,3))


if __name__ == '__main__':
    # year = 2011
    # page_num = 103
    get_results(2011,103)
    get_results(2012,96)
    get_results(2013,90)
    get_results(2014,97)
    get_results(2015,100)

    # 2011 103
    # 2015 100
    # 2017 106
    # 2018 112
    # 2019 90


