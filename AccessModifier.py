# program to illustrate private access modifier in a class


class Geek:

    # private members
    __name = None
    __roll = None
    __branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # private member function
    def __displayDetails(self):

        # accessing private data members
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)

    # public member function
    def accessPrivateFunction(self):

        # accessing private member function
        self.__displayDetails()


# creating object
obj = Geek("avinash", 1706256, "Information Technology")

# calling public member function of the class
obj.accessPrivateFunction()

class B(Geek):
    def greet(self):
        print("hello Indore")
obj12 = B("ravi", 32432, "learning python")
obj12.greet
obj12.accessPrivateFunction()
# print(obj12.__name)
print(dir(obj))
print(obj._Geek__name)
