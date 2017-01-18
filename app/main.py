#!/usr/bin/env python3
# coding: utf-8
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

#記事件数の取得
@asyncio.coroutine
def getArticleNumber(keyword):
    global AsahiURLPrefix
    global maxTitle
    global maxNumber

    #URLの作成と読み込み
    query = 'q=Body%3A' + urllib.parse.quote(keyword.encode('utf-8'))
    url = AsahiURLPrefix + query
    page = yield from get(url)

    #XMLを解析して件数を取得
    root = ET.fromstring(page)
    result = root.find('.//result')
    number = int(result.get('numFound'))

    #最大件数の項目を更新
    if (number > maxNumber):
        maxNumber = number
        maxTitle = keyword

def main(argv):
    #global変数の定義
    global AsahiURLPrefix
    global maxTitle
    global maxNumber

    #キーワードリストを作成
    keywordNumber = len(argv)
    Keywords = []
    for i in range(0, keywordNumber):
        Keywords.append(argv[i])

    #最大件数取得用変数を初期化
    maxTitle = ""
    maxNumber = -1

    #記事検索用のプレフィックスを作成
    AsahiURLPrefix = 'http://54.92.123.84/search?'
    query = [
        ('ackey', '869388c0968ae503614699f99e09d960f9ad3e12'),
        ('rows', '1'),
    ]
    for item in query:
        AsahiURLPrefix += item[0] + "=" + item[1] + "&"

    #記事検索
    loop = asyncio.get_event_loop()
    f = asyncio.wait([getArticleNumber(d) for d in Keywords])
    loop.run_until_complete(f)

    #出力を整形
    string = '{"name":"' + maxTitle + '","count":' + str(maxNumber) + '}'

    #出力
    print(string)
