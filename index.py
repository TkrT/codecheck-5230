# coding: utf-8
# エンコードはutf-8

import sys
from app.main import main

reload(sys)
sys.setdefaultencoding('utf-8')
main(sys.argv[1:])
