import sys

n, m, v = map(int, sys.stdin.readline().split())

tree = [[0]]

for i in range(m):
    node = list(map(int, sys.stdin.readline().split()))
    tree.append(node)
    
print(tree)

visited = [False for _ in range(m+1)]
print(visited)

def dfs(tree, v, visited):
    if visited return False;
    else:
        idx = tree[v][1]
        visited[idx] = True
    dfs(tree, )
dfs(tree, v, )