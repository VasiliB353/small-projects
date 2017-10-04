# Vasili B
# 4/18/2014

# Prime number sieve

def list_primes(low,high):
    nums = []
    for i in range(2,high+1):
        nums.append(i)
    for x in nums:
        for n in nums:
            if float(n)/float(x) == n//x and n != x:
                nums.remove(n)
    return nums

if __name__ == '__main__':
    print list_primes(1,100)