def is_prime(num):
    
    if num == 1:
        return False
    if num == 2:
        return True
    if num == 3:
        return True
    if num % 2 == 0:
        return False
    
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False

        i += 1
    
    return True

def task58():
    
    cnt = 0
    for i in xrange(3, 1500000, 2):
       
        i1 = i - 1
        f = (i - 2) ** 2 + i1
        s = f + i1
        t = s + i1

        if is_prime(f):
            cnt += 1
        
        if is_prime(s): 
            cnt += 1
        
        if is_prime(t):
            cnt += 1
        
        if cnt * 10 < (2 * i - 1):
            print "Edge is ", i
            break

if __name__ == "__main__":
    task58()
