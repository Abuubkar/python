import numpy as np
import random


def createMatrix(n):
    firstRow = random.sample(range(1, n+1), n)
    permutes = random.sample(range(1, n+1), n)
    return list(firstRow[i:]+firstRow[:i] for i in permutes)


test_cases = int(input().strip())

for case in range(test_cases):

    line = list(map(int, input().strip().split()))

    # TRACE
    k = line[1]
    result = list()

    # MATRIX N BY  N size
    N = line[0]

    count = 0
    trace = 0
    while count < (10000):
        array = np.array(createMatrix(N))
        # computing trace
        trace = rrow = rcol = 0
        for index in range(N):
            # calculating trace
            trace += array[index][index]

        if trace == k:
            print("Case #{}: POSSIBLE".format(case+1))
            for x in array:
                answer = ""
                for y in x:
                    answer += str(y) + " "
                print(answer.strip())
            break
        count += 1
    print(count)
    if trace != k:
        print("Case #{}: IMPOSSIBLE".format(case+1))
