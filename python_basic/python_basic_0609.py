
# 함수(def)에서 결과값(return)은 무조건 하나이다.
# def add_and_mul(a,b):
#     return a+b, a*b
#
# a = add_and_mul(2, 3)
# print(a) ## 튜플로 출력됨(수정, 삭제 X)


def say_myself(name, old, man=True): ## man / 성별을 입력하지 않을 경우 자동으로 True // 남자로 고정됨. 기본값 남자!
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)

