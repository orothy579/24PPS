import sys
input = sys.stdin.readline

# 리스트 크기, 쿼리 개수 입력 받기
n, q = map(int, input().split())
# 원본 리스트 초기화
a = [[0]*(n+1)]
# 구간 합 리스트 초기화
d = [[0]*(n+1) for _ in range(n+1)]

# 원본 리스트 입력
for i in range(n):
  #a.append([0] + [int(x) for x in input().split()])
  a.append([0] + list(map(int, input().split())))

# 구간 합 리스트 만들기
for i in range(1,n+1):
  for j in range(1,n+1):
    d[i][j] = d[i-1][j] + d[i][j-1] - d[i-1][j-1] + a[i][j]

for i in range(q):
  x1, y1, x2, y2 = map(int, input().split())
  result = d[x2][y2] - d[x2][y1-1] - d[x1-1][y2] + d[x1-1][y1-1]
  print(result)






