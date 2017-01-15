# coding: utf-8

import sys
import urllib
import urllib2
import xml.etree.ElementTree as ET

def main(argv):
    #最大件数取得用の変数を初期化
    maxtitle = ""
    maxnumber = -1

    for v in argv:
        #キーワードと検索期間からクエリを作成
        urlprefix = 'http://54.92.123.84/search?'
        query = [
            ('ackey', '869388c0968ae503614699f99e09d960f9ad3e12'),
            ('q', 'Body:' + urllib.quote(v)),
        ]

        #URLの形に整形
        url = urlprefix
        for item in query:
            url += item[0] + "=" + item[1] + "&"
        url = url[:-1]

        #レスポンスを取得
        response = urllib2.urlopen(url)
        resdata = response.read()

        #XMLを解析して件数を取得
        root = ET.fromstring(resdata)
        result = root.find('.//result')
        number = int(result.get('numFound'))

        #最大件数の項目を更新
        if (number > maxnumber):
            maxnumber = number
            maxtitle = v


    #出力を整形
    string = '{"name":"' + maxtitle + '","count":' + str(maxnumber) + '}'

    #出力
    print(string)
