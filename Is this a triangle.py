
def is_triangle(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] + sides[1] > sides[2]:
        return True
    return False


if __name__ == '__main__':
    print(is_triangle(1, 2, 2), "->", True, "didn't work when sides were 1, 2, 2")
    print(is_triangle(7, 2, 2), "->", False, "didn't work when sides were 7, 2, 2")
    print(is_triangle(1, 2, 3), "->", False, "didn't work when sides were 1, 2, 3")
    print(is_triangle(1, 3, 2), "->", False, "didn't work when sides were 1, 3, 2")
    print(is_triangle(3, 1, 2), "->", False, "didn't work when sides were 3, 1, 2")
    print(is_triangle(5, 1, 2), "->", False, "didn't work when sides were 5, 1, 2")
    print(is_triangle(1, 2, 5), "->", False, "didn't work when sides were 1, 2, 5")
    print(is_triangle(2, 5, 1), "->", False, "didn't work when sides were 2, 5, 1")
    print(is_triangle(4, 2, 3), "->", True, "didn't work when sides were 4, 2, 3")
    print(is_triangle(5, 1, 5), "->", True, "didn't work when sides were 5, 1, 5")
    print(is_triangle(2, 2, 2), "->", True, "didn't work when sides were 2, 2, 2")
    print(is_triangle(-1, 2, 3), "->", False, "didn't work when sides were -1, 2, 3")
    print(is_triangle(1, -2, 3), "->", False, "didn't work when sides were 1, -2, 3")
    print(is_triangle(1, 2, -3), "->", False, "didn't work when sides were 1, 2, -3")
    print(is_triangle(0, 2, 3), "->", False, "didn't work when sides were 0, 2, 3")
