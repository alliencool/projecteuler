def task62():

    INTERVAL = 10000
    AMOUNT = 5

    nums = range(INTERVAL)
    cubes = [i ** 3 for i in xrange(INTERVAL)]

    cubes_permutations = ["".join(sorted(str(i))) for i in cubes]

    permutation_map = {}

    for permutation in cubes_permutations:
        permutation_map[permutation] = permutation_map.get(permutation, 0) + 1

    result = -1

    for key, value in permutation_map.iteritems():
        if value == AMOUNT:
            if result == -1 or result > cubes[cubes_permutations.index(key)]:
                result = cubes[cubes_permutations.index(key)]

    print "Result: ", result

if __name__ == "__main__":
    task62()
