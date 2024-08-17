# Recursive Palindrome

def palindrome(s):

# Removing the spacing & changes to lowercase
    s = s.replace(" ", "").lower()

    # Base case
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    
    # Recursive
    return palindrome(s[1:-1])

print(palindrome("Race car"))  # Output should be True.
print(palindrome("Hello"))    # Output should be False.
print(palindrome("A man a plan a canal Panama"))  # Output should be True.