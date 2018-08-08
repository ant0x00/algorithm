
def guess_price():
    """
    猜价格游戏。
    输入一共1000以内的数值。
    二分法最快。
    :return:
    """
    old_price = price = i =0
    true_price = 520 #input("请输入商品的真实价格：")
    print(true_price)
    while(old_price != true_price):
        i += 1
        old_price = int(input("请猜价格："))
        if old_price > true_price:
            print("高了!")
        elif old_price < true_price:
            print("低了!")
        else:
            print("猜中了！！！您一共用了%d次"%i)
            break


def fib(n):
    '''斐波那契数列'''
    if(n <= 1): return n
    else: return fib(n-1)+fib(n-2)

def test_fib():
    fib_num = int(input("您想推算第几个月的兔子数？请输入："))
    for i in range(fib_num): print(fib(i))

if __name__ ==('__main__'):
    # guess_price()
    test_fib()