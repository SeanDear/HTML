#coding=utf-8
# import urllib2
# import json
#
# url = "http://m.weather.com.cn/data3/city.xml"
# content1 = urllib2.urlopen(url).read()
# print content1
# province = content1.split(",")
# filel = open("city.txt","w")
# for city in province:
#     citylist = city.split("|")
#     lastData = "%s   %s"%(citylist[0],citylist[-1])+"\n"
#     print lastData
#     filel.write(lastData)
class myClass:
    name = "Sean"
    def sayHi(self):
        print "Hello my name is %s"%(self.name)+"\n"

mc = myClass()
print mc.name
mc.name = "Lily"
print mc.sayHi()