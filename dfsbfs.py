#DFS function

def dfs(visited, graph, node):
    if node not in visited:
        print (node, end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

#BFS function

def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s,end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    visited_DFS = set()
    visited_BFS = set()
    queue = []
    graph = dict()
    n = int(input("Enter no. of nodes: "))
    for i in range(1, n+1):
        edges = int(input("Enter no. of edges for node{}: ".format(i)))
        graph[i] = []
        
        for j in range(1, edges+1):
            node = int(input("Enter edge() for node{}: ".format(j,i)))
            graph[i].append(node)
    
    print("The following is DFS: ")
    dfs(visited_DFS, graph, 1)
    print()
    print("The following is BFS: ")
    bfs(visited_BFS, graph, 1, queue)
    
main()