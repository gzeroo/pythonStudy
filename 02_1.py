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
#
# # 문자열 나누기
# a = "Life is too short";
# print(a.split()); # 공백 기준으로 문자열 나누기 // split() '()' 괄호 안에 있는 기준으로 나뉨
#
# a = "a:b:c:d";
# print(a.split(":"));

# # 리스트 자료형 - 점프 투 파이썬 72p
# odd = [1, 3, 5, 7, 9, "문자열1", "문자열2", [1, 2]];
# print(odd);
#
# a = [1, 2, "안녕하세요"];
# print(a);
# print(a[0]+a[1]);
# print(a[-1]); # [-1] 인덱스는 맨 마지막 값 출력
# print(a[-1][0]); # a[-1] 인덱스에서 [0] 자리 값 출력 '안' 출력 됨
# print(a[0:1]); # 0 인덱스 부터 1 인덱스 앞까지 출력
#
# # 인덱스 : 주소값
# student1 = ["김진욱", "김지영", "김현덕", "양민주", "이창현"];
# student2 = ["임명렬"];
# print(student1[:3]);
# print(student1+student2);
# print((student1+student2)*2); # 반복 가능 " * " 곱하기 해주기
#
# # 리스트 길이 구하기
# print(len(student1));
#
# # 리스트 수정과 삭제(del)
# student1[1] = "홍길동";
# print(student1[1]);
# print(student1); # 홍길동 들어간거 확인 완료
#
# del student1[0]; # del 리스트 삭제
# print(student1);
#
# # 리스트 추가(append)
# student1.append("홍길동2");
# print(student1);
#
# # 리스트 정렬
# student = [1, 3, 4, 2, 5, 8, 6, 7]
# student.sort(); # sort 작은 순서대로 정렬 // 숫자, 영어(A,B,C) 가능
# print(student);

# # 리스트 insert / remove
# student1 = ["김진욱", "김지영", "김현덕", "양민주", "이창현"];
# print(student1.index("김현덕"));  # 김현덕 어느 인덱스에 있는지 찾기
# student1.append("홍길동"); # 홍길동 추가하기
# print(student1);
# student1.insert(0, "홍길동"); # insert 리스트에 인덱스 자리 변경 // 0 인덱스에 홍길동을 넣는다
# print(student1[0]);
# print(student1);
#
# # 삭제
# student1.remove("김진욱"); # 삭제
# print(student1);
#
# print(student1.pop(0)); # pop // 리스트 인덱스 자리에 있는거 출력 후, 리스트에서 삭제
# print(student1);

