# -*- conding:utf-8 -*-
# 类和对象
#一切皆对象
#类：具有相同属性与行为的对象构成的一个整体（集合），类可以想象成为一个类别

#类与对象的关系
#1、类是对象的抽象，而对象是类的具体变现新式
#2、类是一个设计蓝图（模板），对象是根据该蓝图创建的产物

#现实与python程序进行的一种映射
# 对象 属性 行为
#属性：类中定义变量
#行为：类中定义方法（函数）
#函数与方法：是一样的，在面向过程的语言中称为函数，面向对象的语言中称为方法
# 方法依赖于对象 函数功能

#定义类
#命名惯例：每个单词首字母大写，没有分割
class Person():

      #在类中定义方法，需要具有一个参数，按照惯例命名为：Self
      def walk(self):
            print("walk")
      def run(self):
            print('run')
#通过类来创建对象
p=Person()
#在解释器 p.run(p)
p.run()
p.walk()
# self 表示的是当前的对象，也就是调用该方法的对象
# 哪一个对象调用了该方法，self指代的就是哪一个方法
