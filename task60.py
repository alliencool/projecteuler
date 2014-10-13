import time
def eratosthen(rng):
    flags = [1 for i in xrange(rng)]
    flags[0] = 0
    flags[1] = 0
    for i in xrange(2, rng):
        if flags[i]:
            for j in xrange(i * i, rng, i):
                flags[j] = 0
    
    return [i for i in xrange(rng) if flags[i]]

def dict_incr(dictionary, key):
    if dictionary.has_key(key):
        dictionary[key] += 1
    else:
        dictionary[key] = 1

def task60():
    stt = time.time()
    primes = eratosthen(100000000)
    primes_st = [str(prime) for prime in primes]
    primes_s = set(primes)
    primes_l = len(primes)

    primes_d = {prime:{} for prime in primes}
    print "Time to generate prime stuff is ", time.time() - stt, " seconds"
    stt = time.time()
    for i in xrange(primes_l):
        if len(primes_st[i]) > 1:
            for j in xrange(len(primes_st[i]) - 1):
                if primes_st[i][j + 1] == "0":
                    continue
                a = int(primes_st[i][:j + 1])
                b = int(primes_st[i][j + 1:])
                if a in primes_s and b in primes_s:
                    #dict_incr(primes_d[a], b)
                    #dict_incr(primes_d[b], a)
                    primes_d[a][b] = primes_d[a].get(b, 0) + 1
                    primes_d[b][a] = primes_d[b].get(a, 0) + 1
 
    def get_result(t_list, c_list, key, depth):
        if depth <= -1:
            print "Result is ", c_list + [key], ". Sum = ", sum(c_list + [key])
        else:
            for i in xrange(len(t_list) - depth):
                flag = True
                for c in c_list:
                    if primes_d[c].get(t_list[i], 0) < 2:
                        flag = False
                        break
                if flag:
                    get_result(t_list[i + 1:], c_list[:] + [t_list[i]], key, depth - 1)

    for key, d in primes_d.iteritems():
        result = []
        for prime, amount in d.iteritems():
            if prime > key and amount == 2:
                result.append(prime)
        
        result_l = len(result)
        if result_l < 4:
            continue
       
       
        get_result(result, [], key, 3)
    
    print "Time to solve the task itself is ", time.time() - stt, " seconds"
        
if __name__ == "__main__":
    task60()
