# Recursion Ascending Countdown

def ascent_count(x, i):
# Base case
    if i > x:
        return;

    print(i);

# Adding 1 to 1-i until it reaches 5-x
    ascent_count(x, i + 1)

# Counting up from 1-5
ascent_count(5, 1)