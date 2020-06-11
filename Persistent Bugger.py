def persistence(n):
    digits = [int(d) for d in str(n)]
    ctr = 0
    while len(digits) > 1:
        ctr += 1
        sum = 1
        for d in digits:
            sum *= d
        digits = [int(d) for d in str(sum)]
    return ctr

if __name__ == '__main__':
    print(persistence(39), "->", 3)
    print(persistence(4), "->", 0)
    print(persistence(25), "->", 2)
    print(persistence(999), "->", 4)
