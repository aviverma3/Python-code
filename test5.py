class super:
    var1 = None
    _var2 = None
    __var3 = None
    def __init__(self, var1, var2, var3):
        self.var1= var1
        self._var2 = var2
        self.__var3 = var3
    def diplayPublicVar(self):
        print("private var",self.var1)
    
    def displayProtectedVar(self):
        print("protected var", self._var2)
    
    def displayPrivateVar(self):
        print("private var",self.__var3)

class sub(super):
    def __init__(self, var1, var2, var3):
        super.__init__(self,var1, var2, var3)
    
    def accessProtected(self):
        self.displayProtectedVar()

obj = sub("avinash",2,"avi")
obj.diplayPublicVar()
obj.accessProtected()
obj.displayPrivateVar()

print("again protected",obj._var2)
