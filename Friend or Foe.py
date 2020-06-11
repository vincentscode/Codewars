def friend(x):
    ret = []
    for i in x:
        if len(i) == 4:
            ret.append(i)
    return ret


if __name__ == '__main__':
    print(friend(['I', 'Sanjay', 'Gupt']), "->", ['Gupt'])
    print(friend(["Ryan", "Kieran", "Mark", ]), "->", ["Ryan", "Mark"])