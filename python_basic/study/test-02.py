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

# if문 and / or
if (3==3) and (1==1) or (4==2): # 3과 3이 같고, 1과 1이 같기 때문에 4와 2가 같지 않아도 '아싸'를 출력한다.
    print("아싸")