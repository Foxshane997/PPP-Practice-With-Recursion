# Multiply All function

def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(mult_list([2, 3, 4, 5]))
# Output should be 120