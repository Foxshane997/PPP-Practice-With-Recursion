# Number within Range Function

def num_within(number, lower, upper):
    return lower <= number <= upper;

print(num_within(5, 1, 10))  # Output will be: True
print(num_within(15, 1, 10)) # Output will be: False

# This checking whether a number falls within a given range 
# means verifying if the number is greater than or equal to a specified lower bound and 
# less than or equal to a specified upper bound.
