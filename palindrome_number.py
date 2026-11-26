class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        original = x
        result = 0
        
        while x > 0:
            ld = x % 10
            result = (result * 10) + ld
            x = x // 10
            
        return original == result