def is_palindrome(lst):    
    left = 0
    right = len(lst) - 1
    
    while left < right:
        if lst[left] != lst[right]:
            return "Not Palindrome"
        left += 1
        right -= 1
    
    return "Palindrome"

palin1 = [1, 5, 6, 5, 1]
palin2 = [1, 2, 3, 4, 5]

print(is_palindrome(palin1))  # Palindrome
print(is_palindrome(palin2))  # Not Palindrome