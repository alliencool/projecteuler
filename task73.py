def gcd(a, b):

    while True:
    
        if a == 0 or b == 0:
            return max(a, b)

        a, b = b, a % b

if __name__ == "__main__":

    #rng = 1000000
    rng = 12000 
    res = 0
    for denominator in xrange(rng, 1, -1):
        
        if denominator == 2 or denominator == 3:
            continue

        numerator = denominator  / 3
        if numerator * 3 < denominator:
            numerator += 1
        while numerator * 2 < denominator:
            if gcd(numerator, denominator) == 1:
                res += 1
            numerator += 1

    print "Result:", res
