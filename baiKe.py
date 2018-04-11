# coding=utf-8
import urllib2



url = "https://www.qiushibaike.com/"
data = urllib2.urlopen(url).read()
print data