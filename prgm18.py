e,f=map(int,input().split())
for value in range(e,f):
  temp=value
  sum=0
  while(temp>0):
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
  if(sum==value):
    print(value)
