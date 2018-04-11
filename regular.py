# coding=utf-8
import re

string = "Hi,I am Shirley Hilton. I am his wife."
m = re.findall(r"I.*?e",string)
try:
    print(m)
except:
    print("不存在")

string = "site sea sue sweet see case sse ssee loses"
n = re.findall(r"\bs\S*?e\b",string)
print n

string = "79846513218846132148911324897112152115026972893114871878986523198732149"
m = re.findall(r"1[0-9]{9}3",string)
print m