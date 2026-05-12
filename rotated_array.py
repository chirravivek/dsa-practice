# ============================================
# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium | Time: O(log n) | Space: O(1)
# ============================================

def search_rotated(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:  # left half sorted
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:                        # right half sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


# ============================================
# 81. Search in Rotated Sorted Array II
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# Difficulty: Medium | Time: O(log n) avg, O(n) worst | Space: O(1)
# Key difference: duplicates allowed — need extra case when
# nums[low] == nums[mid] == nums[high]
# ============================================

def search_rotated_duplicates(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return True

        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
        elif nums[low] <= nums[mid]:  # left half sorted
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:                          # right half sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False


