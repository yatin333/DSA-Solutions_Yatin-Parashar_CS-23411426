class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        visited = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])  
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    
                    backtrack(path)
                    
                   
                    path.pop()
                    visited[i] = False

        backtrack([])
        return res