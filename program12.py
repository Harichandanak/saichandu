e=int(input(" ")
rev1=0
temp1=e
while(e>0):
  val1=e%10
  rev1=rev1*10+val1
  e=e//10
if(temp1==rev1):
  print("yes")
else:
  print("no")
