def solution(number):
    res = []
    for i in range(number):
        if i % 5 == 0 or i % 3 == 0:
            res.append(i)
    return sum(res)

if __name__ == '__main__':
    print(solution(10), "->",23)