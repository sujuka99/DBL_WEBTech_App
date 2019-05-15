import networkx as nx
import pandas as pd
from bokeh.io import show, save, output_file
from bokeh.plotting import figure
from bokeh.models.graphs import from_networkx
import matplotlib.pyplot as plt
import numpy as np


dataset = pd.read_csv("GephiMatrix_co-authorship.csv", sep=';')
#print(dataset)

rows, cols = np.where(dataset == 1)
edges = zip(rows.tolist(), cols.tolist())
G = nx.Graph()
G.add_edges_from(edges)
#nx.draw(G, node_size=50, with_labels=False)
#plt.show()
plot = figure(title="Networkx Integration Demonstration", x_range=(-1.1,1.1), y_range=(-1.1,1.1),
              tools="", toolbar_location=None)
graph = from_networkx(G, nx.spring_layout, scale=2, center=(0,0))

plot.renderers.append(graph)

output_file("networkx_graph.html")
save(plot)

# giving numbers to the columns and rows instead of names
#index = 0
#list_of_names = []  #storing the names at the correct index, or they will be at the right index after the deletion below
#for column in dataset.columns:
#    list_of_names.append(column)
#    dataset.rename(columns={column:index}, index={column:index-1}, inplace=True)
#    index = index + 1
#
#dataset = dataset.drop(dataset.columns.size-1, axis=1) #remove last column, because that gives NAN all the time
##print(dataset)
#del list_of_names[0]  #remove the unknown name that's ruining everything, now correct indexes
#
#G = nx.from_pandas_dataframe(dataset, 0, 0, 0)

#G = nx.karate_club_graph()
#plot = figure(title="Networkx Integration Demonstration", x_range=(-1.1,1.1), y_range=(-1.1,1.1),
#              tools="", toolbar_location=None)
#
#graph = from_networkx(G, nx.spring_layout, scale=2, center=(0,0))
#plot.renderers.append(graph)
#
#output_file("networkx_graph.html")
#save(plot)

#def show_graph_with_labels(adjacency_matrix):
#    rows, cols = np.where(adjacency_matrix == 1)
#    edges = zip(rows.tolist(), cols.tolist())
#    gr = nx.Graph()
#    gr.add_edges_from(edges)
#    nx.draw(gr, node_size=50, with_labels=False)
#    plt.show()
#
#show_graph_with_labels(dataset) #make_label_dict(get_labels("GephiMatrix_co-authorship.csv")))