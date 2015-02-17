class PyRationalException(Exception):
    pass

def cached(func):
    class InternalCache:
        def __init__(self):
            self.cache_dict = {}

    ic = InternalCache()

    def decorated(slf, a, b):
        if ic.cache_dict.has_key((a, b)):
            return ic.cache_dict[(a, b)]
        
        result = func(slf, a, b)
        ic.cache_dict[(a, b)] = result
        ic.cache_dict[(b, a)] = result
        return result

    return decorated

class PyRational(object):

    def __init__(self, numerator, denominator=1):

        if denominator == 0:
            raise PyRationalException("Divison by zero!")

        if denominator < 0 and numerator > 0:
            numerator *= -1
            denominator *= -1

        gcd = self._gcd(numerator, denominator)
        self.numerator = numerator / gcd
        self.denominator = denominator / gcd

    def __str__(self):
        return "%s / %s" % (self.numerator, self.denominator)

    def _gcd(self, a, b):
        return self._gcd_eucl(a, b)
    
    def _gcd_bin(self, a, b):

        result = 1

        while True:

            if a == b:
                result *= a
                break

            if a == 0 or b == 0:
                result *= (a + b)
                break
        
            if a % 2 == 0 and b % 2 == 0:
                result *= 2
                a /= 2
                b /= 2
            elif a % 2 == 0:
                a /= 2
            elif b % 2 == 0:
                b /= 2
            elif a > b:
                a = (a - b) / 2
            else:
                b = (b - a) / 2

        return result

    @cached
    def _gcd_eucl(self, a, b):

        if a == 0:
            return b
        if b == 0:
            return a
        
        return self._gcd_eucl(b, a % b)
    
    def __gt__(self, rational):
        return self.numerator * rational.denominator > self.denominator * rational.numerator

    def __add__(self, rational):
        
        d_gcd = self._gcd(self.denominator, rational.denominator)
        l_factor = rational.denominator / d_gcd
        r_factor = self.denominator / d_gcd
        numerator = self.numerator * l_factor + rational.numerator * r_factor
        denominator = l_factor * d_gcd * r_factor

        return PyRational(numerator, denominator)

    def __sub__(self, rational):
        return self + PyRational(rational.numerator * -1, rational.denominator)
    
    def __mul__(self, rational):
        return PyRational(self.numerator * rational.numerator, self.denominator * rational.denominator)

    def __div__(self, rational):
        return self * PyRational(rational.denominator, rational.numerator)


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

One = PyRational(1)

def get_fraction(lst, depth):

    ext_mul = 0
    if depth > len(lst) - 1:
        ext_mul = depth / (len(lst) - 1)
    
    ext_lst = lst + lst[1:] * ext_mul

    result = PyRational(ext_lst[depth])
    for element in ext_lst[:depth][-1::-1]:
        result = One / result + PyRational(element)

    return result

def get_root(num, lst):

    depth = 1
    while True:
        fraction = get_fraction(lst, depth)
        if fraction.numerator ** 2 - num * (fraction.denominator ** 2) == 1:
            return (fraction.numerator, fraction.denominator)
        depth += 1

def task66():
    
    squares = [i * i for i in xrange(1, 1001)]
    result = -1
    mx = -1
    for num in xrange(1, 1001):
        if not num in squares:
            lst = list_repr(num, squares) 
            (x, y) = get_root(num, lst)
            if x > mx:
                mx = x
                result = num
    
    print "Result is ", result

if __name__ == "__main__":
    task66()
