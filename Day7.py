#find sum of even numbers between the range n and m
'''n = int(input("Enter a value: "))
m = int(input("Enter a value: "))
total = 0
for i in range(n,m):
    if n%2==0:
        total=total+n
    n+=1
print(total)'''
#len of the number
'''n = 2568979
count=0
while n>0:
    n//=10
    count+=1
print(count)'''
#find the number is palidrom or not
'''n=121
tem=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n//=10
print(rev)
if tem==rev:
    print("palidrom")
else:
    print("not palidrom")'''

#find the length of the number
'''n = int(input("Enter a value: "))
count = 0
while n>0:
    n//=10
    count+=1
print(count)'''

#reverse a number
'''n=int(input("Enter a number: "))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n//=10
print(rev)'''

#number is perfect or not
'''n = int(input("Enter a number: "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print("Perfect number")
else:
    print("Not a perfect number")'''
