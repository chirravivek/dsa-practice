class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def find_days(weights,cap) :
            days = 1
            load = 0
            for w in weights :
                if load + w > cap :
                    days += 1
                    load = w
                else :
                    load += w
            return days
        
        
        low = max(weights)
        high = sum(weights)
        while low <= high :
            mid = (low + high ) // 2
            if find_days(weights,mid) <= days :
                ans = mid
                high = mid -1 
            else :
                low = mid + 1
        return ans
