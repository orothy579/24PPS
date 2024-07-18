def find_nges(N, A):
    result = [-1] * N  # 결과를 저장할 리스트를 -1로 초기화
    stack = []  # 스택 초기화

    for i in range(N):
        # 스택이 비어있지 않고, 현재 원소가 스택의 꼭대기 원소보다 크면
        while stack and A[stack[-1]] < A[i]:
            index = stack.pop()  # 스택의 꼭대기 원소를 pop
            result[index] = A[i]  # 그 인덱스에 대한 오큰수를 현재 원소로 설정
        stack.append(i)  # 현재 인덱스를 스택에 추가

    return result

# 입력 받기
N = int(input().strip())
A = list(map(int, input().strip().split()))

# 오큰수 구하기
result = find_nges(N, A)

# 결과 출력
print(" ".join(map(str, result)))