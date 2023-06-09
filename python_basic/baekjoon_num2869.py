
## 2869 백준 달팽이는 올라가고 싶다 ## 다시 풀어보기!
A, B, V = map(int, input("입력: ").split())

day_list = []
day = 0 # 최종날

while True: # 반복문 제거 # 메모리 초과

    # 아침과 높이가 같을 때
    if A == V:
        print(1,"날")
        break

    # 아침+밤 도착
    day += A - B ## 낮 밤 합계
    day_list.append(day)

    if day_list[-1] >= V:
        print(len(day_list),"날")
        break

    elif day_list[-1]+A >= V: ## 아침 케이스
        print(len(day_list)+1, "날")
        break
