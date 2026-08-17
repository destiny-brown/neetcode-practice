class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        right = -1
        while abs(right) < len(digits)+1:
            if digits[right] != 9:
                digits[right]= digits[right] + 1
                break
            else:
                digits[right] = 0
                right -= 1
        if digits[0] == 0:
            digits.insert(0,1)
        print(digits)
        return digits

 
                



        