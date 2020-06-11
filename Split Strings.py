def solution(s):
    if len(s) % 2 == 0:
        return [s[i:i + 2] for i in range(0, len(s), 2)]
    else:
        res = [s[i:i + 2] for i in range(0, len(s), 2)]
        res[-1] = res[-1] + "_"
        return res


if __name__ == '__main__':
    tests = (
        ("asdfadsf", ['as', 'df', 'ad', 'sf']),
        ("asdfads", ['as', 'df', 'ad', 's_']),
        ("", []),
        ("x", ["x_"]),
    )

    for inp, exp in tests:
        print(solution(inp), "->", exp)
