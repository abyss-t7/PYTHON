num = (1,52,63,24,54,66,74,87,88,81,63,39,60)
x=int(input("Enter the number from the tuple to find its index :"))
i=0
while i<len(num):
    if(num[i]==x):
        print("Found at index :",i)
    i+=1
