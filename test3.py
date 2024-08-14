class Student:
    def __init__(self) -> None:
        pass
    def __init__(self,name,marks,rollnum):
        self.name = name
        self.marks = marks
        self.rollnum = rollnum

s1 = Student("avinash", 90, 234459)
print(s1.name, s1.rollnum)
s2 = Student("pallavi", 91, 83029)
print(s2.name, s2.marks)
