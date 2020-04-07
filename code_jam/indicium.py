import random
import numpy as np


def findCombinationsUtil(arr, index, num,
                         reducedNum):
    # Base condition
    if (reducedNum < 0):
        return
    if (reducedNum == 0):

        if index == N:
            if max(arr[:N]) > N:
                return
            else:
                result.append(arr[:N])
        return
    prev = 1 if(index == 0) else arr[index - 1]
    for k in range(prev, num + 1):
        arr[index] = k
        findCombinationsUtil(arr, index + 1, num,
                             reducedNum - k)


def findCombinations(n):

    arr = [0] * n

    # find all combinations
    findCombinationsUtil(arr, 0, n, n)


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

    findCombinations(k)

    if len(result) == 0:
        print("Case #{}: IMPOSSIBLE".format(case+1))

    trace = 0
    count = 0
    while count < (N**2):
        array = createMatrix(N)
        trace = 0
        for index in range(N):
            # calculating trace
            trace += array[index][index]
        if trace == k:
            print("Case #{}: POSSIBLE".format(case+1))
            for x in array:
                for y in x:
                    print(y, end=" ")
                print()
            break
        count += 1
    if trace != k:
        print("Case #{}: IMPOSSIBLE".format(case+1))
