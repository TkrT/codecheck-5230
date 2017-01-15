﻿# coding: utf-8
# エンコードはutf-8
#更新

import sys
import urllib
import urllib2
import xml.etree.ElementTree as ET
import json

def main(argv):
  maxtitle = ""
  maxnumber = 0

  for v in argv:
    urlprefix = 'http://54.92.123.84/search?'
    query = [
      ('ackey', '869388c0968ae503614699f99e09d960f9ad3e12'),
      ('q', 'Body:' + urllib.quote(v)),
    ]

    url = urlprefix
    for item in query:
      url += item[0] + "=" + item[1] + "&"
    url = url[:-1]

    response = urllib2.urlopen(url)
    resdata = response.read()

    root = ET.fromstring(resdata)
    result = root.find('.//result')
    number = int(result.get('numFound'))

    if (number > maxnumber):
      maxnumber = number
      maxtitle = v

  jsoncontent = OrderedDict()
  jsoncontent['name'] = maxtitle
  jsoncontent['count'] = maxnumber
  jsonstring = json.dumps(jsoncontent, sort_keys=False, ensure_ascii=False)
  print(jsonstring)
