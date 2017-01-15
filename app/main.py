#!/usr/bin/env python3
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

def main(argv):
  for v in argv:
    print(v)
    print(len(v))

    urlprefix = 'http://54.92.123.84/search?'
    v = 'Title:' + v
    query = [
      ('ackey', '869388c0968ae503614699f99e09d960f9ad3e12'),
      ('q', v.encode('utf-8')),
    ]

    req = urllib.request.Request(urlprefix + urllib.parse.urlencode(query))
    with urllib.request.urlopen(req) as response:
      resdata = response.read()

    root = ET.fromstring(resdata)
    result = root.find('.//result')
    print(result.get('numFound'))
