
input1 = int(input())
input2 = int(input())
sum = 0
tmp =0

for i in range(input1):
  tmp = input2 // pow(10,input1-i-1)
  sum += tmp
  input2 -= (tmp * pow(10,input1-i-1))

print(sum)
