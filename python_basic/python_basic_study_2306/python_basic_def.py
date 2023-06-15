
# ## 함수 만들기 / 점프 투 파이썬 150p
# def add(a, b):
#     return a + b
#
# a = 3
# b = 4
# c = add(a, b)
#
# print(c)
#
##################

# def add(a, b):
#     result = a+b
#     return result
# ###################
# def say():
#     return "hi"
#
# a = say()
# print(a)

# def add(a, b):
#     print("%d, %d의 합은 %d입니다." % (a, b, a+b))
#
# add(3, 4) # 3, 4의 합은 7입니다.
# a = add(3, 4) # 3, 4의 합은 7입니다.
# print(a) # none
#
#
# def add(a, b):
#     return a+b
# a = add(a = 3, b = 4)
# b = add(b = 3, a = 4)
# c = add(3, 4)
# print(a, b, c)

def add_many(*args): ## *args // 받아온 매개변수 값을 넣는다 // for i in a_list 랑 유사
    result = 0
    for i in args:
        result = result + i
        return result

a = add_many(1, 2, 3, 4, 5)
print(a)

def add_and_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result + i
    return result

b = add_and_mul('add', 1,2,3,4,5)
c = add_and_mul('mul', 1,2,3,4,5)
print(b, c)