    #三门问题,即美国节目Let's Make a Deal中最后从分别有两只羊和一辆车的三个门中选择一个的游戏,以下是对该游戏的模拟,以模拟者获得五辆汽车为结束,记录总共获得的山羊数量和汽车数量,给模拟者一个直观的概率映像.
    #编者:其实就是我妈怎么也不信换门会比不换获得车的几率高,最后给她测试了一下她就不玩了还是要固执己见,说服人真™是一件难事.
from random import randint
from random import choice
car_get = 0
goat_get = 0
select_list = ["1","2","3"]
change_list = ["y","n"]

def win():
    print("恭喜您获得汽车一辆")
    global car_get
    car_get += 1
    print ("您现在共获得了%d辆汽车" % car_get)

def wrong():
    print("恭喜您获得山羊一头")
    global goat_get
    goat_get += 1

def cardoor(car,door):
    if car == door[0]:
        door1 = 1
        door2 = 0
        door3 = 0
    elif car == door[1]:
        door1 = 0
        door2 = 1
        door3 = 0
    else:
        door1 = 0
        door2 = 0
        door3 = 1

def opengate(car,door,select):
    global change
    global change_list
    if door[int(select)-1] == car:
        del door[int(select)-1]
        gateopen = choice(door)
        while change not in change_list:
            change = input("第%d扇门被打开了,里面是一只山羊,您要选择另一扇门吗?y/n"% gateopen)
            if change == "y":
                wrong()
            elif change == "n":
                win()
            else:
                print("请重新输入")

    else:
        del door[int(select)-1]
        if door[0] == 1:
            while change not in change_list:
                change = input("第%d扇门被打开了,里面是一只山羊,您要选择另一扇门吗?y/n"% door[1])
                if change == "y":
                    win()
                elif change == "n":
                    wrong()
                else:
                    print("请重新输入")
        else:
            while change not in change_list:
                change = input("第%d扇门被打开了,里面是一只山羊,您要选择另一扇门吗?y/n"% door[0])
                if change == "y":
                    win()
                elif change == "n":
                    wrong()
                else:
                    print("请重新输入")

while car_get < 5:
    select = 0
    change = 0
    car = randint(1,3)
    door = [1,2,3]
    cardoor(car,door)
    while select not in select_list:
        select = input("请输入您选择的门的阿拉伯数字,按回车结束:")
        if select not in select_list:
            print("请重新输入")
    opengate(car,door,select)

print("至此您总共获得了5辆汽车和%d只山羊"% goat_get)
