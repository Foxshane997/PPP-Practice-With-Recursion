# Recursive Power Of

def power_of(a, b):

# Base case
    if b == 0:
        return 1
    
    # recursive calculating the math
    return a * power_of(a, b - 1)

print(power_of(2,3))
print(power_of(5,0))
# 2 Cased where it is being invoked