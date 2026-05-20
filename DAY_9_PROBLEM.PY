import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def calculatetotalhours(v,h) :
            totalhours = 0
            for bananas in v :
                totalhours += math.ceil(bananas / h)
            return totalhours
        def minimumrate(v,h):
            low , high = 1 , max(piles)
            while low <= high :
                mid = (low + high ) // 2
                totalhours = calculatetotalhours(v,mid)
                if totalhours <= h :
                    high = mid - 1
                else :
                    low = mid + 1
            return low

        return minimumrate(piles,h)
                
        