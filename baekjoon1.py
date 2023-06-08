# # 백준 코테 2884번
# H, M  = map(int, input(). split())
# # H와 M을 한 줄에 입력 받는다.
#
# # 만일, 2시 30분인 상태일 경우
# if M < 45:
#     H= H-1
#     M = M+60
#     M = M - 45
#
# # 만일, 1시 45분 이상일 경우
# elif M >= 45:
#     M = M -45
#
# # 00시 30분일 경우 45분을 빼면 -1 시로 변하기 때문에 시간을 23시로 고정한다.
# if H<0: # 시간이 0 보다 작으면 23시로 해줘라.
#     H=23
#
# print(H, M)
#
# 백준 코테 2525번
# 첫 줄에 숫자(시), (분) 입력
# 두번째 줄에 추가할 시간 입력

# H, M = map(int, input().split())
# bns = int(input())
# 현재 시간이 2시 30분, 보너스 시간이 120분일 경우
# M = M + bns
# aa = bns // 60 # '//' 몫 값
# for i in range(aa):
#     if M >= 60:
#         H = H + 1
#         M = M - 60
#     if H>=24:
#         H = H-24
# print(H, M)

# H, M = map(int, input().split())
# bns = int(input())
#
# M = M+bns
# while M>=60:
#     H = H+1
#     M=M-60
#     if H>=24:
#         H = H-24
# print(H, M)

# 구구단 만들기
# a= int(input())
# for i in range(1, 10):
#     print(a, '*', i, '=', a*i)

# 코테 a+b 10950번
# t= int(input())
# for _ in range(t): # for _ in range : 변수를 사용하지 않을 경우 이용(i 제거) /반복 횟수만 중요한 것
#     a, b = map(int, input().split())
#     print(a+b)

## while 반복문
## 주어진 수가 10 보다 작다면 앞에 0을 붙여서 두 자리 수로 만들어라.
## 위의 숫자로 나온 두 자리 숫자를 더한다.
## 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리를 수를 이어 붙여라.

# while True:
#     a,b = map(int, input("숫자를 입력하세요 :").split())
#     if a < 10
#         b < 10
#         print("")
#     elif a < b:
#         break

input_num = int(input())

num = input_num  # num 변수에 input_num을 지정
cnt = 0
while True:
    sum_num = (num // 10) + (num % 10)  # 각 자릿수를 더한수
    new_num = ((num % 10) * 10) + (sum_num % 10)  # 새로 만들어지는 수
    cnt += 1  # 사이클 카운트
    if new_num == input_num :
        break
    num = new_num  # num 변수에 last_num을 지정
print(cnt)


## 백준 코테 1110번 파이썬
## 처음 숫자
## 십의 자리수 + 일의 자리수 = 더한 값
## 일의 자리수*10 + 더한 값의 일의 자리수 = 어떠한 값
## 반복
## 처음 숫자가 될 때 까지
## // 몫 % 나머지


# 1. 26을 입력하면 십의 자리수와 일의 자리수를 더한다.
# > 26을 지정넣고, 26을 몫값 2와 26 나머지값 6을 더하면 8
# 2. 지정한 26에서 10의 나머지 값에 10을 곱해서 십의자리수로 만든다.
# > 십의자리수 6 등장, 위에 더한 8을 일의자리수로 둔다.
# 3. 68 숫자 등장

'''
fir_num : A --------- 26
sum_num : A//10 + a%10 -------- 2 + 6 = 8
new_num : (fir_num % 10) * 10 + (sum_num % 10) ------ (6)*10 + 8 = 68
'''

fir_num = int(input())  ## 처음 숫자 입력
num = fir_num # 변수 fir_num / num / sum_num / new_num / cnt
cnt = 0

while True: # 사실일 동안
    sum_num = (num // 10) + (num % 10) # 2+6 =8  /// (num // 10) > 십의자리(몫) 수 뭐냐 / (num % 10) 일의자리수(나머지) 뭐냐
    new_num = (num % 10) * 10 + (sum_num % 10) # (6)*10 + 8 = 68
    cnt = cnt+1
    if new_num == fir_num:
        break # 만나면 밑에 내용 안하고 바로 나옴
    num = new_num
print(cnt)