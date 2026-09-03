class Solution:
    def construct2DArray(self, original, m, n):
        if len(original) != m * n:
            return []

        return [original[i:i+n] for i in range(0, len(original), n)]