
test_cases = int(input().strip())
for case in range(test_cases):
    inputs = int(input().strip())  # taking number of schedules from user

    time_schedules = [0]*inputs  # initializing array of time schedules

    # taking all schedule from user
    for i in range(inputs):
        # seperating each time(string) and converting each time to (int) using map
        # and saving it in form of list (no int) to ensure time are seperated from other schedule
        time_schedules[i] = list(map(int, input().strip().split()))

    copy_schedules = time_schedules.copy()
    time_schedules = sorted(time_schedules)
    # print(time_schedules)

    # SOLUTION =>
    result = ""
    i = 0
    j = [0, 0]
    c = time_schedules[i].copy()
    copy_schedules[copy_schedules.index(time_schedules[i])] = "C"
    time_schedules.pop(i)
    result += "C"
    while time_schedules != []:
        if c[1] <= time_schedules[i][0]:
            c = time_schedules.copy()[i]
            copy_schedules[copy_schedules.index(time_schedules[i])] = "C"
            time_schedules.pop(i)
            result += "C"
        elif c[1] > time_schedules[i][0] and j[1] <= time_schedules[i][0]:
            j = time_schedules.copy()[i]
            copy_schedules[copy_schedules.index(time_schedules[i])] = "J"
            time_schedules.pop(i)
            result += "J"
        elif j[1] > time_schedules[i][0] and c[1] > time_schedules[i][0]:
            copy_schedules = "IMPOSSIBLE"
            result = "IMPOSSIBLE"
            break
    ans = ""
    for name in copy_schedules:
        ans += str(name)
    print("Case #{}: {}".format(case+1, ans))


"""

4
3
360 480
420 540
600 660
3
0 1440
1 3
2 4
5
99 150
1 100
100 301
2 5
150 250
2
0 720
720 1440

"""
