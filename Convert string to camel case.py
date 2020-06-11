def to_camel_case(text):
    if text == "":
        return ""
    text = text.replace("-", "_")
    cc = text.split("_")
    f_low = text[0].islower()
    i = 0
    for p in cc:
        p = list(p)
        p[0] = p[0].upper()
        cc[i] = "".join(p)
        i += 1
    if f_low:
        x = list(cc[0])
        x[0] = x[0].lower()
        cc[0] = ''.join(x)
    res = ''.join(cc)
    return res

if __name__ == '__main__':
    print(to_camel_case(''), "->", '')
    print(to_camel_case("the_stealth_warrior"), "->", "theStealthWarrior")
    print(to_camel_case("The-Stealth-Warrior"), "->", "TheStealthWarrior")
    print(to_camel_case("A-B-C"), "->", "ABC")