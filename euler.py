import math

def cached(func):
    class InternalCache:
        def __init__(self):
            self.cache_dict = {}

    ic = InternalCache()

    def decorated(num):
        if ic.cache_dict.has_key(num):
            return ic.cache_dict[num]
        
        result = func(num)
        ic.cache_dict[num] = result
        return result

    return decorated

@cached
def simple_factorization(num):

    result = []
    square = math.sqrt(num) + 1
    factor = 2
    while num > 1:
        while num % factor == 0:
            result.append(factor)
            num /= factor

        factor += 1
        if factor > square:
            if num > 1:
                result.append(num)
            break
   
    return result

def sorted_lists_deduction(first, second):
    f_index = 0
    s_index = 0
    f_len = len(first)
    s_len = len(second)
    result = []
    while True:
        while f_index < f_len and s_index < s_len and first[f_index] < second[s_index]:
            result.append(first[f_index])
            f_index += 1
        
        while f_index < f_len and s_index < s_len and first[f_index] == second[s_index]:
            f_index += 1
            s_index += 1

        while f_index < f_len and s_index < s_len and first[f_index] > second[s_index]:
            s_index += 1

        if f_index == f_len:    
            break

        if s_index == s_len:
            for i in xrange(f_index, f_len):
                result.append(first[i])
            break

    return result

def task53():
    @cached
    def factorial(num):
        result = [1]
        for i in xrange(2, num + 1):
            result += simple_factorization(i)

        return sorted(result)

    cnt = 0

    for n in xrange(1, 101):
        for r in xrange(0, n + 1):
            numerator = factorial(n)
            denominator = sorted(factorial(r) + factorial(n - r))
            light_num = sorted_lists_deduction(numerator, denominator)
            light_den = sorted_lists_deduction(denominator, numerator)
            num = 1
            for i in xrange(len(light_num)):
                num *= light_num[i]
            den = 1
            for i in xrange(len(light_den)):
                den *= light_den[i]

            result = num / den
            if result > 1000000:
                cnt += 1

    print cnt

if __name__ == "__main__":
    task53()
