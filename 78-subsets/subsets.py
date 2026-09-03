class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(start, current_path):
           
            res.append(list(current_path))
            
            for i in range(start, len(nums)):
                
                current_path.append(nums[i])
                
                backtrack(i + 1, current_path)
               
                current_path.pop()
                
        backtrack(0, [])
        return res