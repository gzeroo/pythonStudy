# 2022.12.22 백준 코테 문제 입출력과 사칙 연산
#
# print("hello world!")
#
# # 첫 줄에 A, B가 주어진다.
# # A와 B는 입력 받아야 함.
# # a = int(input())
# # map 묶다 # split 나누다.
#
# # 정수형은 map 묶고 split 나눠서 한 줄에 2개 정수 입력
# A, B= map(int, input().split()) # 정수형
# print(A+B)
#
# # 문자열은 map 안묶고 문자 입력 가능
# # A, B = (input().split()) # 문자열
# # print(A+B)
#
#
# # 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
# A, B= map(int, input().split()) # 정수형
# print(A-B)
#
# # 두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.
# A, B= map(int, input().split())
# print(A*B)
#
# # 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.
# / : 나누기
# // : 몫
# % : 나머지
# != : 같지 않다.
# A, B= map(int, input().split())
# print(A/B) # 나누기
# print(A%B) # 나머지 나옴 // ex. 7 나누기 4 하면 3 나옴 /
# print(A//B) # 몫만 나옴 // ex. 7 나누기 4 하면 1 나옴 /
#
# # 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A//B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
# # 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
# # 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
#
# A, B= map(int, input().split())
# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B) ##나머지를 구한다. 나누고 남은 값
#
# # 첫째 줄에 준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어진다. 아이디는 알파벳 소문자로만 이루어져 있으며, 길이는 50자를 넘지 않는다.
# # 첫째 줄에 준하의 놀람을 출력한다. 놀람은 아이디 뒤에 ??!를 붙여서 나타낸다.
#
# a=input("")
# print(a+"??!")
#
# # 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
# A, B= map(int, input().split())
# if A > B:
#     print(">")
# elif A < B:
#     print("<")
# else:
#     print("==")
#
# # 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# a=int(input())
# if a>=90:
#     print("A")
# elif a>=80:
#     print("B")
# elif a>=70:
#     print("C")
# elif a>=60:
#     print("D")
# else:
#     print("F")
#
# # 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# # 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# # 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다.
# # 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
#
# # 윤년: 4의 배수, 100의 배수가 아니어야함 or 400의 배수
# year=int(input())
# if (year%4 == 0 and year%100 != 0 or year%400 == 0):
#     #4로 나눴을 때 0이 되어야하고 100으로 나눴을 때 나머지가 0이 되면 안된다. 또는 400으로 나눴을 때 나머지가 0이면 print 1 한다.
#     print(1)
# else:
#     print(0)

# # 백준코드 14681번 사분면 고르기
# x = int(input())
# y = int(input())
# if x > 0 and y > 0: # 양수
#     print(1)
# elif x < 0 and y > 0: # x 음수 y 양수
#     print(2)
# elif x < 0 and y < 0: # x 음수 y 음수
#     print(3)
# else:
#     print(4)

# # # 백준코드 2884번
# # 분에서 45분을 뺼 수 있을 때 첫번째에서는 뺀다. 만일, 분이 45분 미만일 경우 '시'에서 1시간을 빼고 15분을 더한다.
# # 두번째 조건에서 '시'가 0보다 작으면 -'시'가 되기 때문에 0보다 크다는 조건을 둔다.
# # 마지막 조건에서는 23시를 고정으로 두고 마지막 +15분을 해준다.
# H, M= map(int, input().split())
# if M >= 45:
#     print(H,M-45)
# elif H > 0 and M < 45:
#     print(H-1,M+15)
# else:
#     print(23, M+15)

