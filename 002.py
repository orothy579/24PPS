n = int(input())
s = list(map(int, input().split()))
m = max(s)
sum =0

for i in s :
  sum += i/m *100

print(sum/n)