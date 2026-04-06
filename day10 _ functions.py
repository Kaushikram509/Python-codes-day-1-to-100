#function defination
def even_odd(n):
    if n%2==0:
        return 'even'
    else:
        return'odd'
#function calling
n = int(input("Value:"))
re=even_odd(n)
print(re)

#even or odd
#function defination
def even_odd(n):
    if n%2==0:
        print('even')
    else:
        print('odd')
#function calling
n = int(input("Value:"))
re=even_odd(n)
print(re)

#sum of list
# functio defination 
def sum_of_list(li):
    su = 0
    for i in li:
        su+=i
    return su

#function calling
li = [1,2,3,4,5]
su=sum_of_list(li)
print(su)


#calculator buliding like addtion,mulipication,subracton and division
def calculator(a,b):
    if op == '+':
        return a+b
    elif op == '-':
        return b-a
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b

n=int(input("Enter a value: "))
s=int(input("Enter b value: "))
op = input('operator: ')
print(calculator(n,s))
        
