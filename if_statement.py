# if and else statement 
a=20
b=40
if a>b:
    print("a is greater than b")
    print(a)
if a<b:
    print("b is greater than a ")
    print(b)
    
if a>b:
    print("a is greater than b ")
else:
    print("a is smaller then b")
    x= 5
    y= 4
    z= 7
    if (x>y & x>z):
        print("x is greatest value")
        print(x)
    elif ( y>x & y>z):
        print ("y is greatest value" )
        print(y)
    else:
        print("z is the largest")
        print(z)
        tup = (5,6,3,4,5,3,7,8,4,6,4,6,3,)
    if 2 in tup:
            print("3 is present in tuple")
    else:
        print('not found')
        # if else cindition for list 
li = [1,2,3,4,5,6,7]
if li[1]==2:
    li[1]=li[1]+50
    print(li)
    if li[3]==3:
        li[3]=li[3]+492
        print(li)
    else:
        li[3]=li[3]+900
        print(li)
        # if else condtion of dictniory
        d1 = {"a":1,"b":2,"c":3,"d":4,"e":5}
        if d1["b"]==2:
            d1["b"]=d1["b"]+399
        print(d1)           
        