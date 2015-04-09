import math
import time

def gcd(a, b):

    while a != 0 and b != 0:
        a, b = b , a % b

    return max(a, b)

if __name__ == "__main__":

    RNG = 1500000

    time.clock()

    result = [0 for i in xrange(RNG + 1)]
    mx = int(((RNG) / 2) ** 0.5 + 1)
    for m in xrange(mx):
        for n in xrange(m - 1, 0, -1):
            if gcd(m, n) == 1 and (m - n) % 2 == 1:
                perimeter = 2 * m * (m + n)
                add = perimeter
                while perimeter <= RNG:
                    result[perimeter] += 1
                    perimeter += add

    print "Result:", sum((1 for i in result if i == 1))
    
    print "Time for solution with Euclid's formula:", time.clock()
