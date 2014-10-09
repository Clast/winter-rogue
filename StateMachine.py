State = type("State", (object,),{})

class Rest(State):
	def Execute(self):
		print "Resting"

class Attack(State):
    def Execute(self):
        print "Attacking"

class Flee(State):
    def Execute(self):
        print "Fleeing"

class Transition(object):
    def __init__(self,toState):
        self.toState = toState
        
    def Execute(self):
        print "Transitioning"
        
class StateMachine(object):
    def __init__(self,char):
        self.char = char
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.trans = None
    
    def SetState(self, stateName):
        self.curState = self.states[stateName]
        
    def Transition(self, transName):
        self.trans = self.transitions(transName)
        
    def Execute(self):
        if (self.trans):
            self.trans.Execute()
            self.setState(self.trans.toState)
            self.trans = None
        self.curState.Execute()
