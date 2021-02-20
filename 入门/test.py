import random
print(" ~~~~~~~猜猜徐佳佳心里白马王子的编号吧~~~~~~~~~~~")
startNum=100
endNum=999
arm=random.randint(startNum,endNum)
count=0
while 1==1:
    temp=input("不妨猜一下徐佳佳心里想的白马王子编号吧,范围在%d-%d："%(startNum,endNum))
    guess=int(temp)
    count+=1
    if guess==arm:
        print('你猜的数字是%d,恭喜你猜对了'%guess)
        break
    elif guess>arm:
        print('你猜的数字是%d,大了'%guess)
        continue
    elif guess<arm:
        print('你猜的数字是%d,小了'%guess)
        continue
print("游戏结束,你总共猜了%d次"%count)