# def combinationSum(arr, target):
#     print(arr, target)
    

# arr = list(input('Enter list candidates : '))
# target = int(input("Enter target : "))

# combinationSum(arr, target)

def combinationSum(candidates, target):
    # Sort the candidates array (optional for optimization)
    candidates.sort()
    
    def backtrack(remain, combo, start):
        if remain == 0:
            # Found a valid combination
            result.append(list(combo))
            return
        elif remain < 0:
            # Exceeded the sum, stop further exploration
            return
        
        for i in range(start, len(candidates)):
            candidate = candidates[i]
            # Add the number to the current combination
            combo.append(candidate)
            # Explore further with the updated combination and remaining target
            backtrack(remain - candidate, combo, i)
            # Backtrack and remove the number from the current combination
            combo.pop()
    
    result = []
    backtrack(target, [], 0)
    return result

# Example usage
candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
