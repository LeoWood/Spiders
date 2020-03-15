#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/3/15 10:29

# from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup
import requests

# def get_driver():
#     chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
#     driver = webdriver.Chrome(chromedriver)
#     return driver

def get_headers():
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    cookie = 'Ecp_ClientId=5191212001400024765; cnkiUserKey=1f7be8d1-6d5c-7b85-3fc2-de96209a75f8; Hm_lvt_6e967eb120601ea41b9d312166416aa6=1576207299,1576494876,1576588643,1578109217; Ecp_IpLoginFail=200315171.82.3.62; ASP.NET_SessionId=ppi22pdmlglipzchirjzdl2f; SID_kns=123107; SID_klogin=125144; SID_kns_new=123106; KNS_SortType=; SID_krsnew=125132; _pk_ref=%5B%22%22%2C%22%22%2C1584238738%2C%22https%3A%2F%2Fwww.cnki.net%2F%22%5D; _pk_ses=*; SID_kxreader_new=011121; RsPerPage=50'
    cookie = 'Ecp_notFirstLogin=KZoIB5; Ecp_ClientId=5191221001100019718; cnkiUserKey=9a57594c-e8fb-0c51-f2ed-c5384bf30588; UM_distinctid=170a0bc60e6186-0aa93a98db970a-b383f66-140000-170a0bc60e746; Ecp_session=1; ASP.NET_SessionId=aaaoowmikwohbjc25estgy2b; SID_kns=123108; SID_klogin=125141; KNS_SortType=; SID_kxreader_new=011123; SID_kns_kdoc=025011122; SID_kns_new=123123; Hm_lvt_6e967eb120601ea41b9d312166416aa6=1584154949; SID_krsnew=125132; RsPerPage=50; Hm_lpvt_6e967eb120601ea41b9d312166416aa6=1584242149; LID=WEEvREdxOWJmbC9oM1NjYkZCcDMwV0lMQjNDWS82WEVmWStrUUJmdVJuakQ=$R1yZ0H6jyaa0en3RxVUd8df-oHi7XMMDo7mtKT6mSmEvTuk11l2gFA!!; _pk_ref=%5B%22%22%2C%22%22%2C1584246084%2C%22https%3A%2F%2Fwww.cnki.net%2F%22%5D; _pk_ses=*; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"zky311001","ShowName":"%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E9%99%A2%E6%96%87%E7%8C%AE%E6%83%85%E6%8A%A5%E4%B8%AD%E5%BF%83","UserType":"bk","BUserName":"","BShowName":"","BUserType":"","r":"KZoIB5"}; c_m_LinID=LinID=WEEvREdxOWJmbC9oM1NjYkZCcDMwV0lMQjNDWS82WEVmWStrUUJmdVJuakQ=$R1yZ0H6jyaa0en3RxVUd8df-oHi7XMMDo7mtKT6mSmEvTuk11l2gFA!!&ot=03/15/2020 12:42:11; c_m_expire=2020-03-15 12:42:11'
    headers = {'User-Agent': User_Agent, 'cookie': cookie}
    return headers

def get_html(home_url):
    # response = requests.get('https://kns.cnki.net/kns/brief/brief.aspx?curpage=1&RecordsPerPage=50&QueryID=3&ID=&turnpage=1&tpagemode=L&dbPrefix=SCDB&Fields=&DisplayMode=listmode&SortType=(%E5%8F%91%E8%A1%A8%E6%97%B6%E9%97%B4%2c%27TIME%27)+desc&PageName=ASP.brief_result_aspx&isinEn=1&',headers=get_headers())
    #
    # soup = BeautifulSoup(response.content,"html.parser")
    # with open('html.html','w',encoding='utf-8') as f:
    #     f.write(soup.prettify())
    # print(soup.prettify())
    # exit()

    with open('html.html','r',encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(),"html.parser")
    # print(soup.prettify())
    html_links = soup.find_all('a',title="HTML阅读")
    # print(html_links)
    for link in html_links:
        print(link['href'])
    # exit()

def get_urls():
    with open('urls.txt','a',encoding='utf-8') as f:
        for page_id in range(1,10000):
            url = 'https://kns.cnki.net/kns/brief/brief.aspx?curpage={page_id}&RecordsPerPage=50&QueryID=3&ID=&turnpage=1&tpagemode=L&dbPrefix=SCDB&Fields=&DisplayMode=listmode&SortType=(%E5%8F%91%E8%A1%A8%E6%97%B6%E9%97%B4%2c%27TIME%27)+desc&PageName=ASP.brief_result_aspx&isinEn=1&'.format(page_id=page_id)
            response = requests.get(url, headers=get_headers())
            soup = BeautifulSoup(response.content, "html.parser")
            html_links = soup.find_all('a', title="HTML阅读")
            for link in html_links:
                f.write('https://kns.cnki.net' + link['href'] + '\n')
            time.sleep(random.randint(5,15))
            print(page_id, ' Done')


if __name__ == '__main__':
    # home_url = "https://kns.cnki.net/kns/brief/result.aspx?dbprefix=SCDB&crossDbcodes=CJFQ,CDFD,CMFD,CPFD,IPFD,CCND,CCJD"
    # get_html(home_url)
    get_urls()