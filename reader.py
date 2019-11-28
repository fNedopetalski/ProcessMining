from xml.dom import minidom
import networkx as nx
import matplotlib.pyplot as plt

# Check if a string is an integer
# This is necessary to get ID number
def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

# Get all the ID numbers
def setID(item, ID):
    for elem in item:
        if isInt(elem.attributes['value'].value):
            ID.append(elem.attributes['value'].value)

# Get all the activities in a set
def setAct(item, act):
    seq2 = []
    for elem in item:
        if elem.attributes['key'].value == 'Activity':
            act.append(elem.attributes['value'].value)

# Create nodes for each activity in the log
def createNodes(G, seq):
    for i in seq:
        G.add_node(i, name = i)

# Create the edges between the nodes 
def createEdges(G, seq):
    for i in range(len(seq)-2):
        G.add_edge(seq[i], seq[i+2])
        i+=2

tree = minidom.parse('PurchasingExample.xes')   
items = tree.getElementsByTagName('string')

ID = []
act = [] 

G = nx.DiGraph()

setID(items, ID)

setAct(items, act)

createNodes(G, act)

createEdges(G, act)

nx.draw(G, nodesize = 250)

plt.savefig('grafo.png',dpi = 300)