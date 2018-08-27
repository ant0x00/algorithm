def fun():
    if(1<2):return "ffff"
    print("flajfl")


def test_fun():
    s = fun()
    print(s)

if __name__ == ('__main__'):
    s = [26, 19, 27, 80, -9, 17, 37, 25, 18, 93]

    # select_sort
    for i in range(0, len(s) - 1):
        index = i
        for j in range(i + 1, len(s)):
            if s[index] > s[j]:
                index = j
        s[i], s[index] = s[index], s[i]

    # print sort result.
    print(s)