import string


def alphabet_position(text):
    text = text.strip().lower()
    alphabet = string.ascii_lowercase
    res = ""
    for t in text:
        if t in alphabet:
            res += str(alphabet.find(t)+1) + " "
    return res[0:len(res)-1]

if __name__ == '__main__':
    print(alphabet_position("The sunset sets at twelve o' clock."), "->", "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
    print(alphabet_position("The narwhal bacons at midnight."), "->", "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")
    
    from random import randint
    
    number_test = ""
    for item in range(10):
        number_test += str(randint(1, 9))
    print(alphabet_position(number_test), "->", "")