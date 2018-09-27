g=int(input(" "))
temp=g
sum=0
while(g>0):
  rem=g%10
  sum=rem**3+sum
  g=g//10
if(temp==sum):
  print("yes")
else:
  print("no")
