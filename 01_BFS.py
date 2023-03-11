
# Breadth First Search (BFS) Algorithm


# create a node class to create the graph
class Node:
    def __init__(self,name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

# define the algorithm
def breadth_first_search(first_node):
    # Assign the the first node the queue
    queue = [first_node]
    # go throughout the queue until it finish
    while queue:
        current_node = queue.pop(0)
        current_node.visited = True
        print(current_node.name)
        # ADD NEIGHBORS TO THE QUEUE
        for node in current_node.adjacency_list:
            if not node.visited:
                queue.append(node)
                node.visited = True

# check the algorithm
if __name__ == '__main__':

    # Create Nodes
    node_a = Node(name="a")
    node_b = Node(name="b")
    node_c = Node(name="c")
    node_d = Node(name="d")
    node_e = Node(name="e")
    node_f = Node(name="f")
    node_g = Node(name="g")
    node_h = Node(name="h")
    # Add the neighbors
    node_a.adjacency_list.extend([node_e, node_b, node_g])
    node_b.adjacency_list.extend([node_a, node_f, node_g, node_h])
    node_c.adjacency_list.extend([node_b, node_h, node_d])
    node_d.adjacency_list.extend([node_e, node_c])
    node_e.adjacency_list.extend([node_a, node_f, node_d])
    node_f.adjacency_list.extend([node_e, node_b])
    node_g.adjacency_list.extend([node_a, node_b])
    node_h.adjacency_list.extend([node_c, node_b])

    # Run BFS
    breadth_first_search_(node_a)