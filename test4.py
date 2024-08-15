class parent1:
    def func1(self):
        print("hello parent1")

class parent2:
    def func2(self):
        print("hello parent2")

class parent3:
    def func2(self):
        print("hello parent3")

class child(parent1, parent2, parent3):
    def func3(self):
        print("this is child")

obj = child()
obj.func1()
obj.func2()
obj.func3()
