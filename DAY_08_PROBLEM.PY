# Binary Search - nth Power Problems

def power(number, n):
    ans = 1.0
    for i in range(n):
        ans = ans * number
    return ans

def get_nth_root(n, m):
    low = 1
    high = m
    eps = 1e-6
    while (high - low) > eps:
        mid = (low + high) / 2.0
        if power(mid, n) < m:
            low = mid
        else:
            high = mid
    return low

n = int(input())
m = int(input())
print(get_nth_root(n, m))
print(m ** (1/n))