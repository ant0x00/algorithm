# coding: utf-8
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]


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
            print(line.__class__)
            a = stringToString(line)
            line = next(lines)
            b = stringToString(line)

            ret = Solution().addBinary(a, b)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
