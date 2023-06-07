# # 숫자형
# a=7;
# b=4;
# print(a%b);
# print(a//b);
#
# c="가나";
# d="다라";
#
# print(c+d);
#
# print("=" * 50);
# print("My Program");
# print("=" * 50);
#
# # f 문자열 포매팅
# name = "홍길동";
# age = 30;
# print(f'나의 이름은 {name}입니다. 나이는 {age+1}살 입니다.');

# 정렬과 공백(안씀)
# a= "%10s" % "hi";
# print(a);

# 소수점 표현하기(안씀)
# a= "%0.4f" % 3.1234534; # 소수점 4자리 까지만 출력하겠다.
# print(a);

# # 숫자 바로 대입하기(자주 씀) - 점프 투 파이썬 62p // ex. 쿠팡 페이지 넘버 변경 시 사용(ex. 쿠팡에서 노트북 검색 후 겟 파라미터 http 2번창 변경)
# a= "I eat {} apples".format(3); # format 숫자가 괄호 안에 들어가서 출력 됨
# print(a); # 출력 결과 I eat 3 apples 출력됨

# # 문자 개수 세기 && 문자 위치 찾기
# a = "hobby";
# c = a.count('b'); # 문자 개수 세기
# b = a.find('y') # 문자 위치(문자 존재 유무) 찾기 # 없는 값을 찾아달라고 하면 -1 뜸
# e = a.index('o'); # 문자 위치(주소값) 찾기 # 없는 값 찾아달라고 하면 에러 뜸
# print(c, b, e);

# print(",".join('abcd')); # 출력 결과: a,b,c,d // abcd 사이에 "," 가 들어감
#
# a = "hi";
# b = "HI";
# print(a.upper()); # a를 대문자로 올려라
# print(b.lower()); # b를 소문자로 내려라

# # 공백 제거
# a = "    HI     ";
# print(a.lstrip()); # 왼쪽 공백 제거
# print(a.rstrip()); # 오른쪽 공백 제거
# print(a.strip()); # 공백 양쪽 제거

# 문자열 나누기
a = "Life is too short";
print(a.split()); # 공백 기준으로 문자열 나누기 // split() '()' 괄호 안에 있는 기준으로 나뉨

a = "a:b:c:d";
print(a.split(":"));
