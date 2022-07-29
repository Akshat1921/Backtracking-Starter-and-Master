# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

nums = [1,2,3]

def subsets(nums):
    curr = []
    res = []
    n = len(nums)
    def rec(i):
        if i>=n:
            res.append(curr[:])
            return 
        curr.append(nums[i])
        rec(i+1)
        curr.pop()
        rec(i+1)
    rec(0)
    return res

print(subsets(nums))
    