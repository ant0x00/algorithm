# coding: utf-8
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_ = len(needle)
        if not len_:
            return 0
        else:
            for x in range(len_, len(haystack) + 1):  # +1是为了处理两个字符串长度一致的情况
                if haystack[x - len_:x] == needle:
                    return x - len_
            else:
                return -1


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
            haystack = stringToString(line);
            line = next(lines)
            needle = stringToString(line);

            ret = Solution().strStr(haystack, needle)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
