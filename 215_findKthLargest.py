# encoding:utf8
import json


# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
        输出: 4
        """
        return sorted(nums, reverse=True)[k - 1]

    def findKthLargest(self, nums, k):
        n = len(nums)
        if k > n :
            return
        index = self.quick_sort(nums, 0, n-1, k)
        return nums[index]

    def quick_sort(self, nums, begin, end, k):
        left = begin
        right = end
        if left >= right:
            return left
        pos = self.partion(nums, left, right)
        if k == pos + 1:
            return pos
        elif k < pos + 1:
            return self.quick_sort(nums, begin, pos - 1, k)
        else:
            return self.quick_sort(nums, pos + 1, end, k)

    def partion(self, nums, begin, end):
        priot = nums[begin]
        left, right = begin + 1, end - 1
        while left <= right:
            while left <= right and nums[right] > priot:
                right -= 1
            while left <= right and nums[left] <= priot:
                left += 1
            if left > right:
                break
            nums[left], nums[right] = nums[right], nums[left]
        # print(nums, left, right)
        nums[right], nums[begin] = nums[begin], nums[right]
        # print(nums)
        return right


class Solution2:
    # 采用快速排序方法，分成的数列左边大于右边
    def findKthLargest(self, nums, k):
        n = len(nums)
        if (k > n):
            return k
        index = self.quickSort(nums, 0, n, k)
        print(index, nums)
        return nums[index]

    def quickSort(self, nums, l, r, k):
        if l >= r:
            return l
        p = self.partition(nums, l, r)
        if p + 1 == k:
            return p
        if p + 1 > k:
            return self.quickSort(nums, l, p, k)
        else:
            return self.quickSort(nums, p + 1, r, k)

    def partition(self, nums, begin, end):
        priot = nums[begin]
        left, right = begin + 1, end - 1
        while left <= right:
            while left <= right and nums[right] < priot:
                right -= 1
            while left <= right and nums[left] >= priot:
                left += 1
            if left > right:
                break
            nums[left], nums[right] = nums[right], nums[left]
        # print(nums, left, right)
        nums[right], nums[begin] = nums[begin], nums[right]
        # print(nums)
        return right

    def partition2(self, nums, l, r):
        v = nums[l]
        j = l
        i = l + 1
        while i <= r:
            if nums[i] >= v:
                nums[j + 1], nums[i] = nums[i], nums[j + 1]
                j += 1
            i += 1
        nums[l], nums[j] = nums[j], nums[l]
        return j

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
            k = int(line)

            ret = Solution2().findKthLargest(nums, k)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
