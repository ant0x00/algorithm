# coding: utf-8

def reverse(x):
    """
    :type x: int
    :rtype: int
    反转整数
    思路：
    1. 判断正负数
    2. 从左到右取值
    3. 返回时判断反转数是否溢出
    """
    sign = x < 0 and -1 or 1
    x = abs(x)
    ans = 0
    while x:
        ans = ans * 10 + x % 10
        x //= 10
        # x = int(x/10)
    return sign * ans if ans <= 0x7fffffff else 0  # 0x7fffffff=2**32-1


def is_palindrome_number(x):
    # 判断是否回文数
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reverse_number = 0
    while x > reverse_number:
        reverse_number = reverse_number * 10 + x % 10
        x //= 10
    return x == reverse_number or x == reverse_number // 10


def romanToInt(s):
    # https://leetcode-cn.com/problems/roman-to-integer/description/
    # 罗马数字转整数
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
    # https://leetcode-cn.com/problems/longest-common-prefix/description/
    # 最长公共前缀
    # 还有其他解法 https://blog.csdn.net/ojshilu/article/details/12882835
    if not strs:
        return ""
    strs.sort(key=len)
    shortest_str = strs[0]
    max_prefix = len(shortest_str)
    for i in range(max_prefix):
        for one_str in strs:
            if one_str[i] != shortest_str[i]:
                return shortest_str[:i]
    return shortest_str


def longestCommonPrefix_use_zip(strs):
    """
    :type strs: List[str]
    :rtype: str
    最长公共前缀很pythonic的解法
    """
    prefix = ''
    for item in list(zip(*strs)):
        if len(set(item)) > 1:
            return prefix
        else:
            prefix += item[0]
    return prefix


def isValid(str):
    """
    :type s: str
    :rtype: bool
    有效的括号:https://leetcode-cn.com/problems/valid-parentheses/description/
    """
    from collections import deque
    d = {'(': ')', '[': ']', '{': '}'}
    stack = deque()
    for s in str:
        if s in d:
            stack.append(s)
        elif s in d.values():
            if len(stack) == 0:
                return False
            if s == d[stack[-1]]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    # print(reverse(-3210))
    # print(is_palindrome_number(121))
    # print(romanToInt("LVIII"))
    # print(longestCommonPrefix_use_zip(["abca", "aba", "abab"]))
    print(isValid("(r)"))
