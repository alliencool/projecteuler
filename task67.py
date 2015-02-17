import sys

if __name__ == "__main__":
    result = []
    with open(sys.argv[1]) as fd:
        for line in fd:
            lst = [int(i) for i in line.split(" ")]
            new_result = [0] * len(lst)
            
            if len(result) == 0:
                result = lst
                continue

            for i in xrange(len(result)):
                new_result[i] = result[i] + lst[i]
            
            new_result[-1] = result[-1] + lst[-1]

            for i in xrange(len(result)):
                if new_result[i + 1] < (result[i] + lst[i + 1]):
                    new_result[i + 1] = result[i] + lst[i + 1]

            result = new_result

    print sorted(result)[-1]
