# All True  Iterable Function

def all_true(iterable):
    return all(iterable)

# This will output as true as everything we are passing in this option is true
print(all_true([True, True, True]))

# Due to it checking of everything we are passing is true this option will output as false
print(all_true([True, False, True])) 