# import random
#
# list = [ ]
# ran_num = random.randint(0,9)
#
# for i in range(3):
#     while ran_num in list:
#         ran_num = random.randint(0,9)
#         list.append(ran_num)
#
#         list.sort() # 리스트 나온 내용 오름차순
#         print(list)


## 백준 코테 10807번
# '''
# 첫줄에 숫자 몇개 적을지
# 둘째줄에 숫자 입력(첫 줄에 입력한 개수 만큼)
# 세번째 줄에 찾을 숫자가 뭔지 작성
# '''

# num = int(input()) # 숫자 몇개 적을건지
# a = list(map(int, input().split())) # 숫자 입력 list를 이용해 묶음 / map ~ split 는 여러 정수 입력 시 사용
# final_num = int(input()) # 찾을 숫자가 뭔지 작성
# print(a.count(final_num)) # final_num 의 값을 세어라. list 안에 들어가 있는
#
# # ex) 숫자 5개 쓸래, 5개의 숫자에서 2가 몇개 나왔는지 볼래

# 백준 코테 10871번
# '''
# 첫줄에 N하고 X가 주어짐, N 값은 A의 개수, X값은 최종적으로 X 보다 작은 값들 출력
# 두번째 줄 A - list(map(int, input().split())) <--- 입력될 숫자의 개수 : N
# 최종 출력 : A 값들 중 X 보다 작은 값들 출력
# '''

# N, X = map(int,input().split())
# A = list(map(int,input().split()))
# for i in (N):
#     if A[i] < X:
#         print(A[i], end=" ")
#
# for i in range(5):
#     print(i, end=" ") # end 는 줄 바꿈 안됨 / i값 나온거를 한 줄로 세워주세요, " " 은 한 번 공백 뛰어서 해줘


# a = [1, 2, 3, 4, 5, 6]
# #    ^  ^  ^  ^  ^  ^
# #    0  1  2  3  4  5 <----- 인덱스 값
# print(a[0]) #  [] (대괄호) 인덱스 : 위치값(주소값)

# a_list = [i for i in range(1, 11)] # 1 ~ 10 까지 i에 넣어준다.
# print(a_list)
# print(max(a_list)) # a_list 값에서 최대값 출력
# print(min(a_list)) # a_list 값에서 최소값 출력
# a_list.remove(3) # remove : 제거하다. / 3 제거해라
# print(a_list)


# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
# 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.
# 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.
# 출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.

# '''
# 총 30명
# 28명이 과제를 제출한다.
# 2명이 안한다
# 안한 2명을 추출해라.(2줄, 작은 값 부터)
# '''
#
#
# #students = [i for i in range(1,31)]
# # [1, 2, 3, 4, 5, 6....29, 30]
#
# # i for i in range(1,31) 후자에 들어간 i값을 for 앞에 있는 i에 변수 값이 들어감.
# # list 값 선언할 때(열어줄 때), 리스트에서 인덱스값(자리) 추출할 때만 ' [] ' 사용
# # s_list[0] : 리스트에서 인덱스값으로 뽑아줄 떄
# # s_list.remove()
#
#
#
# s_list= [i for i in range(1,31)]
# for _ in range(28):
#      stu_sum = int(input())
#      s_list.remove(stu_sum)
#
# print(min(s_list))
# print(max(s_list))


# # set() : 리스트에 있는 중복 숫자를 제거한다.
# a = [1, 2, 3, 3, 3]
# b = list(set(a))
# print(b)
#
# a="나는 천재입니다."
# print(len(a)) # len : 문자열 길이 세기


# A=[1, 3, 3]
# print(A)
# A.append("5")
# print(A)


'''
1. 숫자 10개 입력(10줄로 입력)
2. 각 입력된 숫자마다 42로 나눈 값
3. 나눈 값이 몇 종류인지 --> 1, 2, 3, 3 ---> 3 종류의 숫자
 > 중복을 제거해라
'''

# # 리스트에서 set 함수를 이용하여 중복을 제거한다.
# rest_list = [ ] # 42로 나눈 값 등록됨
# for i in range(10): # 숫자 10개 입력(10줄로 입력)
#     input_num = int(input())
#     rest = input_num % 42 # 각 입력된 숫자마다 42로 나눈 값 / rest에 나눈 값을 담는다.
#     rest_list.append(rest) # rest_list에 rest에 들어간 숫자를 등록해라.
# result = set(rest_list) # 42로 나눈 값을 set으로 중복 제거한다.
# print(len(result)) # len 은 문자열을 세어준다.(문자의 개수를 센다.)
#
#
# # 백준 런타임 에러 의미: 더 짧은 코드가 존재한다.

rest_list = [ ]
for i in range(10):
    input_num = int(input())
    rest_list.append(input_num % 42)
print(len(set(rest_list)))