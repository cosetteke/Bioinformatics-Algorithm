# https://dodona.ugent.be/nl/courses/359/series/3490/activities/668293311
def emergency_plan(n, m):
    """
    >>> emergency_plan(17, 5)
    [1, 6, 11, 16, 5, 12, 2, 9, 17, 10, 4, 15, 14, 3, 8, 13, 7]
    >>> emergency_plan(16, 11)
    [1, 12, 8, 5, 3, 2, 4, 7, 11, 16, 14, 15, 10, 6, 9, 13]
    """
    zones = list(range(1,n+1))
    plan = []
    i = 0
    while zones:
        if i >= len(zones):
            i %= len(zones) # 步长 %= 长度
        plan.append(zones.pop(i))
        i += (m-1) # 因为string长度在变
    return plan
def valid_jump(area_num):
    """
    >>> valid_jump(17)
    7
    >>> valid_jump(14)
    """
    for i in range(1,area_num):
        if emergency_plan(area_num, i)[-1] == 13:
            return i
    return None
if __name__ == '__main__':
    import doctest
    doctest.testmod()