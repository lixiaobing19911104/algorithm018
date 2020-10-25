def plus_one(li):
    n = len(li)
    for i in range(n - 1, -1, -1):
        li[i] += 1
        if li[i] != 10:
            break
        li[i] = 0
        if i == 0:
            li.insert(0, 1)
    return li


if __name__ == '__main__':
    print(plus_one([1, 9, 9, 9]))
    print(plus_one([1, 9, 9, 2]))
    print(plus_one([9, 9, 9, 9]))
