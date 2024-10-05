def permutation(string, left, right):
    if left == right:
        print(''.join(string))
    else:
        for i in range(left, right + 1):
            
            print(string[left], string[i]);
            string[left], string[i] = string[i], string[left]
            print(string[left], string[i]);
         
            permutation(string, left + 1, right)
            
            string[left], string[i] = string[i], string[left]


input_string = 'abc'
string_list = list(input_string) 
print(string_list)
permutation(string_list, 0, len(input_string) - 1)
