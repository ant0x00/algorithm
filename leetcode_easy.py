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


def romanToInt(s):
    # https://leetcode-cn.com/problems/roman-to-integer/description/
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ans = 0
    for i in range(len(s) - 1):
        c = s[i]
        cafter = s[i + 1]
        if roman_dict[c] < roman_dict[cafter]:
            ans = ans - roman_dict[c]
        else:
            ans = roman_dict[c] + ans
    ans += roman_dict[s[-1]]
    return ans


def longestCommonPrefix(strs):
    if not strs:
        return ""
    strs.sort(key=len)
    shortest_str = strs[0]
    max_prefix = len(shortest_str)
    for i in range(max_prefix):
        for one_str in strs:
            if one_str[i] != shortest_str[i]:
                return shortest_str[:i]
                break
    return shortest_str



if __name__ == '__main__':
    # print(reverse(-3210))
    # print(is_palindrome_number(121))
    # print(romanToInt("LVIII"))
    print(longestCommonPrefix(["abca","aba","aaab"]))
