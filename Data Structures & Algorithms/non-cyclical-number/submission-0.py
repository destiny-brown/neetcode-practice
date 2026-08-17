class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            thousand = n // 1000 % 10
            hundred = n // 100 % 10
            tens = n // 10 % 10 
            unit = n // 1 % 10
            n = pow(thousand, 2) + pow(hundred, 2) + pow(tens, 2) + pow(unit, 2)
        
        if n != 1:
            return False
        else:
            return True