test_cases = int(input().strip())

for case in range(test_cases):

    answer = ""
    # filling array
    input_string = input().strip()

    size = len(input_string)

    # char = input_string[0]
    i = 0
    prev = "0"
    char = input_string[i]
    while i < len(input_string):
        if char == '0':
            answer += char
        elif char != prev:
            diff = int(char) - int(prev)
            bracket = ""
            if diff > 0:
                for value in range(diff):
                    bracket += '('
            answer += bracket + char
        elif char == prev:
            answer += char

        prev = char
        i += 1
        if i < len(input_string):
            char = input_string[i]

        if char != prev:
            diff = int(prev) - int(char)
            bracket = ""
            if diff > 0:
                for value in range(diff):
                    bracket += ')'
            answer += bracket

        if i == len(input_string):
            if char != '0':
                diff = abs(int(char))
                bracket = ""
                if diff > 0:
                    for value in range(diff):
                        bracket += ')'
                answer += bracket
    print("Case #{}: {}".format(case+1, answer))
