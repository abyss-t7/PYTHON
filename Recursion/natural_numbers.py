def calc(k):
    if k==0:
        return 0
    
    return calc(k-1)+k
        

        
print(calc(4))