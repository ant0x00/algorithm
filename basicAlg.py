def guess_price():
    """
    猜价格游戏。
    输入一共1000以内的数值。
    二分法最快。
    :return:
    """
    old_price = price = i = 0
    true_price = 520  # input("请输入商品的真实价格：")
    print(true_price)
    while (old_price != true_price):
        i += 1
        old_price = int(input("请猜价格："))
        if old_price > true_price:
            print("高了!")
        elif old_price < true_price:
            print("低了!")
        else:
            print("猜中了！！！您一共用了%d次" % i)
            break


def fib(n):
    '''斐波那契数列；递归算法'''
    if (n <= 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def test_fib():
    fib_num = int(input("您想推算第几个月的兔子数？请输入："))
    for i in range(fib_num): print(fib(i))


def fact(n):
    """还是递归算法"""
    if (n <= 1): return 1
    return n * fact(n - 1)


def test_fact():
    fact_num = int(input("请输入想计算的阶乘数："))
    print(f"阶乘计算结果是：{fact(fact_num)}")


def guess_num():
    """数字猜数游戏 枚举实现"""
    for i1 in range(1, 10):
        for i2 in range(10):
            for i3 in range(10):
                for i4 in range(10):
                    for i5 in range(1, 10):
                        multiplier = i1 * 10000 + i2 * 1000 + i3 * 100 + i4 * 10 + i5
                        result = i5 * 100000 + i5 * 10000 + i5 * 1000 + i5 * 100 + i5 * 10 + i5
                        # print(f"{multiplier},{result}")
                        if (multiplier * i1 == result):
                            print("{0} {1} {2} {3} {4}".format(i1, i2, i3, i4, i5))
                            print("x{0:8}".format(i1))
                            print("-----------")
                            print("{0} {1} {2} {3} {4} {5}".format(i5, i5, i5, i5, i5, i5))


if __name__ == ('__main__'):
    test_fact()
    # guess_num()
    # guess_price()
    # test_fib()
