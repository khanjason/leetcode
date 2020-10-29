from functools import lru_cache

class Solution:
    def mincostTickets(self, days, costs):
        durations = [1, 7, 30]
        @lru_cache(None)
        def dp(n): 
            if n >=len(days): 
                return 0
            ans=float('inf')
            t=n
            for c, d in zip(costs, durations):
                while t<len(days) and days[t]<(days[n] + d):
                    t=t+1
                ans=min(ans, dp(t)+c)

            return ans

        return dp(0)
