# -*- coding: utf-8 -*-
class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'haha'

    def eat(self):
        print('%s在吃鱼,它%d岁了'%(self.name,self.age))



tom = cat('tom',10)
tom.eat()
print(tom)

del tom