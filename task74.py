import time

time.clock()

def factorial(n):
    
    return reduce(lambda result, next: result * next, xrange(2, n + 1), 1)

factorials = [factorial(i) for i in xrange(10)]

def list_repr(num):
    res = []
    if num == 0:
        res.append(0)
    while num:
        res.append(num % 10)
        num /= 10
    res.reverse()
    return res

list_nums = [list_repr(i) for i in xrange(10000000)]

def chain_len(num):

    num_set = set()
    num_set.add(num)
    while True:
        num = sum((factorials[ci] for ci in list_nums[num]))
        if not num in num_set:
            num_set.add(num)
        else:
            break
    return len(num_set)

if __name__ == "__main__":
    print "Time to precalculate:", time.clock()
    print "Result is:", sum((1 for i in xrange(1000000) if chain_len(i) == 60 )) 
    print "Time to solve:", time.clock()
