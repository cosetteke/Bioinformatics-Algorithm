# https://dodona.ugent.be/nl/courses/359/series/3491/activities/279985369
import datetime
def rollover_date(day=datetime.date.today().day, month=datetime.date.today().month, year = datetime.date.today().year):

    # first roll over the month to the next year
    year += (month - 1) // 12
    month = (month - 1) % 12 + 1 # 注意两个顺序不能反 不然month的值会改变
    # roll over extra days to month
    return datetime.date(year, month, 1) + datetime.timedelta(day - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()