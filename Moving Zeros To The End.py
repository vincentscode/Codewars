def move_zeros(array):
    array2 = []
    for c in array:
        if not (c == 0 and (type(c) == int) or type(c) == float):
            array2.append(c)
    return array2 + [0] * (len(array) - len(array2))

if __name__ == '__main__':
    print(type(0.0))
    print(move_zeros([0, 12, 0.0, 4, 0, 3, 4, False]))