def move_zeroes(li):
    j = 0
    i = 0
    n = len(li)
    while j < n:
        if li[j] != 0:
            li[i] = li[j]
            i += 1
        j += 1
    while i < n:
        li[i] = 0
        i += 1
    return li


if __name__ == '__main__':
    print(move_zeroes([0,1,0,3,12]))

