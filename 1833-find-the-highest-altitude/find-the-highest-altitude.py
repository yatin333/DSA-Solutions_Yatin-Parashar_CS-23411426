class Solution:
    def largestAltitude(self, gain):
        cur = ans = 0

        for x in gain:
            cur += x
            ans = max(ans, cur)

        return ans