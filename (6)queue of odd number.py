#定义一个函数getOdd，设置1个参数number，用于接收传入的正整数。
#该函数用于将1到任意正整数之间的奇数添加到空列表中，并将添加完成后的列表返回。
#最后，传入参数 20调用该函数，并输出结果。
#奇数指不能被 2 整除的整数，例如 1，3，5，7，9，即除以 2 余数为 1。


def getOdd(number):
    numberlist = []
    for num in range(1,number + 1):
        if num % 2 == 1:
            numberlist.append(num)
    print(numberlist)
    
getOdd(20)