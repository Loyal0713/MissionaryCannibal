
# CPS 480
# Joshua Brown - brown8jt
# hw2-2c

# This program explores the missionaries and cannibals problem.
# It uses a breadth first search in order to find the search through
# the state space to find the goal state. In order to run, you must use
# python 3.6. In order to call the program, navigate to the file's directory
# and from the command line type "python hw2.py". Running the program will create
# a file "hw2output.txt" that contains the output.

# State class symbolizing the left and right sides of the "river" and also
# the side of the boat. Also contains a link to the parent state
class State:

    def __init__(self, missL, cannL, boat, missR, cannR):
        self.ml = missL
        self.cl = cannL
        self.boat = boat
        self.mr = missR
        self.cr = cannR
        self.parent = None

    # function determining if the current state is the goal state
    def isgoal(self):
        if self.ml == 0 and self.cl == 0:
            return True
        else:
            return False

    # function that determines if the current state is a legal state
    def islegal(self):
        # make sure there are no negative missionaries or cannibals,
        # and that missionaries are not outnumbered
        if (self.ml >= 0) and (self.ml < 4) and (self.mr >= 0) and (self.mr < 4):
            if (self.cl >= 0) and (self.cl < 4) and (self.cr >= 0) and (self.cr < 4):
                if (abs(self.ml-self.cl) >= 0) and (abs(self.mr-self.cr) >= 0):
                    return True
        else:
            return False

    # helper funciton used to print the state to the console
    def printstate(self):
        print("M:" + str(self.ml) + " C:" + str(self.cl) + " Boat:" + str(self.boat) + " M:" + str(self.mr) + " C:" + str(self.cr))

# generates the next state based on the given state
def nextgen(cur):

    # list to hold current state
    children = [];
    if cur.boat == 'l':

        # 2 missionaries move to right
        newstate = State(cur.ml-2, cur.cl, 'r', cur.mr+2, cur.cr)
        if newstate.islegal():
            newstate.parent = cur
            children.append(newstate)

        # 2 cannibals move to right
        newstate = State(cur.ml, cur.cl-2, 'r', cur.mr, cur.cr+2)
        if newstate.islegal():
            newstate.parent = cur
            children.append(newstate)

        # 1 missionary moves right
        newstate = State(cur.ml-1, cur.cl, 'r', cur.mr+1, cur.cr)
        if newstate.islegal():
            newstate.parent = cur
            children.append(newstate)

        # 1 cannibal moves right
        newstate = State(cur.ml, cur.cl-1, 'r', cur.mr, cur.cr+1)
        if newstate.islegal():
            newstate.parent = cur
            children.append(newstate)

        # 1 missionary and 1 cannibal move right
        newstate = State(cur.ml-1, cur.cl-1, 'r', cur.mr+1, cur.cr+1)
        if newstate.islegal():
            newstate.parent = cur
            children.append(newstate)

    else:

        # 2 missionaries move to left
        newstate = State(cur.ml+2, cur.cl, 'l', cur.mr-2, cur.cr)
        if newstate.islegal():
            newstate.parent = cur
            children.append(newstate)

        # 2 cannibals move to left
        newstate = State(cur.ml, cur.cl+2, 'l', cur.mr, cur.cr-2)
        if newstate.islegal():
            newstate.parent = cur
            children.append(newstate)

        # 1 missionary moves right
        newstate = State(cur.ml+1, cur.cl, 'l', cur.mr-1, cur.cr)
        if newstate.islegal():
            newstate.parent = cur
            children.append(newstate)

        # 1 cannibal moves right
        newstate = State(cur.ml, cur.cl+1, 'l', cur.mr, cur.cr-1)
        if newstate.islegal():
            newstate.parent = cur
            children.append(newstate)

        # 1 missionary and 1 cannibal move right
        newstate = State(cur.ml+1, cur.cl+1, 'l', cur.mr-1, cur.cr-1)
        if newstate.islegal():
            newstate.parent = cur
            children.append(newstate)

    return children

# function used to search for the goal state
def search():

    #initialize state for 3 missionaries and cannibals
    initial = State(3,3, 'l', 0,0)

    if initial.isgoal():
        return initial

    # set up breadth first search
    all = list()
    searched = set()
    all.append(initial)

    while all:

        # grab first state in queue
        state = all.pop(0)

        # return goal state
        if state.isgoal():
            print("found goal")
            return state

        # add state to searched set
        searched.add(state)

        # generate list of new states
        children = nextgen(state)

        # add new states if they have not been checked yet
        for child in children:
            if (child not in searched) or (child not in all):
                all.append(child)

    return None

# helper function used to print the solution path of states
def printpath(solution):

    file = open("hw2output.txt", "w+")

    # start with empty list
    path = []
    path.append(solution)


    parent = solution.parent

    # traverse from goal state to initial state
    while parent:
        path.append(parent)
        parent = parent.parent

    for i in range(len(path)):
        state = path[len(path) - i - 1]

        string = "M:" + str(state.ml) + " M:" + str(state.cl) + " Boat:" + str(state.boat) + " M:" + str(state.mr) + " C:" + str(state.cr)
        file.write(string)
        print(string)

def main():
    path = search()
    printpath(path)

if __name__ == "__main__":
    main()
