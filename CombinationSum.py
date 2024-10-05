def combinationSum(candidates, target):
    # Sort the candidates array (optional for optimization)
    candidates.sort()
    res = []
    
    def backtrack(i, cur, total):
        if total == target:
            # Found a valid combination
            res.append(cur.copy())
            return
        elif i >= len(candidates) or total > target:
            # Exceeded the sum, stop further exploration
            return
        
        cur.append(candidates[i])
        backtrack(i, cur, total + candidates[i])
        cur.pop()
        backtrack(i + 1 , cur, total)
    
    backtrack(0, [], 0)
    return res

# Example usage
candidates = [2, 3, 6, 7]
target = 8
print(combinationSum(candidates, target))
