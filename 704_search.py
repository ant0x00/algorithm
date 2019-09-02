import json


class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (high + low) // 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return -1

    def search1(self, nums, target):
        for n in nums:
            if target == n: return nums.index(n)
        return -1


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
            nums = stringToIntegerList(line)
            line = next(lines)
            target = int(line)

            ret = Solution().search(nums, target)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
