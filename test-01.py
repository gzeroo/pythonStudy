# 2022.12.22
# input / 입력

a = input("이름을 입력하세요 : ") # 입력(숫자, 문자, 문자열) / str 문자열로 인식
b = int(input("나이를 입력하세요 : ")) # 입력 정수 / 입력값을 모두 정수로 인식
print("당신의 이름은", a, "입니다.")
print("당신의 나이는", b, "살 입니다.")

# a = input()
# print(type(a))

# int : (정수)
# str : string(문자열)

a = int(input())
b = int(input())
gob = a*b
print(gob)

# a = input("이름을 정해주세요.")
# b = int(input("숫자를 입력하세요."))
# print("당신의 이름은", a, "입니다.")
# print("당신의 숫자는", b, "입니다.")

a = int(input("숫자를 입력하세요."))
b = int(input("숫자를 입력하세요."))
if a > b:
    print("a가 b 보다 큽니다.")
elif b > a:
    print("b가 a 보다 큽니다.")
else:
    print("a랑 b는 같습니다.")

# 정수형은 map 묶고 split 나눠서 한 줄에 2개 정수 입력
A, B= map(int, input().split()) # 정수형
print(A+B)

# 문자열은 map 안묶고 문자 입력 가능
# A, B = (input().split()) # 문자열
# print(A+B)

