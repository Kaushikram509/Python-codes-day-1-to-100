#Types of Arguments
#subraction of two numbers
#1.postion arguments
def subraction(b,a):
    return b-a

a = int(input("A:"))
b = int(input("B:"))
print(subraction(b,a))


#2.keyword arguments
def sub(a,b):
    return a - b
n=int(input())
y=int(input())
print(sub(a = y,b = n))


#3.sum of two number
def add(a,b):
    return a+b
a = int(input())
b = int(input())
print(add(a,b))


# sum of three number
def add(a,b,c):
    return a+b+c
a=int(input())
b=int(input())
c=int(input())
print(add(a,b,c))

# sum of four number
def add(a,b,c,d):
    return a+b+c+d
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(add(a,b,c,d))


#multipilication of four number
def multi(a,b,c=0,d=0):
    return a*b*c*d
b1 = int(input())
b2 = int(input())
b3 = int(input())
b4 = int(input())
print(multi(b1,b2,b3,b4))
print(multi(b1,b2,b3))
print(multi(b1,b2))


#varible lenght postional arguments
#sum of four number
def add(x , *args):
    print(type(args))
    print(args)
    s = 0
    for num in args:
        s += num
    return s

print(add(1,2,3,4,5,6,7,8,9))


l=[1,2,3,4,5,6,7,10]
print(l[-1:-5:-1])
print(l[-1:-100:-1])
print(l[-5:3])


l1=[1,2,3]+[3]
print(l1)
