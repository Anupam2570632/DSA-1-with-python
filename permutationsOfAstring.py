def permutation(s):
    
    # base case if length of the string is 0 then return a empty list
    if len(s) == 0 :
        return []
    
    # base case is length is 1 the return a list containing the character
    if len(s) == 1 :
        return [s]
    
    # list for collecting the permutations
    permutations = []
    
    for i in range(len(s)):
        
        current_char = s[i]

        remaining_string = s[:i] + s[i + 1:]
        
        print(f'for loop 1 - {i}')
        val = permutation(remaining_string)
        print(f'permutation {val}')
        for perm in permutation(remaining_string):
            print(f'perm - {perm}')
            print(f'current char - {current_char}')
            print(f'perm concat-----{current_char + perm}')
            permutations.append(current_char + perm)
            print(f'list --{permutations}')    
    
    
    return permutations
    
    
input_string = "abc"
output = permutation(input_string)
print(output)