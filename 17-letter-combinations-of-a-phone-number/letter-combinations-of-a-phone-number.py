class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        
        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index: int, current_path: list[str]):
            
            if index == len(digits):
                result.append("".join(current_path))
                return
            
           
            possible_letters = digit_to_letters[digits[index]]
            
            
            for letter in possible_letters:
                current_path.append(letter)
                backtrack(index + 1, current_path)
                current_path.pop()  
        
        backtrack(0, [])
        return result   