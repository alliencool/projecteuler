def gcd(a, b):

    while True:
    
        if a == 0 or b == 0:
            return max(a, b)

        a, b = b, a % b

if __name__ == "__main__":

    result_n = 0
    result_d = 1
    rng = 1000000
    for denominator in xrange(rng, 1, -1):
        
        if denominator == 7:
            continue
        
        numerator = denominator * 3 / 7
        while gcd(numerator, denominator) != 1:
            numerator -= 1

        if numerator * result_d > result_n * denominator:
            result_n = numerator
            result_d = denominator

    print "Result:", result_n, "/", result_d
