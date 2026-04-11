class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #since it has to do with repititions using a hashmap would be the best 
        #because we can store the value and how many times it appears
        count = {}
        res, maxCount = 0, 0 
        #res is like the candidate for being theh result 

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)
        return res
        