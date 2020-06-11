def palindrome_chain_length(n):
    ctr = 0
    while str(n)[::-1] != str(n):
        n = str(int(str(n)[::-1]) + int(str(n)))
        ctr += 1
    return ctr

if __name__ == '__main__':
    print(palindrome_chain_length(87))