#coding=utf-8

#This fuc grab all .jpg from a baidu tieba

import urllib
import re
import os
import shutil
import path
import GLOBAL_PARA


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, picPath+'%s.jpg' % x)
        x+=1

picPath=GLOBAL_PARA.OUTPUT
path.delete_path(picPath)
url="http://tieba.baidu.com/p/2460150866"
html = getHtml(url)
getImg(html)
