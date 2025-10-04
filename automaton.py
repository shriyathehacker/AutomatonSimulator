class State:
    def __init__(self, id: int) -> None:
        self.id = id
        self.outgoingNodes = {} #{condition: endState}

    def addOutgoingNode(self, condition: str, node) -> None:
        self.outgoingNodes[condition] = node

    def check(self, condition: str): #-> State
        for key, value in self.outgoingNodes.items():
            if key == condition:
                return value

class States:
    def __init__(self, number: int) -> None:
        self.states = [State(i) for i in range(number)]

    def addEdge(self, id: int, nodeID: int, condition: str):
        sta = self.getNode(nodeID)
        cu = self.getNode(id)

        cu.addOutgoingNode(condition, sta)

    def getNode(self, ID: int) -> State:
        for state in self.states:
            if state.id == ID:
                return state

class InputAlphabet:
    def __init__(self, alphabet: list) -> None:
        self.alphabet = alphabet

class StartState:
    def __init__(self, states: States, stateID: int) -> None:
        self.state = states.getNode(stateID)

class AcceptState:
    def __init__(self, states: States, acceptedStateID: list[int]) -> None:
        self.accepted = []

        for id in acceptedStateID:
            self.accepted.append(states.getNode(id))

    def accept(self, state: State) -> bool:
        for validStates in self.accepted:
            if validStates == state:
                return True
            
        return False

class TransitionFunction:
    def __init__(self) -> None:
        pass

    def move(self, state: State, character: str) -> State:
        return state.check(character)

class Automaton:
    def __init__(self, states: States, alphabet: InputAlphabet, start: StartState, accept: AcceptState, trans: TransitionFunction) -> None:
        self.states = states
        self.alphabet = alphabet
        self.start = start
        self.accept = accept
        self.trans = trans

    def run(self, string: str) -> bool:
        currentState = self.start.state
        for i in string:
            if i in self.alphabet.alphabet:
                currentState = self.trans.move(currentState, i)
            else:
                print("Invalid string")
                
        if self.accept.accept(currentState):
            return True
        else:
            return False

#Step 1, define the number of states        
Q = States(4)

#Step 2, add edges
Q.addEdge(0, 1, "4")
Q.addEdge(0, 0, "8")
Q.addEdge(0, 0, "1")
Q.addEdge(1, 0, "4")
Q.addEdge(1, 2, "8")
Q.addEdge(1, 0, "1")
Q.addEdge(2, 0, "4")
Q.addEdge(2, 0, "8")
Q.addEdge(2, 3, "1")
Q.addEdge(3, 3, "4")
Q.addEdge(3, 3, "8")
Q.addEdge(3, 3, "1")

#Step 3, add alphabet
sigma = InputAlphabet(["4", "8", "1"])

#Step 4, add a transition function
delta = TransitionFunction()

#Step 5, add a start state
s = StartState(Q, 0)

#Step 6, add a accepted strings
F = AcceptState(Q, [3])

computer = Automaton(Q, sigma, s, F, delta)

while True:
    user = input()
    answer = computer.run(user)
    if answer == True:
        print("accept")
    else:
        print("reject")