# Recursive Factorial Function

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1);
    
print(recursive_factorial(5)); # Should be output of 120
print(recursive_factorial(3)); # Should be output of 6
