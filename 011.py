n = int(input())
nlist = [0] *n # 수열 숫자

for i in range(n):
    nlist[i] = int(input())

stack = []
result = ""
current = 1

for number in nlist:
    while current <= number:
        stack.append(current)
        result += '+\n'
        current += 1
    if stack[-1] == number:
        stack.pop()
        result += '-\n'
    else:
        print('NO')
        break
else: # for 루프가 break 없이 정상적으로 완료되었을 때 실행
    print(result)
