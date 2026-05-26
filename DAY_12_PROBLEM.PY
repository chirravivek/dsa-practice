from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            # How many numbers are missing before arr[mid]?
            # If no gaps existed, arr[mid] should equal (mid + 1)
            # Difference = total missing numbers upto this point
            missing = arr[mid] - (mid + 1)

            if missing < k:
                low = mid + 1  
            else:
                high = mid - 1  

        # low + k gives the k-th missing number
        return low + k

