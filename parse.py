#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# @Time = '2018/10/7'
# author = ‘wulu’


from bs4 import BeautifulSoup

class parse:

    def parseHtml(self, txt):
        #判断是否为空
        if txt is None:
            print 'txt is None'
            return
        soup = BeautifulSoup(txt, 'html.parser')
        print soup
        divsoup = soup.find_all('div', attrs={'action-type': 'feed_list_item'})
        for div in divsoup:
            print div
            print '**************************************************************************************************'