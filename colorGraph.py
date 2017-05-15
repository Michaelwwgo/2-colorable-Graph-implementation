from node import Node
import Queue
import sys


def graphContainsUnvisitedNodes(graph):
    for node in graph:
        visited = node.isVisited()
        if not visited:
            return True

def getUnvisitedNode(graph):
    for i in range(1,len(graph)):
        if not graph[i].isVisited():
            return graph[i]
    return graph[0];

def getOddCycle(graph,side1,side2):
    cycleL = []
    cycleR = []
    while  side1!=side2:
        cycleL.append(side1)
        cycleR.append(side2)
        side1 = graph[side1].getPrev()
        side2 = graph[side2].getPrev()
    fullCycle = []
    fullCycle.append(side1)
    for state in reversed(cycleL):
        fullCycle.append(state)
    for state in cycleR:
        fullCycle.append(state)

    return fullCycle




#This function takes the graph parameter and returns True or False for is2Colorable
#Along with a list of the whole graph if it is which should Ideally contain that
#graph's colors or otherwise a short list of states that caused the graph to fail.
def is2Colorable(graph):
    #mark graph 0 because the node there does not actually exist in the graph
    #I just created an offset by 1 so that the index matches the state number
    graph[0].markVisited()
    #loop through all graph's unvisited nodes
    #this while loop checks for potential disconnected graphs
    while graphContainsUnvisitedNodes(graph):
        #queue used to execute BFS
        queue = Queue.Queue()
        #get the unvisited node, mark it's colorRed since it is first state visited
        #in the current connected graph. Enqueue that state.
        curr = getUnvisitedNode(graph)
        curr.colorRed()
        curr.markVisited()
        queue.put(curr)
        while not queue.empty():
            curr = queue.get()
            currColor = curr.getColor()
            neighbors = curr.getNeighbors()
            #For all the neighbors in the most recently visited state, add it into
            #the queue and color it the opposite color of the most recently visited
            #state. If a child is visited and its color is of conflict with the curr
            #state return False as well as the odd cycle associated with it.
            for index in neighbors:
                child = graph[index]
                if not child.isVisited():
                    queue.put(child)                  #If it is unvisited mark it as visited and
                    child.assignPrev(curr.state)      #give it the color opposite of the curr color
                    child.markVisited()               #mark it as visited and give it a pointer to its parent
                    child.colorOpposite(currColor)
                elif child.getColor()==currColor:
                    return (False,getOddCycle(graph,curr.state,child.state))
    #Once whole graph is visited return true and return the graph with all it's colors.
    return (True,graph)




#Open the file
file = open(sys.argv[1],'r');
#Get the number of vertices
Vcount = int((file.readline()));
#Create all the graph nodes with no reference to child nodes
#Skips index 0 in order to line up vertex numbers with the vertex index.
graph = []
for i in range(Vcount+1):
    V = Node(i)
    graph.append(V)
#For each line in the file get the current node and the node to which it points
arr = []
for line in file:
    arr.append(line)
    node_adjacent = line.split(" ")
    graph[int(node_adjacent[0])].addChild(int(node_adjacent[1]))
    graph[int(node_adjacent[1])].addChild(int(node_adjacent[0]))

#Output of is two colorable as a tuple pair of (True/False , list of states)
coloredList = is2Colorable(graph)
#Output target file into the second console input made writable
targetFile = open(sys.argv[2],'w')

#Check if the output was true if yes write yes to output file and print out coloredList
#otherwise print no and print the output of coloredList which was the oddCycle.
if(coloredList[0]==True):
    targetFile.write("Yes\n")
    for index in range(1,len(coloredList[1])):
        targetFile.write(str(coloredList[1][index].state)+' '+coloredList[1][index].color+'\n')
else:
    targetFile.write("No\n")
    for element in coloredList[1]:
        targetFile.write(str(element)+'\n')
