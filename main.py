#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# @Time = '2018/10/7'
# author = ‘wulu’


from httpUtils import httpUtils
from parse import parse
import json


# url = 'https://weibo.com/ttarticle/p/show?id=2309404292491795940787'
# txt = httpUtils().getRequest(url)
# # print txt
# parse().parseHtml(txt)

urls = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_hot=1&pagebar=0&pl_name=Pl_Official_MyProfileFeed__20&id=1005053327799410&script_uri=/bugenniwan&feed_type=0&page=1&pre_page=1&domain_op=100505&__rnd=1538902301278'
txts = httpUtils().getJson(urls)
data = json.loads(txts)['data']
print parse().parseHtml(data)