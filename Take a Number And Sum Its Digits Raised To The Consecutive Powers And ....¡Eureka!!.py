def sum_dig_pow(a, b):
    res = []
    for num in range(a, b+1):
        digits = [int(d) for d in str(num)]
        sum = 0
        for i in range(0, len(digits)):
            sum += digits[i] ** (i+1)
        if sum == num:
            res.append(num)
    return res

if __name__ == '__main__':

    print(sum_dig_pow(1, 10), "->", [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(sum_dig_pow(1, 100), "->", [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
    print(sum_dig_pow(10, 89), "->", [89])
    print(sum_dig_pow(10, 100), "->", [89])
    print(sum_dig_pow(90, 100), "->", [])
    print(sum_dig_pow(89, 135), "->", [89, 135])