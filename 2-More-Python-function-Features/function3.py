# One True Any Iterable Function

def one_true(iterable):
    # Checks for "any" that happen to be or have one "true" passed in.
    return any(iterable)

# This will output as True as "any" is checking for any True that is passed in.
print(one_true([False, False, True]))

# This will output false due to it not passing in a "true".
print(one_true([False, False, False]))