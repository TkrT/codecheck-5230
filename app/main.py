#!/usr/bin/env python3
# coding: utf-8
import sys
import os
import urllib.parse
import xml.etree.ElementTree as ET
import asyncio
import aiohttp

#Webページの取得
@asyncio.coroutine
def get(url):
    response = yield from aiohttp.request('GET', url)
    return (yield from response.text())

#XMLを解析して件数を取得
def analyzeAsahiXML(page):
    root = ET.fromstring(page)
    result = root.find('.//result')
    return (int(result.get('numFound')))

#記事件数の取得
@asyncio.coroutine
def getMaximumArticleNumber(maxTitle, maxNumber, prefix, keyword):
    #URLの作成と読み込み
    q = "Body:" + keyword 
    url = prefix + 'q=' + urllib.parse.quote(q.encode('utf-8'))
    page = yield from get(url)

    #XMLを解析して件数を取得
    number = analyzeAsahiXML(page)

    #最大件数の項目を更新
    if (number > maxNumber[0]):
        maxNumber[0] = number
        maxTitle[0] = keyword

def main(argv):
    #キーワードリストを作成
    keywordNumber = len(argv)
    Keywords = []
    for i in range(0, keywordNumber):
        Keywords.append(os.fsencode(argv[i]).decode(sys.getfilesystemencoding()))

    #記事検索用のプレフィックスを作成
    prefix = 'http://54.92.123.84/search?'
    query = [
        ('ackey', '869388c0968ae503614699f99e09d960f9ad3e12'),
        ('rows', '1'),
    ]
    for item in query:
        prefix += item[0] + "=" + item[1] + "&"

    #最大件数取得用変数を初期化
    maxTitle = [""]
    maxNumber = [-1]

    #記事検索
    loop = asyncio.get_event_loop()
    f = asyncio.wait([getMaximumArticleNumber(maxTitle, maxNumber, prefix, v) for v in Keywords])
    loop.run_until_complete(f)

    #出力を整形
    string = '{"name":"' + maxTitle[0] + '","count":' + str(maxNumber[0]) + '}'

    #出力
    print(string)
