class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        left = 0
        right = -1

        str_length = len(s)

        if str_length == 0:
            return True

        count = 0

        while count < str_length // 2:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
                count +=1
        
        return True