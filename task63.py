def get_digits(num):


    result = []
    ind = 1

    while True:

        s_number = str(ind ** num)
        if len(s_number) > num:
            break

        if len(s_number) == num:
            result.append(ind ** num)

        ind += 1

    return result

def task63():

    print sum([len(get_digits(x)) for x in xrange(1, 1000)])

if __name__ == "__main__":
    task63()
