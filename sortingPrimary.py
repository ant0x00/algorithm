def buket_sorting():
    """桶排序，从小到大排列"""
    str_input = input("请输入要排序的数字，数之间用空格隔开：")
    input_arr = [0 for x in range(101)]
    for num in str_input.split():
        input_arr[int(num)] += 1
    for i in range(100):
        if input_arr[i] > 0: print(i)


def bubble_sorting():
    """
    冒泡排序：
    思路：每次比较相邻的元素，如果顺序错误就交换过来
    测试用数据： 26 19 27 80 -9 17 37 25 18
    """
    str_input = input("请输入要排序的数字，数之间用空格隔开：")
    num_arr = str_input.split()
    for i in range(len(num_arr) - 1):  # 决定排序的轮次
        for j in range(len(num_arr) - i - 1):  # 决定每轮要比较的次数
            if num_arr[j] > num_arr[j + 1]:
                num_arr[j], num_arr[j + 1] = num_arr[j + 1], num_arr[j]
        print(num_arr)


def fast_sorting(test_list):
    """
    快速排序：
    思路：找一个基准元素N，然后先从右往左找第一个小于N的元素S，再由左往右找大于N的元素L，将S和L对调，再寻找，重复对调
          知道左右的坐标相遇，然后和N对调，递归。
    """
    less = []
    pivotList = []
    more = []
    if len(test_list) <= 1:
        return test_list
    else:
        pivot = test_list[0]
        for i in test_list:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        print(more + pivotList + less)
        less = fast_sorting(less)
        more = fast_sorting(more)
        return less + pivotList + more


def qsort(arr):
    """快排更简洁的写法"""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + [pivot] + qsort([x for x in arr[1:] if x >= pivot])

if __name__ == "__main__":
    test_list = [26, 19, 27, 80, -9, 17, 37, 25, 18]
    print(qsort(test_list))
    # buket_sorting()
    # bubble_sorting()
    # bubble_sorting()
