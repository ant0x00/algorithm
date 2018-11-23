import json


# 贪心法
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        max_profit = 0
        for i in range(l-1):
            if prices[i]<prices[i+1]:
                max_profit =max_profit + prices[i+1] - prices[i]
        return max_profit


def stringToIntegerList(input):
    return json.loads(input)


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
            prices = stringToIntegerList(line)

            ret = Solution().maxProfit(prices)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()