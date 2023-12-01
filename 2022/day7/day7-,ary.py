# day 7: no space left on device
import input
from pprint import pprint

data = (input).data.splitlines()
#print(data)

dir = {} # to hold all the directories

# graph shit
def addNode(graph : dict, node) -> None:
    if node not in graph:
        graph[node] = {} # empty dictionary

def addEdge(graph, u, v = None) -> None:
    addNode(graph, u) # add u
    graph[u] = v # connect u to v

def createGraph(datos) -> dict:
    g = {}
    curr = g
    past = curr
    p2 = curr

    for line in datos:
        if line[0] == '$': # line with a command 
            if 'cd' in line: # changing directories
                cd = line[5:]+' (dir)' # directory name we're moving to now + (dir) so we know its a directory lol
                if '..' in cd: # move up in the directory path
                    curr = past
                    past = p2
                    continue
                # add this new directory to the dictionary
                addNode(curr, cd)
                p2 = past
                past = curr
                curr = curr[cd]
            if 'ls' in line: # doesn't matter
                continue
        else:
            if 'dir' in line: # if the line is just listing a directory it doesn't rly matter rn
                continue
            else: # otherwise, if its a file, we want to add it to our graph-dictionary thingy
                size, name = line.split() # split up for easy indexing lmao
                addEdge(curr, name, size)
    return g # return the graph

def recursiveDir(graphy) -> int:
    global dir
    i = 0
    for key, val in graphy.items():
        if '(dir)' in key: # if this key is a directory
            x = recursiveDir(val) # examine the value(s) for additional directories
            i += x # increment total for this directory
            if key in dir: # if this key is already in our
                key = key + str(x) # add name of directory
            dir[key] = x # set value of the key
        else:
            i += int(val) # incremnet value of the directory
    return i # return value of the directory

def laPrimeraParte(datos : list) -> int:
    global dir
    graph = createGraph(data)
    #pprint(graph)
    recursiveDir(graph)
    #print(dir)

    total = 0
    for key, val in dir.items(): # find all the values that are less than 100000
        print(val)
        if val <= 100000:
            total += val
    return total
print(laPrimeraParte(data))

