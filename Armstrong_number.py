class Solution(object):
    def isArmstrong(self, n):
        """
        :type n: int
        :rtype: bool
        """
        k=len(str(n))
        total=0
        num=n
        while n>0:
            lst=num%10
            total=total+(lst**k)
            num=num//10

        return total==n

