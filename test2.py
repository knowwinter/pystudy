# -*- coding: utf-8 -*-
class A:
    def __init__(self):
        self.name = 'aaa'
        self.__age = 10

    def __test(self):
        print('hahahah')

    def getName(self):
        print(self.__age)

    def test(self):
        self.__test()

# a = A()
# #a.__test()
# a.test()

class B(A):
    pass

b = B()
b.getName()
b.test()

