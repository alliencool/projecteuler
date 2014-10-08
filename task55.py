def task55():

    def is_palindrome(line):
        return line == line[-1::-1]
    
    def is_lychrel(num, depth=None):
        CONDITION = 50
        if depth == None:
            depth = 0

        if depth > 0 and depth < CONDITION and is_palindrome(str(num)):
            return False

        if depth >= CONDITION:
            return True
        
        depth += 1
        return is_lychrel(num + int(str(num)[-1::-1]), depth)

    cnt = 0

    for i in xrange(1, 10000):
        if is_lychrel(i):
            cnt += 1

    print "Amount of Lychrel's numbers below 10000 is %s." % cnt


if __name__ == "__main__":
    task55()
