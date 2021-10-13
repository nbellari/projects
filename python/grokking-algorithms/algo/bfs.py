from ds.graph import Graph
from collections import deque

def breadth_first_search(g, begin, end):
    """
    Given a graph g, start node "begin" and an end node "end" that tells whether
    a given node in the graph can reach "end", walks the graph using BFS
    """
    sq = deque()
    visited = []
    # No need to explicitly check if "begin" is part of the graph
    sq += g.get_adjacent_nodes(begin)

    while sq:
        next = sq.popleft()
        if next not in visited:
            if next == end:
                return True
            sq += g.get_adjacent_nodes(next)
    
    return False

if __name__ == "__main__":
    g1 = Graph("""
        Bob -> Anuj
        Bob -> Peggy
        Me -> Bob
        Me -> Alice
        Me -> Claire
        Alice -> Peggy
        Claire -> Johny
        Claire -> Thom
        """)
    print (breadth_first_search(g1, "Me", "Bob"))