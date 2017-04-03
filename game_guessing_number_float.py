from random import uniform
num = uniform(1,100)

print("Guess the number!")
bingo = False

while bingo == False:
    answer = int(input())

    if answer < int(num):
        print("too small!")

    if answer > int(num):
        print("too big!")

    if answer == int(num):
        print("BINGO!")
        print(num)
        bingo = True
