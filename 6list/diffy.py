# https://dodona.ugent.be/nl/courses/359/series/3490/activities/636597847
def next(list):
    """
    >>> next([32, 9, 14, 3])
    (23, 5, 11, 29)
    >>> next((1, 2, 1, 2, 1, 0))
    (1, 1, 1, 1, 1, 1)
    >>> next((1, 2, 1, 2, 1, 1))
    (1, 1, 1, 1, 0, 0)
    """
    new = []
    for i in range(1, len(list)):
        new.append(abs(list[i] - list[i-1]))
    new.append(abs(list[-1]-list[0]))
    return tuple(new)

def ducci(list):
    """
    >>> ducci([32, 9, 14, 3])
    ((32, 9, 14, 3), (23, 5, 11, 29), (18, 6, 18, 6), (12, 12, 12, 12), (0, 0, 0, 0))
    >>> ducci((1, 2, 1, 2, 1, 0))
    ((1, 2, 1, 2, 1, 0), (1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0))
    >>> ducci((1, 2, 1, 2, 1, 1))
    ((1, 2, 1, 2, 1, 1), (1, 1, 1, 1, 0, 0), (0, 0, 0, 1, 0, 1), (0, 0, 1, 1, 1, 1), (0, 1, 0, 0, 0, 1), (1, 1, 0, 0, 1, 1), (0, 1, 0, 1, 0, 0), (1, 1, 1, 1, 0, 0))
    """
    list = tuple(list)
    ducci = []
    while not (list in ducci or set(list) == {0}):
        # 注意这里不可以写成 while (list not in ducci) or (set(list) != {0}) 见手写笔记
        # 报错是runtime error
        ducci.append(list) # 注意不是extend
        list = next(list)
    ducci.append(list)
    return tuple(ducci)
# append 是将整个的对象添加到原列表的末尾。 而extend 是将列表与原有的列表合并。

def period(list1):
    """
    >>> period([32, 9, 14, 3])
    0
    >>> period((1, 2, 1, 2, 1, 0))
    0
    >>> period((1, 2, 1, 2, 1, 1))
    6
    """
    ducci_ = list(ducci(list1)) # 注意要转化成list
    if len(set(ducci_)) == len(ducci_):
        return 0
    last_item = ducci_[-1]
    return len(ducci_) - ducci_.index(last_item) - 1 # 不能用find()



if __name__ == '__main__':
    import doctest
    doctest.testmod()