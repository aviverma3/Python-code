class Student:
    def __init__(self):
        self.__name = "Avinash"

    def _funName(self):      # protected method
        return "this is verma"
obj = Student()
print(obj.__name) 

class Subject(Student):       #inherited class
    pass


obj1 = Subject()
# print(dir(obj))

# calling by object of Student class
     
print(obj._funName())     
# calling by object of Subject class
# print(obj1._name)    
print(obj1._funName())