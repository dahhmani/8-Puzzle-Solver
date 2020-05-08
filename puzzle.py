import planner
from node import Node
from plot_path import * # TA code
from sys import argv
from time import time

def main():
    goal = Node('123456780') # specify the puzzle's goal configuration
    start = Node(argv[1]) # read the puzzle's initial configuration from the command line

    if start.isSolvable():
        t0 = time()
        plan, *_ = planner.BFS(start, goal) # solve the puzzle using brute force search
        t1 = time() 
        print(f'Puzzle is solved in {t1-t0} s\n')
        logResults(plan)
        visualizePath()
    else:
        print('Puzzle is unsolvable')

def logResults(plan):
    with open('nodePath.txt', 'w') as file:
        for node in plan:
            tiles = restructure(node.state)
            for i in range(9):
                file.write(f'{tiles[i]} ')
            file.write('\n')

    with open('plan.txt', 'w') as file:
        file.write('State\t\tAction\n')
        for node in plan:
            file.write(f'{node.state}\t')
            file.write(f'{node.action}\n')

def restructure(state):
    ''' column-wise representation of the state '''
    state = list(state)
    state[1], state[3] = state[3], state[1]
    state[2], state[6] = state[6], state[2]
    state[5], state[7] = state[7], state[5]

    return state

if __name__ == '__main__':
    main()