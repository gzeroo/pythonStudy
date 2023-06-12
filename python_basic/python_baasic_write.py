# ## 파일 읽고 쓰기 - 점프 투 파이썬 171p

## 파일 쓰기
# f = open("C:/Users/eovy/Downloads/test/새 파일.txt", 'w') # 파일 열기 / 파일 없으면 새로 파일 생성
# ## open(파일 이름(경로+파일 이름), 파일 열기 모드) // r - 읽기 모드 / w - 쓰기 모드(실행하면 이전 꺼 사라짐) : 덮어쓰기 / a - 추가 모드(파일의 마지막에 새로운 내용을 추가할 때 사용)
# data = "안녕하세요"
# f.write(data) # write 작성
# f.close() # 파일 닫기
#
#
f = open("C:/Users/eovy/Downloads/test/새 파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

## 파일 읽기
# f = open("C:/Users/eovy/Downloads/test/새 파일.txt", 'r')
#
# while 1:
#     line = f.readline() # 라인(줄) 별로 읽어옴
#     if not line:
#         break
#     print(line)
#
# f.close()

# f = open("C:/Users/eovy/Downloads/test/새 파일.txt", 'r')
# lines = f.readlines() # 모든 줄을 리스트로 가져옴
# for line in lines: ## 전체 리스트로 가져와서 line에 대입해서 가져왔음
#     print(line)
# f.close()

# f = open("C:/Users/eovy/Downloads/test/새 파일.txt", 'r')
# lines = f.read()
# print(lines)
#
# f.close()

## 글 추가하기!
# f = open("C:/Users/eovy/Downloads/test/새 파일.txt", 'a')
#
# for i in range(11, 21):
#     data = "%d 번째 줄입니다.\n" %i
#     f.write(data)
# f.close()
