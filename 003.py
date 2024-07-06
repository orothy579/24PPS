import sys
input = sys.stdin.readline # 대규모 입력 받는데에 더 빠르다.

# 첫 번째 줄에서 n과 q를 입력받습니다.
n, q = map(int, input().split())

# 두 번째 줄에서 길이 n의 배열 a를 입력받습니다.
a = list(map(int, input().split()))

# 누적 합 배열을 계산합니다.
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i - 1]

results = []

for _ in range(q):
    l, r = map(int, input().split())
    result = s[r] - s[l - 1]
    results.append(result)

for result in results:
    print(result)
