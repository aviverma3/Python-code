class sports:
    _name = None
    _team = None

    
    def __init__(self, name, team):
        self._name = name
        self._team = team

    def diplay(self):
        print("Players name", self._name)
        print("team name", self._team)

class cricket(sports):
    def __init__(self, name, team):
        sports.__init__(self, name, team)
    
    def displayInDetails(self):
        print("name: ",self._name)
        self.diplay()

obj = cricket("avinash", "ipl")
# obj.diplay()
obj.displayInDetails()


        
