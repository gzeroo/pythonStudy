import random


print("가위 바위 보를 해요!")
num = int(input("몇회 할까요?: "))

for i in range(num):
    ai = random.choice(["가위", "바위", "보"])

    print("=" * 50)
    print("현재", i+1,"회차 입니다.")
    print("가위 바위 보 중에서 하나를 입력하세요")
    print("=" * 50)

    you = input("입력: ")

    print("당신: ", you, "||", "상대방: ", ai)

    if you == ai:
        print("비겼습니다!")
    elif you == "보" and ai == "가위":
        print("ai가 이겼습니다!")
    elif you == "바위" and ai == "보":
        print("ai가 이겼습니다!")
    elif you == "가위" and ai == "주먹":
        print("ai가 이겼습니다!")
    else:
        print("you 가 이겼습니다!")