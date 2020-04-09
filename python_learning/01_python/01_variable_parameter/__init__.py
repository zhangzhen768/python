# coding:utf-8


def variable_parameter(test, *args, **kwargs):
    """
    这是一个测试可变参数的函数(无任何实际意义)
    :param test:
    :param args:
    :param kwargs:
    :return:
    """
    print ("test " + test)
    # 遍历元组中的所有参数
    for i in args:
        print ("args", i)
    # 遍历字典中的所有参数
    for key, value in kwargs.items():
        print (key, value)


if __name__ == '__main__':
    print "Hello World"
    variable_parameter("This is a test", 1, 2, 3, name='eagle', age=10, hobby=['eat', 'drunk', 'play', 'happy'])
