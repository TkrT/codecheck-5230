#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
      ('q', 'Title:' + urllib.quote(v.encode('utf-8'))),
    ]

    url = urlprefix
    for item in query:
      url += item[0] + "=" + item[1] + "&"
    url = url[:-1]

    response = urllib2.urlopen(url)
    resdata = response.read()

    root = ET.fromstring(resdata)
    result = root.find(u'.//result')

    if (number > maxnumber):
      maxnumber = number
      maxtitle = v

  jsoncontent = {
    "name": maxtitle,
    "count": maxnumber
  }
  jsonstring = json.dumps(dict)
  print(jsonstring)
