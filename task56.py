def task56():

    def summ(num):
        return sum([int(i) for i in str(num)])

    result = 0
    for a in xrange(1, 100):
        for b in xrange(1, 100):
            sm = summ(a ** b)
            if sm > result:
                result = sm

    print result

if __name__ == "__main__":
    task56()
