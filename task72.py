import time

def eratosthene(num):
    
    result = [None for i in range(num + 1)]
    
    result[0] = {1: 1}
    result[1] = {1: 1}
    
    for i in xrange(2, num + 1):
        if i * 2 > num:
            for j in xrange(i, num + 1):
                if result[j] == None:
                    result[j] = {j:1}
            break
        if result[i] == None:
            result[i] = {i : 1}
            for j in xrange(i * 2, num + 1, i):
                pwr = 0
                number = j
                while number % i == 0:
                    number = number / i
                    pwr += 1
                
                if result[j] == None:    
                    result[j] = {i : pwr}
                else:
                    result[j][i] = pwr
    
    return result

if __name__ == "__main__":
    
    rng = 1000000
    
    time.clock()
    
    factors = eratosthene(rng * 10)
    
    result = 0
    for i in xrange(2, rng + 1):
        d = factors[i]

        euler = reduce(lambda res, f: res * (f ** d[f] - f ** (d[f] - 1)), d.keys(), 1)
        result += euler

    print result, "Time to solve:", time.clock()
