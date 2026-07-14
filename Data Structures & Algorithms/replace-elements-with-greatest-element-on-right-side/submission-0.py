#i loops through the entire array
#k is at 0 
#check is value of k is greater than value at i re
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            maximum = max(arr[i+1:], default=-1)
            arr[i] = maximum
    
        return arr
    