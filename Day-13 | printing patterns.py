#printing starts
for i in range(5):
    for j in range(5):
        print('*',end=" ")
    print()


#printing numbers in colums
for i in range(5):
    for j in range(5):
        print(i+1,end=" ")
    print()


#printing numbers rows
for i in range(5):
    for j in range(5):
        print(j+1,end=" ")
    print()



'''*
* *
* * * 
* * * *'''
for i in range(5):
    for j in range(5):
        if i >= j:
            print("*",end = " ")
        else:
            print(" " ,end=" ")
    print()



#patterns
n=4
for i in range(n):
    for j in range(n):
        if i == 0 or i== n-1 or j==0 or j==n-1:
            print("*",end = " ")
        else:
            print(" ", end=" ")
    print()
