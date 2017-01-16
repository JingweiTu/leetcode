
# O(n) time complexity. Linear space complexity.
# Pretty simple concept. Given two integers, we use xor to find the sum without all the carried
# 1s and then we use & to find the indices where we carry 1s (ie where we have m[i] == 1 and 
# n[i] == 1). We then left shift the number by 1 to carry the 1s to the left by one index.
def recursiveBinaryAddition(n,m):
    if (m == 0):
        return n
    else:
        return recursiveBinaryAddition(n^m, (n&m) << 1)

def iterativeBinaryAddition(n,m):
    while m != 0:
        n, m = n^m, (n&m) <<1
    return n

def multiplyBinary(n,m):
    prod = 0
    for i in range(m):
        prod = iterativeBinaryAddition(n,prod)
    return prod

#TODO 
def divideBinary(n,m):
    