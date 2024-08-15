class Student:
    def __init__(self) -> None:
        pass
    def __init__(self,name,marks,rollnum):
        self.name = name
        self.marks = marks
        self.rollnum = rollnum
    @staticmethod #decorator
    def hello():
        print("hello")

    def dispay(self):
        print(self.name, self.marks, self.rollnum)

s1 = Student("avinash", 90, 234459)
print(s1.name, s1.rollnum)

s1.hello()

s2 = Student("pallavi", 91, 8302932)
s2.dispay()

class chemistry(Student):
    name = "breaking bad"
    @staticmethod
    def subject():
        print("this is chemistry class")
    
ch1 = chemistry("ravi", 99, 42324)
ch1.dispay()
ch1.subject()
s3 = Student("namaneshawar", 97, 324325)
s3.dispay()
print(ch1.name)

# ch1.subject()
