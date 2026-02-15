i=1
while i<=10:
    print(i)
    i+=1
    i=int(input("Enter the first value"))
    n=int(input("Enter the gap you want"))
    p=int(input("Enter the last no you want"))
    while i<=p:
        print(i)
        i=i+n
    while i<=10:
             print("This is table of",n)
             print(n,"*",i,"=",n*i)
             i+=1