out = open("./output/food.out", "w")
with open("./input/food.in", "r") as file:

    # taking input
    T = int(file.readline())
    for t in range(T):
        distributed = 0
        n, limit = map(int, file.readline().strip().split())
        A = list(map(int, file.readline().split()))
        A.sort()

        while(A != []):
            A = list(x for x in A if x != 0)

            for i in range(min(len(A), limit)):
                A.pop(0)
                distributed += 1

            A = list(x-1 for x in A)
        out.write(str(distributed)+'\n')
