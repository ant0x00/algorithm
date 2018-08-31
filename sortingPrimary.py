def buket_sorting(test_list):
    """
    桶排序，从小到大排列
    本例子可以处理 -100 到100的数
    """
    # str_input = input("请输入要排序的数字，数之间用空格隔开：")
    test_list = [x + 100 for x in test_list]
    input_arr = [0 for x in range(201)]
    for num in test_list:
        input_arr[num] += 1
    for i in range(200):
        if input_arr[i] > 0: print(i - 100)


def buket_sorting_optimize(list):
    """桶排序也可以进行优化，达到不牺牲时间复杂度，但减少空间复杂度的目的"""
    pass


def selection_sorting(test_list):  # 直接选择排序
    n = len(test_list)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if test_list[j] < test_list[min]:  # 每一趟找出所有未排序的最小数坐标
                min = j
        test_list[i], test_list[min] = test_list[min], test_list[i]  # 将筛选出的最小数放在已排序数组的最后
        print(test_list)
    print(test_list)


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
        print(less + pivotList + more)
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


def insert_sorting(list):  # 插入排序，每趟循环将未排序的第一个新元素插入到已排序的正确位置
    n = len(list)
    for i in range(1, n):
        if list[i] < list[i - 1]:
            temp = list[i]
            index = i
            for j in range(i - 1, -1, -1):
                if list[j] > temp:
                    list[j + 1] = list[j]
                    index = j
                else:
                    break
        list[index] = temp
        print(list)
    print(list)


# to do
# 堆排序（基于选择排序）等学完数据结构 堆以后完善

# 归并排序
def merge_sort(lst):  # 此方法来自维基百科：http://zh.wikipedia.org/zh/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        merged = []

        while left and right:
            merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))

        while left:
            merged.append(left.pop(0))

        while right:
            merged.append(right.pop(0))

        return merged

    print(lst)
    middle = int(len(lst) / 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)


def shell_sort(list):
    """
    希尔排序（基于插入排序），递减增量排序算法
    改进的地方：插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
    但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位。
    """
    n = len(list)
    # 初始步长
    gap = round(n / 2)
    print(gap)
    while gap > 0:
        for i in range(gap, n):
            # 每个步长进行插入排序
            temp = list[i]
            j = i
            # 插入排序
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        # 得到新的步长
        gap = round(gap / 2)
        print(list)
        print(gap)
    print(list)


def qsort2(alist, l, u):  # 单索引快排one index for partion
    if l >= u:
        return

    m = l
    for i in range(l + 1, u + 1):
        if alist[i] < alist[l]:
            m += 1
            alist[m], alist[i] = alist[i], alist[m]
            # print(alist)
    # swap between m and l after partition, important!
    alist[m], alist[l] = alist[l], alist[m]
    print(m)
    print(alist)

    qsort2(alist, l, m - 1)
    qsort2(alist, m + 1, u)
    return alist


def qsort3(arr, lower, upper):
    if lower >= upper: return
    pivot = arr[lower]
    left, right = lower + 1, upper
    while left <= right:
        while left <= right and arr[left] < pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left > right:
            break
        arr[left], arr[right] = arr[right], arr[left]
        print(arr)
    arr[lower], arr[right] = arr[right], arr[lower]
    print(f"{left}:{right}")
    print(arr)
    qsort3(arr, lower, right - 1)
    qsort3(arr, right + 1, upper)
    return arr


def qsort4(alist, lower, upper):
    print(alist)
    if lower >= upper:
        return

    pivot = alist[lower]
    left, right = lower + 1, upper
    while left <= right:
        while left <= right and alist[left] < pivot:
            left += 1
        while left <= right and alist[right] >= pivot:
            right -= 1
        if left > right:
            break
        # swap while left <= right
        alist[left], alist[right] = alist[right], alist[left]
    # swap the smaller with pivot
    alist[lower], alist[right] = alist[right], alist[lower]

    qsort4(alist, lower, right - 1)
    qsort4(alist, right + 1, upper)


if __name__ == "__main__":
    test_list = [26, 101, 27, 80, -9, 17, 37, 18, 93, 25]

    # print(fast_sorting(test_list))
    # buket_sorting(test_list)
    # bubble_sorting()
    # selection_sorting(test_list)
    print(qsort3(test_list, 0, len(test_list) - 1))
    # import timeit #统计函数执行时间
    # print(timeit.timeit("bubble_sorting", setup="from __main__ import bubble_sorting",number=1000))
