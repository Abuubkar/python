def findCombinationsUtil(arr, index, num,
                         reducedNum):
    # Base condition
    if (reducedNum < 0):
        return
    if (reducedNum == 0):

        if index == N:
            result.append(arr[0:index])
            # for i in range(index):
            #     print(arr[i], end=" ")
            # print("")
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


# TRACE
n = 100
result = list()
index = 0
# MATRIX N BY  N size
N = 20

findCombinations(n)
print(result)
