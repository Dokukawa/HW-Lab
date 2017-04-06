def Equal(num1,num2):
    if num1 < num2:
        print("%d is too small!"% num1)
        return False
    elif num1 > num2:
        print("%d is too big!"% num1)
        return False
    else:
        print("BINGO!The right number is %d!"% num1)
        return True

from random import randint
num = randint(1,100)
print("Guess the number!")
bingo = False
while bingo == False:
    answer = eval(input('input a integer here:'))
    bingo = Equal(answer,num)
