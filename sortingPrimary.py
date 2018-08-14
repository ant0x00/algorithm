
def buket_sorting():
    """桶排序，从小到大排列"""
    str_input = input("请输入要排序的数字，数之间用空格隔开：")
    input_arr = [0 for x in range(101) ]
    for num in str_input.split():
        input_arr[int(num)]+=1
    for i in range(100):
        if input_arr[i]>0: print(i)

def bubble_sorting():
    """
    冒泡排序：
    思路：每次比较相邻的元素，如果顺序错误就交换过来
    测试用数据：-9 17 37 25 18 26 19 27 80
    """
    str_input = input("请输入要排序的数字，数之间用空格隔开：")
    num_arr = str_input.split()
    for i in range(len(num_arr)-1): #决定排序的轮次
        for j in range(len(num_arr)-i-1): #决定每轮要比较的次数
            if num_arr[j] > num_arr[j+1]:
                num_arr[j],num_arr[j+1] = num_arr[j+1],num_arr[j]
        print(num_arr)


def sortStudent(list):
    for i in range(len(list)):
        for j in range(1, len(list)-i):
            if list[j-1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]
    print(list)

if __name__ == "__main__":
    # buket_sorting()
    # bubble_sorting()
    sortStudent(['-9', '17', '18', '25', '19', '26', '27', '80'])