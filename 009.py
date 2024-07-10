#  ACGT 순서 맞추는 거 중요! 입력이 이 순서에 맞게 들어오기 때문에!
checklist = [0] * 4
mylist = [0] * 4
checking = 0

def mylist_add(c):
    global checklist, mylist, checking
    if c == 'A':
        mylist[0] += 1
        if mylist[0] == checklist[0]:
            checking += 1
    elif c == 'C':
        mylist[1] += 1
        if mylist[1] == checklist[1]:
            checking += 1
    elif c == 'G':
        mylist[2] += 1
        if mylist[2] == checklist[2]:
            checking += 1
    elif c == 'T':
        mylist[3] += 1
        if mylist[3] == checklist[3]:
            checking += 1

def mylist_remove(c):
    global checklist, mylist, checking
    if c == 'A':
        if mylist[0] == checklist[0]:
            checking -= 1
        mylist[0] -= 1
    elif c == 'C':
        if mylist[1] == checklist[1]:
            checking -= 1
        mylist[1] -= 1
    elif c == 'G':
        if mylist[2] == checklist[2]:
            checking -= 1
        mylist[2] -= 1
    elif c == 'T':
        if mylist[3] == checklist[3]:
            checking -= 1
        mylist[3] -= 1

s, p = map(int, input().split())
a = list(input())
checklist = list(map(int, input().split()))
result = 0

# 초기 설정: checklist 값이 0인 경우 checking을 증가
for i in range(4):
    if checklist[i] == 0:
        checking += 1

# 처음 p개의 문자에 대해 mylist를 설정하고 checking 값을 확인
for i in range(p):
    mylist_add(a[i])

# 모든 checklist 조건이 충족되면 결과 증가
if checking == 4:
    result += 1

# 슬라이딩 윈도우를 사용하여 문자열을 검사
for i in range(p, s):
    j = i - p
    mylist_add(a[i])  # 새로운 문자를 추가
    mylist_remove(a[j])  # 오래된 문자를 제거
    if checking == 4:  # 모든 조건이 충족되는지 확인
        result += 1

print(result)

