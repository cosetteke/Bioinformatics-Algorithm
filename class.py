class Student(object):
    def __init__(self, first='', last='', id=0):  # initializer
        self.first_name_str = first
        self.last_name_str = last
        self.id_int = id

    def update(self, first='', last='', id=0):
        if first:
            self.first_name_str = first
        if last:
            self.last_name_str = last
        if id:
            self.id_int = id

    def __str__(self):  # string representation, for printing
        return "{} {}, ID:{}".format \
            (self.first_name_str, self.last_name_str, self.id_int)


import math


class Point(object):
    def __init__(self, x_param=0.0, y_param=0.0):
        self.x = x_param
        self.y = y_param

    def distance(self, param_pt):
        x_diff = self.x + param_pt.x
        y_diff = self.y + param_pt.y
        return math.sqrt(x_diff ** 2 + y_diff ** 2)

    def sum(self, param_pt):
        newpt = Point()
        newpt.x = self.x + param_pt.x
        newpt.y = self.y + param_pt.y
        return newpt

    def __str__(self):
        print("called the __str__ method")
        return "({:.2f},{:.2f})".format(self.x, self.y)


class NewClass(object):
    def __init__(self, attribute='default', name='Instance'):
        self.name = name  # public attribute
        self.__attribute = attribute  # 'private' attribute

    def __str__(self):
        return '{} has attribute {}'.format(self.name, self.__attribute)

def special_sum(a, b):
    if type(a) == int and type(b) == int:
        result = a+b
    else:
        try:
            result = int(a) + int(b)
        except ValueError:
            result = 0
    return result

class MyClass(object):
    def __init__(self, param1 = 0):
        print('in constructor')
        self.value = param1

    def __str__(self):
        print('in str')
        return 'Val is : {}'.format(str(self.value))

    def __add__(self, param2):
        print('in add')
        result = self.value + param2.value
        return MyClass(result)

class Rational(object):
    def __init__(self, numer, denom = 1):
        print('in constructor')
        self.numer = numer
        self.denom = denom

    def __str__(self):
        print('in string')
        return str(self.numer) + '/' + str(self.denom)

    def __repr__(self):
        print('in repr')
        return self.__str__()

