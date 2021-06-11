from game import Directions
from util import Stack, Queue, PriorityQueue, manhattanDistance
import sys
from searchProblems import ScaryProblem
UNREACHABLE_GOAL_STATE = [Directions.STOP]


def tinyMazeSearch(problem):
    """
    Run to get familiar with directions.
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.

    Run this function to get familiar with how navigations works using Directions enum.
    """

    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    to_goal_easy_directions = [s, s, w, w, w, w, s, s, e, e, e, e, s, s, w, w, w, w, s, s, e, e, e, e, s, s, w, w, w, w,
                               w]
    return to_goal_easy_directions


def simpleMazeSearch(problem):
    """
    Q1:
    Search for the goal using right-hand or left-hand method explained in docs.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getNextStates(problem.getStartState())
    Dont forget to take a look at handy classes implemented in util.py.
    """
    "*** YOUR CODE HERE ***"
    currentState = problem.getStartState()
    lastState = currentState
    to_goal_directions = []
    pacmandir = "right"
    counter = 0
    while not problem.isGoalState(currentState):
        actions = []
        counter += 1
        nextStates = problem.getNextStates(currentState)
        for nextState in nextStates:
            actions.append(nextState[1])
        
        if pacmandir == "left":
            if not Directions.SOUTH in actions: #there is a wall to the left
                if Directions.WEST in actions:
                    for nextState in nextStates:
                        if nextState[1] == Directions.WEST:
                            currentState = nextState[0]
                            break
                    to_goal_directions.append(Directions.WEST)
                else:
                    pacmandir = "up"
            else: 
                pacmandir = "down"
                for nextState in nextStates:
                        if nextState[1] == Directions.SOUTH:
                            currentState = nextState[0]
                            break
                to_goal_directions.append(Directions.SOUTH)
        elif pacmandir == "right": 
            if not Directions.NORTH in actions: #there is a wall to the left
                if Directions.EAST in actions:
                    for nextState in nextStates:
                        if nextState[1] == Directions.EAST:
                            currentState = nextState[0]
                            break
                    to_goal_directions.append(Directions.EAST)
                else:
                    pacmandir = "down"
            else: 
                pacmandir = "up"
                for nextState in nextStates:
                        if nextState[1] == Directions.NORTH:
                            currentState = nextState[0]
                            break
                to_goal_directions.append(Directions.NORTH)
        elif pacmandir == "up":
            if not Directions.WEST in actions: #there is a wall to the left
                if Directions.NORTH in actions:
                    for nextState in nextStates:
                        if nextState[1] == Directions.NORTH:
                            currentState = nextState[0]
                            break
                    to_goal_directions.append(Directions.NORTH)
                else:
                    pacmandir = "right"
            else: 
                pacmandir = "left"
                for nextState in nextStates:
                        if nextState[1] == Directions.WEST:
                            currentState = nextState[0]
                            break
                to_goal_directions.append(Directions.WEST)
        elif pacmandir == "down":
            if not Directions.EAST in actions: #there is a wall to the left
                if Directions.SOUTH in actions:
                    for nextState in nextStates:
                        if nextState[1] == Directions.SOUTH:
                            currentState = nextState[0]
                            break
                    to_goal_directions.append(Directions.SOUTH)
                else:
                    pacmandir = "left"
            else: 
                pacmandir = "right"
                for nextState in nextStates:
                        if nextState[1] == Directions.EAST:
                            currentState = nextState[0]
                            break
                to_goal_directions.append(Directions.EAST)
    return to_goal_directions
"*** YOUR EXPLANATION HERE***"
"""
bale, ba in algorithm pacman khane haye map ra tey mikonad ta be noghteye payan beresad
vali in algorithm behine nist
"""
    
def lastAction(currentState, lastState):
    if currentState[1] == lastState[1]:
        if currentState[0] - lastState[0] < 0:
            return Directions.WEST
        else :
            return Directions.EAST
    elif currentState[0] == lastState[0]:
        if currentState[1] - lastState[1] < 0:
            return Directions.SOUTH
        else :
            return Directions.NORTH


def dfs(problem):
    """
    Q2:
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal.
    Make sure to implement a graph search algorithm.
    Dont forget to take a look at handy classes implemented in util.py.
    """

    "*** YOUR CODE HERE ***"
    currentState = problem.getStartState()
    lastState = currentState
    to_goal_directions = []
    visitedNode = []
    stack = Stack()
    stackTemp = Stack()
    visitedNode.append(currentState)
    stack.push(currentState)

    while not problem.isGoalState(currentState):
        nextStates = problem.getNextStates(currentState)

        for nextState in nextStates:
            lastState = currentState
            if not visited(nextState, visitedNode):
                lastState = currentState
                currentState = nextState[0]
                visitedNode.append(currentState)
                stack.push(currentState)
                break

        if lastState == currentState:
            
            if stack.isEmpty():
                return [Directions.STOP]
            pop = stack.pop()
            if stack.isEmpty():
                return [Directions.STOP]
            currentState = stack.pop()
            stack.push(currentState)
    count = 0
    while not stack.isEmpty():
        stackTemp.push(stack.pop())

    nextState = lastState
    while not problem.isGoalState(nextState):
        currentState = stackTemp.pop()
        nextState = stackTemp.pop()
        to_goal_directions.append(lastAction(nextState, currentState))
        stackTemp.push(nextState)

    return to_goal_directions
    "*** YOUR EXPLANATION HERE***"
    """
    bale ravande moshahedeye khaneha motabeghe algorithme dfs ast
    na , pacman ta jai ke be hadaf beresad khane hara baresi mikonad va lozoman hameye khane hara barresi nemikonad 
    """

