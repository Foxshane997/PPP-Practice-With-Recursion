# Recursive Duplicate Function

# Base case for if empty or has only one letter.
def recursive_duplicate(s):

    if len(s) < 2:
        return s
    
# For removing adjacent duplicates
    result = []
    i = 0
    while i < len(s):
        if i == 0 or s[i] != s[i - 1]:
            result.append(s[i])
        i += 1

# Changing list back to a string
    new_s = ''.join(result)

# recursive if there are adjacent dupes
    if new_s == s:
        return new_s
    else:
        return recursive_duplicate(new_s)
    
print(recursive_duplicate("AABBCCDD"))  # Output should be: ABCD
