def find_uniq(arr):
    known = {}
    for num in arr:
        if num in known:
            known[num] += 1
        else:
            known[num] = 1
    return min(known, key=known.get)

if __name__ == '__main__':
    print(find_uniq([1, 1, 1, 2, 1, 1]), "->", 2)
    print(find_uniq([0, 0, 0.55, 0, 0]), "->", 0.55)
    print(find_uniq([3, 10, 3, 3, 3]), "->", 10)