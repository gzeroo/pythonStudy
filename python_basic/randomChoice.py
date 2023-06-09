import random


print("가위 바위 보를 해요!")
num = int(input("몇회 할까요?: "))

ai_win = 0
you_win = 0
num_win = 0

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
        num_win += 1
    elif you == "보" and ai == "가위":
        print("ai가 이겼습니다!")
        ai_win += 1
    elif you == "바위" and ai == "보":
        print("ai가 이겼습니다!")
        ai_win += 1
    elif you == "가위" and ai == "주먹":
        print("ai가 이겼습니다!")
        ai_win += 1
    else:
        print("you 가 이겼습니다!")
        you_win += 1

print("="*50)
print("가위 바위 보 결과:", you_win,"승", num_win, "무", ai_win, "패")
print("="*50)

## 입력 잘못받을 경우 재입력 받고 진행되게 하기
