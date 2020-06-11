def divisors(integer):
    divs = []
    for i in range(2, integer):
        if integer % i == 0:
            divs.append(i)
    if len(divs) == 0:
        return "{} is prime".format(integer)
    return divs


if __name__ == '__main__':
    print(divisors(15), "->", [3, 5])
    print(divisors(12), "->", [2, 3, 4, 6])
    print(divisors(13), "->", "13 is prime")