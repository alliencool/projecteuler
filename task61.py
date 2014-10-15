def get_digit_list(func, digit_count):

    result = []
    ind = 1
    num = 1
    s_num = "1"
    while len(s_num) <= digit_count:
        if len(s_num) == digit_count:
            result.append((num, ind))
        ind += 1 
        num = func(ind)
        s_num = str(num)

    return result

def get_result(numbers, candidates, depth, connected):

    if depth == -1:
        if connected[candidates[-1]].count(candidates[0]) > 0:
            print "Result : ", candidates, sum([c[0] for c in candidates])
    
    else:
        for number in numbers:
            flag = True
            for candidate in candidates:
                if candidate[2] == number[2] or candidate[1] == number[1]:
                    flag = False
                    break

            if flag:
                get_result(connected[number], candidates + [number], depth - 1, connected)

def task61():

    tria = lambda n: n * (n + 1) / 2
    squa = lambda n: n * n
    pent = lambda n: n * (3 * n - 1) / 2
    hexa = lambda n: n * (2 * n - 1)
    hept = lambda n: n * (5 * n - 3) / 2
    octa = lambda n: n * (3 * n - 2)

    numbers = []

    for func, ident in [(tria, 1), (squa, 2), (pent, 3), (hexa, 4), (hept, 5), (octa, 6)]:
        num_list = get_digit_list(func, 4)
        numbers = numbers + [(a, b, ident) for a, b in num_list]

    ntoi = {x:i for i, x in enumerate(numbers)}
    
    connected_with = {x:[] for x in numbers}
    for num1 in numbers:
        for num2 in numbers:
            if num1[2] != num2[2] and num1[1] != num2[1] and str(num1[0])[2:] == str(num2[0])[:2]:
                connected_with[num1].append(num2)

    get_result(numbers, [],  5, connected_with)

    

if __name__ == "__main__":
    task61()
