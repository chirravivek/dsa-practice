give me the bot cods in at a time

3:21 pm
Aggressive Cows — Both Codes
1. Linear Search (Brute Force)
python
def can_place(arr, dist, cows):
    count = 1
    last = arr[0]

    for i in range(1, len(arr)):
        if arr[i] - last >= dist:
            count += 1
            last = arr[i]

    if count >= cows:
        return True
    return False


def aggressive_cows_linear(arr, cows):
    arr.sort()
    n = len(arr)

    ans = 0

    for dist in range(1, arr[n-1] - arr[0] + 1):
        if can_place(arr, dist, cows):
            ans = dist        # works, keep going
        else:
            break             # fails, stop

    return ans


# Test
arr = [0, 3, 4, 7, 9, 10]
cows = 4
print(aggressive_cows_linear(arr, cows))  # Output: 3
TC = O(n × (max-min)) | SC = O(1)

2. Binary Search (Optimal)
python
def can_place(arr, dist, cows):
    count = 1
    last = arr[0]

    for i in range(1, len(arr)):
        if arr[i] - last >= dist:
            count += 1
            last = arr[i]

    if count >= cows:
        return True
    return False


def aggressive_cows_binary(arr, cows):
    arr.sort()
    n = len(arr)

    low = 1                    # minimum possible distance
    high = arr[n-1] - arr[0]  # maximum possible distance
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if can_place(arr, mid, cows):
            ans = mid          # works, try larger
            low = mid + 1
        else:
            high = mid - 1     # too large, try smaller

    return ans


# Test
arr = [0, 3, 4, 7, 9, 10]
cows = 4
print(aggressive_cows_binary(arr, cows))  # Output: 3
TC = O(n × log(max-min)) | SC = O(1)