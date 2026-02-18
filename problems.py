num=int(input("Enter the first number"))
if (num % 2)==0:
    print("It is even no")
else:
    print("It is odd no")
if num>0:
        print("Positive")
elif num==0:
        print("Zero")
else:
        print("Negative")
factorial=1
if num < 0:
    print("Sorry,no factorial for negative no")
elif num==0:
    print("The factorial of no is 1")
else:
    for i in range(1,num+1):
     factorial=factorial*i
    print("The factorial of",num,"is",factorial) 