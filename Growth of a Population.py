def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        years += 1
        p0 += p0 * (percent / 100) + aug
    return years


if __name__ == '__main__':
    print(nb_year(1500, 5, 100, 5000), "->", 15)
    print(nb_year(1500000, 2.5, 10000, 2000000), "->", 10)
    print(nb_year(1500000, 0.25, 1000, 2000000), "->", 94)
