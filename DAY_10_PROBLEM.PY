class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def possible(day):
            bouquets = 0
            consecutive = 0
            for bloom in bloomDay:
                if bloom <= day:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0
            return bouquets >= m

        n = len(bloomDay)

        if m * k > n:
            return -1

        low = min(bloomDay)
        high = max(bloomDay)
        answer = high

        while low <= high:
            mid = (low + high) // 2
            if possible(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer
