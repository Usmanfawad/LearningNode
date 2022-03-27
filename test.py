def done(x):
    x += 1
    return x

def main(lst,x,limit):
    # print(len(lst))

    count = 0
    for i in lst:

        if i > 0:
            lst[count] = i-1

        if i == 0:
            lst[count] = 6
            lst.append(9)

        count+=1


    x += 1
    while x != limit:
        print(x)
        # if x==130:
        #     length_og = len(lst)
        #     length = len(lst)//2000
        #     print(length_og )
        #     print(length)
        #     lst = lst[:length]
        return main(lst,x,limit)
    return len(lst)

if __name__ == "__main__":

    print('')

    value = input()
    # print(value)
    lst = value.split(',')
    lst2 = value.split(',')
    # print(lst)

    nc = 0
    for i in lst:
        lst[nc] = int(i)
        lst2[nc] = int(i)
        nc+=1

    # n_lst = lst

    x = 0

    a = main(lst,x,80)
    result1 = a
    print('')

    print(f'After 80 days, there are {result1} ants.')

    print('')

    print(lst2)
    b = main(lst2,x,256)
    result2 = b
    print(f'After 256 days, there are {result2} ants.')


