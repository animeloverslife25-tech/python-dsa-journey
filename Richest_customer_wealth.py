class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        max_wealth=0

        for customer in accounts:
            current_wealth=sum(customer)
            max_wealth=max(current_wealth,max_wealth)
        
        return max_wealth