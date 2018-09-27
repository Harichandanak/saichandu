e,f=input().split()
e,f=int(e),int(f)
for i in range(e+1,f):
  g=0
  for j in range(1,i+1):
    if(i%j==0):
      g+=1
    else:
      if(g==2):
        print(i,end=' ')
