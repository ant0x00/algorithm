def condidate(m, A):
    j = m
    c = A[m]
    count = 1
    while j < len(A) - 1 and count > 0:
        j = j + 1
        if A[j] == c:
            count = count + 1
        else:
            count = count - 1
    if j == len(A) - 1:
        return c
    else:
        return condidate(j + 1, A)



def majority(A):
    if not A:
        return None
    c = condidate(0, A)
    count = 0
    for i in range(len(A)):
        if A[i] == c:
            count = count + 1
    if count > len(A) / 2:
        return c
    else:
        return None


if __name__ == '__main__':
    data = []
    result = majority(data)
    print(result)
