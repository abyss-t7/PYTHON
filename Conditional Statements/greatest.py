num1 = int(input("Enter a number 1 :"))
num2 = int(input("Enter a number 2 :"))
num3 = int(input("Enter a number 3 :"))

if (num1 > num2 and num1>num3):
    print("Greatest number is :",num1)
    
elif (num2 > num1 and num2>num3):
    print("Greatest number is :",num2)
    
elif (num3 > num2 and num3>num1):
    print("Greatest number is :",num3)

else:
    input("Invalid")
