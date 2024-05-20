import pyinputplus as pyip
import random
while True:
    min=1
    max=100
    
    count = 0
    target = random.randint(min,max)
    print(target)
    print("==========猜字遊戲==========\n")
    while True:
        count +=1
        keyin = pyip.inputInt(f"猜數字的範圍{min}~{max}\n")
        print(keyin)
        if keyin == target:
            print(f"賓果 !猜對了,  答案是{target}")
            print(f"您總共猜了{count}次")
            break
        elif(keyin > target):
            print("再小一點")
            max = keyin-1
        elif(keyin < target):
            print("再大一點")
            min = keyin + 1
        print(f'你已經猜了{count}次')
    playagain = pyip.inputYesNo("還要繼續玩遊戲嗎?(y,n)")
    if playagain == 'no':
        break

    print("遊戲結束")
