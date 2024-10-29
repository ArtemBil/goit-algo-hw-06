from algs.algs import dijkstra

weighted_edges_kyiv = {
    "Akademmistechko": {"Zhytomyrska": 2, "Lisova": 10, "Khreshchatyk": 5},
    "Zhytomyrska": {"Akademmistechko": 2, "Sviatoshyn": 1.5},
    "Sviatoshyn": {"Zhytomyrska": 1.5, "Nyvky": 1, "Khreshchatyk": 6},
    "Nyvky": {"Sviatoshyn": 1, "Lisova": 9},
    "Lisova": {"Nyvky": 9, "Akademmistechko": 10, "Darnytsia": 2.5},
    "Darnytsia": {"Lisova": 2.5, "Livoberezhna": 2},
    "Livoberezhna": {"Darnytsia": 2, "Khreshchatyk": 4},
    "Khreshchatyk": {"Livoberezhna": 4, "Akademmistechko": 5, "Sviatoshyn": 6}
}

shortest_paths_kyiv = dijkstra(weighted_edges_kyiv, 'Akademmistechko')

print(shortest_paths_kyiv)
