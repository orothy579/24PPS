import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
count = 0

a = list(map(int, input().split()))
i = 0
j = n-1

a.sort()

while i < j:
  if a[i] + a[j] < m:
    i +=1
  elif a[i] + a[j] > m:
    j -=1
  else:
    count +=1
    i +=1
    j -=1

print(count)

