"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here


def sumdiff(num_set):
    result = {}
    sum_num = {}
    diff_num = {}
    final = {}

    for num in num_set:
        result[num] = f(num)

    for key1 in result:
        for key2 in result:
            sum_num[key1, key2] = result[key1] + result[key2]

    for key1 in result:
        for key2 in result:

            if result[key1] > result[key2]:

                diff_num[key1, key2] = result[key1] - result[key2]

            else:
                diff_num[key2, key1] = result[key2] - result[key1]
    for key1 in sum_num:
        for key2 in diff_num:

            if sum_num[key1] == diff_num[key2]:
                final[key1 +
                      key2] = f"{result[key1[0]]} + {result[key1[1]]} = {result[key2[0]]} - {result[key2[1]]}"

    for key in final:
        print(
            f"f({key[0]}) + f({key[1]}) = f({key[2]}) - f({key[3]})    {final[key]}")


sumdiff(q)
