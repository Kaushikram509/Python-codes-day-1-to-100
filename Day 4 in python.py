#find whether the number is +ve even, -even, +ve odd, -ve odd (including 0 as positive even)
number = int(input("Enter the number: "))
if(number%2==0 and number >=0):
     print(number,"The number is positive even")
elif(number%2==0 and number<0):
     print(number,"The number is negative even")
elif(number%2!=0 and number>0):
     print(number,"The number is positive odd")
else:
     print(number,"The number is negative odd")



#find biggest among three numbers using map(int, input().split())
num1, num2, num3 = map(int, input("Enter the numbeers: ").split())
if(num1 > num2 and num1 > num3):
     print(num1,"is greater ")
elif(num2 > num3):
     print(num2,"is greater")
else:
     print(num3,"is greater")



#find whether the number is +ve even, -even, +ve odd, -ve odd (including 0 as positive even) using nested if
number = int(input("Enter the number: "))
if(number >= 0):
     if(number%2==0):
         print(number,"Number is positive even")
     else:
         print(number, "number is positive odd")
else:
     if(number%2==0):
         print(number, "number is negative even")
     else:
         print(number, "number is negative odd")



#find biggest among three numbers using map(int, input().split()) using nested if
 num1, num2, num3 = map(int, input("Enter the numbeers: ").split())
 if(num1 > num2):
     if(num1 > num3):
         print(num1,"is greater than",num2,"and",num3)
     else:
         print(num1,"is not greater than",num2,"and",num3)
 else:
     if(num2 > num3):
         print(num2,"is greater than",num3)
     else:
         print(num3,"is greater")
