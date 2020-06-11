def encrypt(text, n):
    if type(text) is not str:
        return None
    res = text
    for i in range(n):
        tmp = ""
        for j in range(1, len(res), 2):
            tmp += res[j]
        for j in range(0, len(res), 2):
            tmp += res[j]
        res = tmp
    return res


def decrypt(encrypted_text, n):
    if type(encrypted_text) is not str:
        return None
    res = encrypted_text
    for i in range(n):
        tmp_list = [""]*len(res)
        e = 1
        for j in range(0, int(len(res)/2)):
            tmp_list[e] = res[j]
            e += 2
        e = 0
        for j in range(int(len(res)/2), len(res)):
            tmp_list[e] = res[j]
            e += 2
        res = "".join(tmp_list)
    return res

if __name__ == '__main__':
    print(encrypt("This is a test!", 0), "->", "This is a test!")
    print(encrypt("This is a test!", 1), "->", "hsi  etTi sats!")
    print(encrypt("This is a test!", 2), "->", "s eT ashi tist!")
    print(encrypt("This is a test!", 3), "->", " Tah itse sits!")
    print(encrypt("This is a test!", 4), "->", "This is a test!")
    print(encrypt("This is a test!", -1), "->", "This is a test!")
    print(encrypt("This kata is very interesting!", 1), "->", "hskt svr neetn!Ti aai eyitrsig")

    print(decrypt("This is a test!", 0), "->", "This is a test!")
    print(decrypt("hsi  etTi sats!", 1), "->", "This is a test!")
    print(decrypt("s eT ashi tist!", 2), "->", "This is a test!")
    print(decrypt(" Tah itse sits!", 3), "->", "This is a test!")
    print(decrypt("This is a test!", 4), "->", "This is a test!")
    print(decrypt("This is a test!", -1), "->", "This is a test!")
    print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "->", "This kata is very interesting!")

    print(encrypt("", 0), "->", "")
    print(decrypt("", 0), "->", "")
    print(encrypt(None, 0), "->", None)
    print(decrypt(None, 0), "->", None)
