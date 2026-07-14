class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = k = 0
        for index in range(len(nums)):
            if nums[index] == val:
                nums[index] = 0
                count += 1
        nums.sort(reverse=True)
        length = len(nums)
        k = length - count
        return k