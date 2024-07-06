import sys
input = sys.stdin.readline

n, m = map(int, input().split())
count = 0

a = list(map(int, input().split()))
s = [0] * n
s[0] = a[0]

# 부분합 계산
for i in range(1,n):
    s[i] = s[i-1] + a[i]

# 나머지 개수 세기
remainder_count = [0] * m
remainder_count[0] = 1 #부분합이 없는 경우..

for i in range(n):
    remainder = s[i] % m
    count += remainder_count[remainder]
    remainder_count[remainder] += 1

print(count)
