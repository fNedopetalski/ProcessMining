#import pandas as pd
#import xml.etree.cElementTree as ET
#import matplotlib.pyplot as plt
#import networkx as nx
from xml.dom import minidom


tree = minidom.parse('PurchasingExample.xes')
items = tree.getElementsByTagName('string')

for elem in items:
    if elem.attributes['value'].value == '339':
        print('hey')

