from collections import deque

def BFS(start, goal):
    ''' Breadth-first Search (Brute-force Search) '''
    solved, visited, count = False, set(), 0
    
    # Forward Search
    unvisited = deque([start]) # queue
    visited.add(start.state)

    while unvisited:
        current = unvisited.pop() # queue.dequeue()

        if current == goal:
            solved = True
            break

        count += 1

        for node in current.neighbors():
            if node.state not in visited:
                node.parent = current
                unvisited.appendleft(node) # queue.enqueue()
                visited.add(node.state)
    
    # Backtrack
    plan = generatePlan(current)
    plan.appendleft(start)

    return (plan, solved, count)

def DFS(start, goal):
    ''' Depth-first Search (Brute-force Search) '''
    solved, visited, count = False, set(), 0
   
    # Forward Search
    unvisited = deque([start]) # stack

    while unvisited:
        current = unvisited.pop() # stack.pop()
        visited.add(current.state)

        if current == goal:
            solved = True
            break

        count += 1

        for node in current.neighbors():
            if node.state not in visited:
                node.parent = current
                unvisited.append(node) # stack.push()

    # Backtrack
    plan = generatePlan(current)
    plan.appendleft(start)

    return (plan, solved, count)

def generatePlan(currentNode):
    plan = deque() # queue
    while (currentNode.parent is not None):
        plan.appendleft(currentNode)
        currentNode = currentNode.parent

    return plan