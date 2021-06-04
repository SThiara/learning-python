import math

def integer_square_root(k):
  return math.floor(math.sqrt(k))

def integer_square_root(k):
  if k == 0:
    return 0
def integer_square_root(k):
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1