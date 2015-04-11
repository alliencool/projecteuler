def cached(func):

    internal_cache = {}

    def decorated(num, biggest):
        if internal_cache.has_key((num, biggest)):
            return internal_cache[(num, biggest)]

        result = func(num, biggest)
        internal_cache[(num, biggest)] = result
        return result
    
    return decorated

@cached
def amnt_of_sums(num, biggest):
    if num <= 1:
        return 1
    #sm = 0
    sm = reduce(lambda sm, i: sm + amnt_of_sums(num - i, i), xrange(1, min(num, biggest) + 1), 0)
    #for i in xrange(1, min(num, biggest) + 1):
    #    sm += amnt_of_sums(num - i, i)
    return sm

if __name__ == "__main__":

    print amnt_of_sums(2, 1)
    print amnt_of_sums(3, 2)
    print amnt_of_sums(4, 3)
    print amnt_of_sums(5, 4)
    print amnt_of_sums(100, 99)
