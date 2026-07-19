"""Recursion is when a function calls itself."""
def kill(num):
    if num==0:
        return 
    print(num)
    kill(num-1) 
    print("Inside Memory [behind the scene]")
    """ it become 5-1=4, which is kill(4) and then it will become 4-1=3, which is kill(3)
    and then it will become 3-1=2, which is kill(2) and then it will become 2-1=1, which is kill(1) 
    and then it will become 1-1=0, which is kill(0) and then it will return 0 and the recursion will
    stop."""
    
kill(7)


"""Every recursion needs TWO things:
1. Base Case (Stopping Condition) i.e. 
if num == 0:
    return

2. Recursive Case
kill(num-1)
This tells recursion how to continue."""

