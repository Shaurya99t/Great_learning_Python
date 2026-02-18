def hello():
    print("Hello World")
print(hello)
def add10(x):
 return x+10    
print(add10(20))
def even_odd(x):
 if x%2==0:
        print(x,"Is even")
 else:
        print(x,"Is odd")
print(even_odd(7))
g=lambda x: x*x*x
print(g(88))
# the number is odd aur not divisible by 2
li=[7,8,4,8,22,67,97,43,78,33,56,57]
final_list=list(filter(lambda x:(x%2 !=0),li))
print(final_list)
final_list=list(map(lambda x: x*2,li))
print(final_list)
from functools import reduce
sum = reduce((lambda x,y :x+y),li)
print(sum)