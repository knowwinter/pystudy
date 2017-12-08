# -*- coding: utf-8 -*-
class Base(object):
    def test(self):
        print('-----base')

class A(Base):
    def test1(self):
        print('test1')

class B(Base):
    def test2(self):
        print('test2')

class C(B, A):
    pass

t = C()

t.test2()