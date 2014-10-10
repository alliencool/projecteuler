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

def task57():
    
    rational = PyRational(1)
    result = 0
    for i in xrange(1, 1001):

        rational = PyRational(1) + PyRational(1) / (rational + PyRational(1))
        if len(str(rational.numerator)) > len(str(rational.denominator)):
            result += 1
        
    print result

if __name__ == "__main__":
    task57()
