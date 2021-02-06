
# Pseudo code

def DFS(root):
    if root: return
    visit(root)
    root.visited = True
    for n in root.adjacent:
        if n.visited == false:
            search(n)


