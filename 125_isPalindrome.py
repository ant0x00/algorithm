# encoding:utf8

# https://leetcode-cn.com/playground/new/empty
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        left = 0
        right = n-1
        while left<right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True



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

            ret = Solution().isPalindrome(s)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
