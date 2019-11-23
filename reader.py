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
            ID += [elem.attributes['value'].value]

tree = minidom.parse('PurchasingExample.xes')
items = tree.getElementsByTagName('string')

ID = []

setID(items, ID)
