def is_bipartite(graph, size):
    color = [-1] * len(graph)  
    color[0] = 0  
    queue = [0]  
    
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if color[v] == -1:
                color[v] = 1 - color[u] 
                queue.append(v)
            elif color[v] == color[u]:
                return False  
    return True

def max_matching(graph, size):
    match = [-1] * len(graph)
    def dfs(u, visit):
        for v in graph[u]:
            if not visit[v]:
                visit[v] = True
                if match[v] == -1 or dfs(match[v], visit):
                    match[v] = u
                    return True
        return False
    for u in range(size):
        visit = [False] * len(graph)
        dfs(u, visit)
    return match

def Kenig(graph, size):
    if not is_bipartite(graph, size):
        return "Граф не двудольный"
    
    match = max_matching(graph, size)
    free = [u for u in range(size) if u not in match]
    directed = [[] for _ in range(len(graph))]
    for u in range(size):
        for v in graph[u]:
            if match[v] == u:
                directed[v].append(u)  
            else:
                directed[u].append(v)  
    
    visit = [False] * len(graph)
    queue = free.copy()
    for u in queue:
        visit[u] = True
    while queue:
        u = queue.pop(0)
        for v in directed[u]:
            if not visit[v]:
                visit[v] = True
                queue.append(v)
    

    cover = []
    cover.extend(u for u in range(L_size) if not visit[u])
    cover.extend(v for v in range(L_size, len(graph)) if visit[v])
    return sorted(cover)

def graph():
    L_size = int(input())
    R_size = int(input())
    total = L_size + R_size
    graph = [[] for _ in range(total)]
    
    while True:
        edge = input().strip()
        if not edge:
            break
        u, v = map(int, edge.split())
        graph[u].append(v)
        graph[v].append(u)  
    
    return graph, L_size

graph, L_size = graph()
result = Kenig(graph, L_size)
    
print(result)