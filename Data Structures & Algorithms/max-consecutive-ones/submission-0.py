class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = count = 0
        for num in nums:
            if num == 1:
                count += 1   
            else:
                maximum = max(maximum, count)
                count = 0    
        maximum = max(maximum, count)
        return maximum

        