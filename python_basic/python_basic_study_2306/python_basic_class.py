
## 클래스 - 점프 투 파이썬 184p
# result = 0
# def add(num):
#     global result  ## global 쓰면 전역 변수
#     result += num
#     return result
#
# add(5)
# print(add(3))

#
# result1 = 0
# result2 = 0
# def add1(num):
#     global result1  ## global 쓰면 전역 변수
#     result1 += num
#     return result1
#
# def add2(num):
#     global result2  ## global 쓰면 전역 변수
#     result2 += num
#     return result2
#
# add1(3)
# add1(5)
# add2(2)
# add2(3)
#
# class Calculator: # 클래스 생성
#     def __init__(self): #__init__ == 아래 setdata랑 같음 (self) 자기 자신 가르킴
#         self.result = 0
#
#     def add(self, num):
#         self.result += num
#         return self.result
#
# cal1 = Calculator() # 객체 생성
# cal2 = Calculator()
#
# print(cal1.add(3)) ## cal1.add // cal1에 있는 add라는 함수를 사용하겠다.
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

## 사칙 연산 만들기- 점프 투 파이썬 197p

class ForCal: ## 클래스 생성
    def setdata(self, first, second): ## self : 클래스 자신을 가르킴 / 현재 코드상 setdata 를 칭함  // 자바로 치면 해당 클래스 this 를 말함
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = ForCal() ## 객체 생성
b = ForCal()

a.setdata(4, 2)
b.setdata(3, 8)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

print(b.add())
print(b.mul())
print(b.sub())
print(b.div())


## 상속 - 점프 투 파이썬 203p
class MoreFourCal(ForCal): ## 클래스 | 클래스명  | (상속받을 클래스명)
    pass # 패쓰 쓰면 상속 받은 클래스 그대로 반영