# coding: utf-8
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        双指针使用（left和right）
        """
        if not s:
            return ''
        s = list(s)
        left = 0
        right = len(s) - 1
        while right > left:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)

    def reverseString3(self, s):
        if len(s) <= 1:
            return s
        else:
            return s[-1]+ self.reverseString3(s[:-1])

    def reverseString2(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join([x for x in reversed(s)])


def stringToString(input):
    return input[1:-1]


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);

            ret = Solution().reverseString3(s)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
