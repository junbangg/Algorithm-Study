# Pseudo code

def search(root):
    queue = Queue()
    root.marked = true
    queue.enqueue(root)

    while queue:
        r = queue.dequeue()
        visit(r)
        for n in r.adjacent:
            if not n.marked:
                n.marked = True
                queue.enqueue(n)
