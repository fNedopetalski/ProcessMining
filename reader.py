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
    labels=[]
    for i in range(len(seq)-2):
        labels.append((seq[i],seq[i+2]))
        i+=2
    G.add_edges_from(labels)

tree = minidom.parse('PurchasingExample.xes')   
items = tree.getElementsByTagName('string')

ID = []
act = [] 

G = nx.DiGraph()

setID(items, ID)

setAct(items, act)

createNodes(G, act)

createEdges(G, act)

G.remove_edge("End", "Create Purchase Requisition")

pos = nx.layout.spring_layout(G, k =2.0)

nx.draw(G, with_labels = True, nodesize = 250)

print("Número de nós: ",G.number_of_nodes())
print("Número de arestas: ",G.number_of_edges())
plt.show()

#plt.savefig('grafo.png', dpi = 300)