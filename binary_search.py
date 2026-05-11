LEETCODE 34 QUESTION :

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def lower_bond(nums,n,target) :
            low = 0
            high = n-1
            ans = n
            while low <= high :
                mid = (low + high ) // 2
                if nums[mid] >= target :
                     ans = mid
                     high = mid - 1
                else :
                    low = mid + 1
            return ans 
        
        def upper_bond(nums,n,target):
            low = 0
            high = n-1
            ans = n
            while low <= high :
                mid  = (low + high) // 2
                if nums[mid] > target:
                    ans = mid
                    high = mid - 1 
            
                else :
                    low = mid + 1
            return ans 
        n = len(nums)
        first = lower_bond(nums,n,target)
        
        if first == n or nums[first] != target :
            return [-1,-1]
        
        last = upper_bond(nums,n,target) - 1
        return [first,last]



COUNTCOACURANCE:


def lower_bond(arr, n, x):
    n = len(arr)
    ans = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def upper_bond(arr, n, x):
    n = len(arr)
    ans = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def countOccurrences(arr, n, x):
    first = lower_bond(arr, n, x)

    if first == n or arr[first] != x:
        print("element not found")
        return 0

    last = upper_bond(arr, n, x) - 1
    count = last - first + 1
    print(f"first: {first}, last: {last}, count: {count}")
    return count

arr = [2, 4, 6, 8, 8, 8, 11, 13]
n = 8
x = 8
countOccurrences(arr, n, x)