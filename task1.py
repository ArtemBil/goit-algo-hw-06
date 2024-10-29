import networkx as nx
import matplotlib.pyplot as plt


kyiv_metro_data = {
    "Akademmistechko": ["Zhytomyrska", "Lisova", "Khreshchatyk"],
    "Zhytomyrska": ["Akademmistechko", "Sviatoshyn"],
    "Sviatoshyn": ["Zhytomyrska", "Nyvky", "Khreshchatyk"],
    "Nyvky": ["Sviatoshyn", "Lisova"],
    "Lisova": ["Nyvky", "Akademmistechko", "Darnytsia"],
    "Darnytsia": ["Lisova", "Livoberezhna"],
    "Livoberezhna": ["Darnytsia", "Khreshchatyk"],
    "Khreshchatyk": ["Livoberezhna", "Akademmistechko", "Sviatoshyn"]
}

G_kyiv = nx.Graph()

for station, neighbors in kyiv_metro_data.items():
    for neighbor in neighbors:
        G_kyiv.add_edge(station, neighbor)

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G_kyiv, seed=42)
nx.draw(G_kyiv, pos, with_labels=True, node_color="lightblue", node_size=500, edge_color="gray", font_size=12, font_weight="bold")
plt.title("Kyiv Metro Network (Using kyiv_metro_data)")
plt.show()

num_nodes_kyiv = G_kyiv.number_of_nodes()
num_edges_kyiv = G_kyiv.number_of_edges()
degree_kyiv = dict(G_kyiv.degree())

print({
    "Number of nodes": num_nodes_kyiv,
    "Number of edges": num_edges_kyiv,
    "Degree of each node": degree_kyiv
})