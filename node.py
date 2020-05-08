class Node:
    def __init__(self, state, action=None, parent=None):
        self.state = state # the puzzle configuration which is stored row-wise as a string
        self.action = action # the action performed on the parent to produce this state
        self.parent = parent # previous node

    def neighbors(self):    
        state = list(self.state)
        blank = state.index('0')
        adj = []
        # Right 
        tmpstate = state[:]
        if blank not in [2,5,8]:
            tmpstate[blank], tmpstate[blank+1] = tmpstate[blank+1], tmpstate[blank]
            adj.append(Node(''.join(tmpstate), 'Right'))
        # Left
        tmpstate = state[:]
        if blank not in [0,3,6]:
            tmpstate[blank], tmpstate[blank-1] = tmpstate[blank-1], tmpstate[blank]
            adj.append(Node(''.join(tmpstate), 'Left'))
        # Up
        tmpstate = state[:]
        if blank not in [0,1,2]:
            tmpstate[blank], tmpstate[blank-3] = tmpstate[blank-3], tmpstate[blank]
            adj.append(Node(''.join(tmpstate), 'Up'))
        # Down
        tmpstate = state[:]
        if blank not in [6,7,8]:
            tmpstate[blank], tmpstate[blank+3] = tmpstate[blank+3], tmpstate[blank]
            adj.append(Node(''.join(tmpstate), 'Down'))

        return adj 

    def isSolvable(self):
        inversions = 0
        state = list(map(int, self.state))

        for i in range(8):
            for j in range(i+1, 9):
                if(state[j] and state[i] and state[i] > state[j]):
                    inversions += 1

        return inversions % 2 == 0

    def display(self):
        for i in range(9):
            print(self.state[i], end=' ')
            if (i+1) % 3 == 0: print()
        print('-' * 5)
        
    def __eq__(self, other):

        return self.state == other.state