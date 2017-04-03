from random import randint    #从random模块中加载Randint（随机整数）方法
num = randint(1,100)    #设定一个1到100之间的随机数

print("Guess the number!")
bingo = False    #与下文中的while并用，使游戏结束前重复answer = int(input())过程

while bingo == False:
    answer = int(input())    #设定输入的整数为回答    此处不能输入浮点数，会报错，之后记得看下怎么修改
    
    if answer < num:
        print("too small!")

    if answer > num:
        print("too big!")

    if answer == num:
        print("BINGO!")
        bingo = True
