n=int(input("Enter the Value"))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("This is the reverse no",rev)
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
     print("The number is palendrom")
else:
    print("The number is not palendrom")
    