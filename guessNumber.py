#coding=utf-8
from random import randint

def numIsCorrect(num):      #用于判断数据是否有效
    correct = False
    if num == 0:
        print "请输入有效的数字"
    elif num < 50 or num > 105:
        print "数字范围在50--105之间的哟"
    else:
        correct = True
    return correct

def numGuess(number,computer):          #用于提示用户答案范围
    guess = False
    if number - computer >= 20:
        print "猜的数字太大了"
    elif number - computer >= 10:
        print "猜的数字有点接近了"
    elif number - computer > 0:
        print "猜的数字已经非常接近了"
    elif number - computer == 0:
        guess = True
        print "恭喜大人，今晚吃🐷"
    elif number - computer > -10:
        print "猜的数字有点接近，但比答案小"
    elif number - computer > -20:
        print "猜的数字离答案有些遥远了,但比答案小"
    else:
        print "你已经成功远离了正确答案"
    return guess


fl = open("game.txt")
name = raw_input("请输入您的姓名")
dict = {}
for line in fl.readlines():
    # print line.split()
    dict[name] = line.split()

    print dict


# score = fl.read().split()
fl.close()
# game_times = int(score[0])                  #游戏总次数
# min_times = int(score[1])                   #最小成功轮数
# total_times = int(score[2])                 #猜过的总轮数
# name = raw_input("请输入你的名字")
# if game_times != 0:
#     print name+"已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案" % (game_times, min_times, float(total_times) / game_times)
# com = randint(50,105)
# print "游戏开始，请输入您猜的数字"
# you = input()
# game_times += 1
# total_times += 1
# min_times_num = 1
# while you:
#     if numIsCorrect(you):
#
#         if numGuess(you,com):
#             break
#         else:
#             print "请输入你猜的数字"
#             you = input()
#             min_times_num += 1
#             total_times +=1
#     else:
#         you = input()
#         continue
# if min_times == 0:
#     min_times = min_times_num
# else:
#     if min_times_num < min_times:
#         min_times = min_times_num
# lastData = [game_times,min_times,total_times]
# lastStr = []
# print lastData
# print score
# for time in lastData:
#     lastStr.append(str(time))
# string = " ".join(lastStr)
# fm = open("game.txt","a")
# fm.write("\n"+string)
# fm.close()