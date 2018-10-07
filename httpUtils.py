#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# @Time = '2018/10/7'
# author = ‘wulu’


import requests
import webbrowser


class httpUtils:

    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
               'Cookie': 'SINAGLOBAL=9170976356248.912.1536582816735; UOR=,,cuiqingcai.com; YF-Ugrow-G0=ea90f703b7694b74b62d38420b5273df; login_sid_t=aef81d7ce6db887b80b1d1e5589acaa3; cross_origin_proto=SSL; YF-V5-G0=5f9bd778c31f9e6f413e97a1d464047a; wb_view_log=1440*9002; _s_tentry=passport.weibo.com; Apache=8249900273619.832.1538895011848; ULV=1538895011858:3:1:1:8249900273619.832.1538895011848:1537771751360; YF-Page-G0=a478b43c3fd6f5a258feb64dc37bff16; WBtopGlobal_register_version=9744cb1b8d390b27; WBStorage=e8781eb7dee3fd7f|undefined; SCF=AoL5zTWQ_aOOCX3B3v4SSNXEuNRki5_vExUFvq1AA1K1BK2zYPxw7nTUzjoWrFWsYfMLZYFPshJGnc5efyaKkn8.; SUB=_2A252vcikDeRhGeNP6FEY9ifJzz6IHXVVyr1srDV8PUNbmtBeLXPGkW9NToLVZ3rW-TlMeFDCH95UIh9GC5earQAo; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh2fkqZGAzELsvz0Q.Ku5qk5JpX5K2hUgL.Fo-pe0e4So.fShz2dJLoIfQLxKnLB.BLB-eLxKnLB.2LB-zLxK.L1K.L12eLxKnLBoMLB-qLxKBLBonLBoqLxK-L122LBoeLxKnLBo-L1hBLxKBLBonL12BLxK-L1-eLBKnLxKBLBo.L12-t; SUHB=0D-F_MFDiDWlh4; ALF=1539503126; SSOLoginState=1538898164; un=281822114@qq.com; wb_view_log_5133969542=1440*9002'}

    url = 'https://weibo.com/bugenniwan'

    def getRequest(self, url):

        #判断url是否为空
        if url is None:
            print 'urs is None'

        txt = requests.get(url, headers=self.headers)

        if txt is None:
            print 'request result is None'

        return txt.text

    def getJson(self, url):

        if url is None:
            print 'url is None'

        txt = requests.get(url, headers=self.headers)

        if txt is None:
            print 'request result is None'

        return txt.text.encode('utf-8')

