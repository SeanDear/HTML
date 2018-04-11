#coding:utf-8
import urllib2
from city import city
import json


cityName = raw_input("请输入查询天气的城市")
cityCode = city.get(cityName)
if cityCode:
    url = ("http://www.weather.com.cn/data/cityinfo/%s.html"%cityCode)
    content = urllib2.urlopen(url).read()
    data = json.loads(content)
    weather_dict = data["weatherinfo"]
    high = u"最高温度:"+weather_dict["temp1"]
    low = u"最低温度:"+weather_dict["temp2"]
    weather = u"天气:"+weather_dict["weather"]
    time = u"时间："+weather_dict["ptime"]
    list = [cityName,high,low,weather,time]
    for sub in list:
        print sub+"\n"




