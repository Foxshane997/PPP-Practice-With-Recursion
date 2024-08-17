# Recursive Reverse Function

def recursive_reverse(s):
    
# Base case set to 1
    if len(s) <= 1:
        return s
    
# Recursive to reverse order of string letters
    return recursive_reverse(s[1:]) + s[0]

print(recursive_reverse("Hello"))
print(recursive_reverse("Shane"))