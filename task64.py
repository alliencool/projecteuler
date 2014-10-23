def last_less(x, lst):
    result = -1
    for i in lst:
        if i <= x:
            result = i
        else:
            break

    return result
    
def gcd_eucl(a, b):

    if a == 0:
        return b
    if b == 0:
        return a
    
    return gcd_eucl(b, a % b)

def triple_gcd(a, b, c):

    gcd = gcd_eucl(a, b)
    gcd = gcd_eucl(gcd, c)

    if gcd != 1:
        a /= gcd
        b /= gcd
        c /= gcd

    return (a, b, c)

def list_repr(num, squares):
    
    result = []
    
    floor = int(last_less(num, squares) ** 0.5)
        
    a = 1
    b = 0
    c = 1
    
    cache = set()
    
    while True:
        if (a, b, c) in cache:
            break
         
        cache.add((a, b, c))
        mul = (a * floor + b) / c
        result.append(mul)
        
        b = b - mul * c

        a_new = a * c
        b_new = -1 * b * c
        c_new = a * a * num - b * b

        a, b, c = triple_gcd(a_new, b_new, c_new)
        
    return result

def task64():
    
    squares = [i * i for i in xrange(1, 101)]

    amount = 0

    for num in xrange(1, 10001):
        if not num in squares:
            lst = list_repr(num, squares) 
            if len(lst) % 2 == 0:
                amount += 1
    
    print "Result: ", amount

if __name__ == "__main__":
    task64()
