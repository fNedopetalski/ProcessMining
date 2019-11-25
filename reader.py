from xml.dom import minidom

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
    for elem in item:
        if elem.attributes['key'].value == 'Activity':
            act.add(elem.attributes['value'].value)

tree = minidom.parse('PurchasingExample.xes')   
items = tree.getElementsByTagName('string')

ID = []
act = set({}) # Forced to be a set

setID(items, ID)

setAct(items, act)