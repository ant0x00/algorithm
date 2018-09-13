def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sign = x < 0 and -1 or 1
    x = abs(x)
    ans = 0
    while x:
        ans = ans * 10 + x % 10
        x //= 10
        # x = int(x/10)
    return sign * ans if ans <= 0x7fffffff else 0


def is_palindrome_number(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reverse_number = 0
    while x > reverse_number:
        reverse_number = reverse_number * 10 + x % 10
        x //= 10
    return x == reverse_number or x == reverse_number // 10


if __name__ == '__main__':
    # print(reverse(-3210))
    print(is_palindrome_number(121))