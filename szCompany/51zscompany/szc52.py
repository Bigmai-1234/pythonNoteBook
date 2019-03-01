# -*- coding: utf-8 -*- 
# @Time    : 19-2-25 下午2:52 
# @Author  : jayden.zheng 
# @FileName: szc51.py 
# @Software: PyCharm 
# @content :

# -*- coding: utf-8 -*-
# @Time    : 19-2-25 上午9:21
# @Author  : jayden.zheng
# @FileName: szcompanySpider.py
# @Software: PyCharm
# @content :

from lxml import etree
import requests
import time
import urllib3
import warnings
import random
import pandas as pd
warnings.simplefilter(action='ignore', category=FutureWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from fake_useragent import UserAgent
ua = UserAgent(verify_ssl=False)

#互联网
#mainUrl = 'http://www.job5156.com/qiye/shenzhen-1/pn'
#媒体传播 41页
mainUrl = 'http://www.job5156.com/qiye/shenzhen-15/pn'
#广告创意
#mainUrl = 'http://qy.58.com/sz_264/pn'


def companyLstGet(url,agents=ua.random,proxies = None):

    while True:
        try:
            time.sleep(2 + random.random() * 3)
            mresponse = requests.get(url, headers={'User-Agent': agents}, proxies=proxies, timeout=5).content
            break
        except:
            agents = ua.random
            time.sleep(200)
    if len(mresponse):
        html = etree.HTML(mresponse, parser=etree.HTMLParser(encoding='utf-8'))
        companyPageLst = html.xpath('//ul[@id="job_list"]//div[@class="line_com"]//a/@href')

    else:
        return 0

    return companyPageLst


def companyInfoGet(companyPageLst,agents=ua.random,proxies = None):

    companyNameLst = []
    companyAddrLst  =[]
    companySizeLst = []
    companyInfoLst = []
    companyBeloneLst = []

    for page in companyPageLst:
        page = "http://www.job5156.com" + page
        #print('do --------->'+ page)
        while True:
            try:
                time.sleep(2 + random.random() * 3)
                mresponse = requests.get(page, headers={'User-Agent': agents}, proxies=proxies, timeout=5).content
                break
            except:
                agents = ua.random
                time.sleep(200)
        if len(mresponse):
            html = etree.HTML(mresponse, parser=etree.HTMLParser(encoding='utf-8'))
            companyName = html.xpath('//h1[@class="com_name"]/text()')
            companyAddr = html.xpath('//div[@class="com_addr_content"]/span/text()')
            companySize = html.xpath('//ul[@class="basic_msg_list"]/li[2]/span/text()')
            companyInfo = html.xpath('//*[@id="com_intro_cont"]/div[1]/pre/text()')
            companyBelone = html.xpath('//ul[@class="basic_msg_list"]/li[1]/a/text()')

            companyNameLst.append(companyName)
            companyAddrLst.append(companyAddr)
            companySizeLst.append(companySize)
            companyInfoLst.append(companyInfo)
            companyBeloneLst.append(companyBelone)
        else:
            return 0


    companyLstInfoDf = pd.DataFrame([companyNameLst, companyBeloneLst,companyAddrLst, companySizeLst, companyInfoLst])

    return companyLstInfoDf.T


for i_page in range(1,41):
    print('doing -------------' + str(i_page))
    mUrl = mainUrl+str(i_page)
    print(mUrl)
    companyPageLst = companyLstGet(mUrl,agents=ua.random,proxies = None)
    companyLstInfoDf = companyInfoGet(companyPageLst,agents=ua.random,proxies = None)
    companyLstInfoDf.to_csv('ad_company_info_' + str(i_page) + '.csv')
    print(len(companyLstInfoDf))








