import random

# 구구단 만들기
# num = int(input())
# for i in range(1, 10):
#     n = num*i
#     print(num, "*", i, "=", n)

# # 합
# n = int(input())
# a_list = []
# for i in range(1, n+1):
#     a_list.append(i)
# print(sum(a_list)) # [ 0, 1, 2 ]

# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i
# print(sum)

# score = int(input())
# if 100 >= score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")


## 백준 알람시계 // 문제 번호 2884
## 2개 입력 받을 때 아래와 같이 map 을 쓰고 split(문자열 나누기) 해주기

# num1, num2 = map(int, input("숫자 2개를 입력해주세요: ").split())
#
# if num2 >= 45:
#     num2_time = num2 - 45
#     print(num1, "시", num2_time, "분")
# elif num2 < 45:
#     if num1 == 0:
#         num1_time = 23
#         num2_time = (num2+60)-45
#         print(num1_time,"시", num2_time,"분")
#     elif 24 >= num1 > 0:
#         num1_time = num1 - 1
#         num2_time = (num2+60)-45
#         print(num1_time,"시", num2_time,"분")


# while True:
#     num1, num2 = map(int, input("숫자 2개를 입력해주세요: ").split())
#     if num1 != 0 and num2 != 0:
#         print(num1 + num2)
#     elif num1 == 0 and num2 == 0:
#         break

# num = int(input())
# a_list = list(map(int, input().split())) # 리스트 여러개 숫자 받기
# num_find = int(input())
# print(a_list.count(num_find))

# print("몇번 입력할까요?")
# num1 = int(input("입력: "))
# a_list = []
#
# for i in range(num1):
#     print("현재", i+1,"번 입력했습니다.")
#     print("숫자를 입력해주세요: ")
#     num2 = int(input())
#     a_list.append(num2)
# print("무슨 숫자를 찾을까요?")
# num_find = int(input())
# print("찾는 숫자의 개수는: ", a_list.count(num_find))


