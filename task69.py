
def eratosthene(num):

    result = [0 for i in range(num + 1)]
    
    result[0] = 1
    result[1] = 1
    
    for i in range(num + 1):
        if result[i] == 0:
            sqr = i ** 2
            if sqr > num + 1:
                break
            for j in range(sqr, num + 1, i):
                result[j] = 1
    
    return [i for i in range(num + 1) if (result[i] == 0)]
    
def factor(num, excl=None):
    if excl == None:
        excl = []
        
    if num in excl:
        return [(num, 1)]
    
    result = []
    
    i = 2
    while i * i <= num:
        
        if num % i == 0:
            power = 0
            while num % i == 0:
                num = int(num / i)
                power += 1
            result.append((i, power))
        
        if num in excl:
            result.append((num, 1))
            num = 1
        i += 1
    
    if num > 1:
        result.append((num, 1))
                
    return result
    
def euler(num, excl=None):
    
    if excl == None:
        excl = []
    
    if num == 1:
        return 1
    
    factors = factor(num, excl)
    
    result = 1
    for f in factors:
        result *= (f[0] ** f[1] - f[0] ** (f[1] - 1))
       
    return result

if __name__ == "__main__":

    rng = 1000000
    primes = set(eratosthene(rng))
    mx = 0
    n = 0
    for i in range(rng + 1):
        f = euler(i, primes)
        f = i / f
        if f > mx:
            mx = f
            n = i
    print("Result is ", n)    
