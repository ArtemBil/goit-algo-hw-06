from algs.algs import (dfs_iterative, bfs_iterative)

kyiv_metro_graph = {
    "Akademmistechko": ["Zhytomyrska", "Lisova", "Khreshchatyk"],
    "Zhytomyrska": ["Akademmistechko", "Sviatoshyn"],
    "Sviatoshyn": ["Zhytomyrska", "Nyvky", "Khreshchatyk"],
    "Nyvky": ["Sviatoshyn", "Lisova"],
    "Lisova": ["Nyvky", "Akademmistechko", "Darnytsia"],
    "Darnytsia": ["Lisova", "Livoberezhna"],
    "Livoberezhna": ["Darnytsia", "Khreshchatyk"],
    "Khreshchatyk": ["Livoberezhna", "Akademmistechko", "Sviatoshyn"]
}

start_station = "Akademmistechko"

dfs_path = dfs_iterative(kyiv_metro_graph, start_station)
bfs_path = bfs_iterative(kyiv_metro_graph, start_station)

print(f"Шлях DFS: {dfs_path} \n")
print(f"Шлях BFS: {bfs_path} \n")

