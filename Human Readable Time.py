def make_readable(seconds):
    if seconds >= 3600:
        h_remain = seconds % 3600
        h = str(int((seconds - h_remain) / 3600))
        seconds = seconds - (int(h) * 3600)
    else:
        h_remain = seconds
        h = str(0)

    if h_remain >= 60:
        s = h_remain % 60
        m = str(int((h_remain - s) / 60))
    else:
        s = str(seconds)
        m = str(0)

    if len(h) < 2:
        h = "0" + h

    if len(m) < 2:
        m = "0" + m

    if len(str(s)) < 2:
        s = "0" + str(s)

    return "{}:{}:{}".format(h, m, s)

if __name__ == '__main__':
    print(make_readable(34))
    print(make_readable(4334))
    print(make_readable(86399), "23:59:59")