def visited(node, path):
    flag = False
    for p in path:
            if node[0] == p:
                flag = True
    return flag

def bfs(problem):
    """
    Q3:
    Search the shallowest nodes in the search tree first.
    Dont forget to take a look at handy classes implemented in util.py.
    """

    "*** YOUR CODE HERE ***"
    currentState = problem.getStartState()
    lastState = currentState
    to_goal_directions = []
    visitedNode = []
    queue = Queue()
    stack = Stack()
    stackAction = Stack()
    visitedNode.append(currentState)
    queue.push(currentState)
    while not problem.isGoalState(currentState):
        currentState = queue.pop()
        nextStates = problem.getNextStates(currentState)
        for nextState in nextStates:
            temp = []
            if not visited(nextState, visitedNode):
                temp.append(currentState)
                temp.append(nextState)
                stack.push(temp)
                queue.push(nextState[0])
                visitedNode.append(nextState[0])

    findState = currentState
    while not stack.isEmpty():
        state = stack.pop()
        if findState == state[1][0]:
            findState = state[0]
            stackAction.push(state[1][1])

    while not stackAction.isEmpty():
        to_goal_directions.append(stackAction.pop())
    return to_goal_directions

    "*** YOUR EXPLANATION HERE***"
    """
    bfs faghat baraye masaeli ke hazineye masir matrah nabashad javabe behine ra midahad va agar dar masalei hazineye masir ha
    motefavet bashad , bfs lozoman masire behine re bar nemigardanad
    """

def deadend(problem):
    """
    Q5: Search for all dead-ends and then go for goal state.
    Dont forget to take a look at handy classes implemented in util.py.
    """
    currentState = problem.getStartState()
    startState = currentState
    lastState = currentState
    to_goal_directions = []
    visitedNode = []
    stack = Stack()
    stackTemp = Stack()
    visitedNode.append(currentState)
    queue = Queue()
    queue.push(currentState)
    deadend = []
    goal = []
    pqueue = PriorityQueue()
    
    while not queue.isEmpty():

        currentState = queue.pop()
        nextStates = problem.getNextStates(currentState)
        for nextState in nextStates:
            temp = []
            if len(nextStates) == 1 and visited(nextState, visitedNode):
                if not problem.isGoalState(currentState):
                    deadend.append(currentState)
                    break

            if not visited(nextState, visitedNode):
                temp.append(currentState)
                temp.append(nextState)
                stack.push(temp)
                queue.push(nextState[0])
                visitedNode.append(nextState[0])

        if problem.isGoalState(currentState):
            goal.append(currentState)

    goalState = startState 
    count = len(deadend)
    for i in range(count + 1):
        if i == count:
            returns = Bfs(startState, goal, problem)
            actions = returns[1]
            for action in actions:
                to_goal_directions.append(action)
        else:  
            dm = sys.maxint
            returns = Bfs(startState, deadend, problem)
            actions = returns[1]
            for action in actions:
                to_goal_directions.append(action)
            deadend.remove(returns[0])
            startState = returns[0]

    return to_goal_directions
    "*** YOUR CODE HERE ***"


def Bfs(startState, goalStates, problem):
    currentState = startState
    lastState = currentState
    to_goal_directions = []
    visitedNode = []
    queue = Queue()
    stack = Stack()
    stackAction = Stack()
    visitedNode.append(currentState)
    queue.push(currentState)
    while not currentState in goalStates:
        currentState = queue.pop()
        nextStates = problem.getNextStates(currentState)
        for nextState in nextStates:
            temp = []
            if not visited(nextState, visitedNode):
                temp.append(currentState)
                temp.append(nextState)
                stack.push(temp)
                queue.push(nextState[0])
                visitedNode.append(nextState[0])

    findState = currentState
    while not stack.isEmpty():
        state = stack.pop()
        if findState == state[1][0]:
            #print "find"
            findState = state[0]
            stackAction.push(state[1][1])

    while not stackAction.isEmpty():
        to_goal_directions.append(stackAction.pop())
    return [currentState, to_goal_directions]


def ucs(problem):
    """
    Q7: Search the node of least total cost first.
    Dont forget to take a look at handy classes implemented in util.py.
    """

    "*** YOUR CODE HERE ***"
    currentState = problem.getStartState()
    lastState = currentState
    to_goal_directions = []
    visitedNode = []
    pqueue = PriorityQueue()
    stack = Stack()
    stackAction = Stack()
    visitedNode.append(currentState)
    pqueue.push(currentState, 0)
    while not problem.isGoalState(currentState):
        currentState = pqueue.pop()
        nextStates = problem.getNextStates(currentState)
        for nextState in nextStates:
            temp = []
            if not visited(nextState, visitedNode):
                temp.append(currentState)
                temp.append(nextState)
                stack.push(temp)
                pqueue.push(nextState[0], nextState[2])
                visitedNode.append(nextState[0])

    findState = currentState
    while not stack.isEmpty():
        state = stack.pop()
        if findState == state[1][0]:
            #print "find"
            findState = state[0]
            stackAction.push(state[1][1])

    while not stackAction.isEmpty():
        to_goal_directions.append(stackAction.pop())
    return to_goal_directions

    "*** YOUR EXPLANATION HERE***"
    """
    agar hazineye hameye masir ha yeksan bashand , bfs va ucs yeksan khahand shod 
    """