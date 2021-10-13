import re
from collections import defaultdict

class Graph:
    """
    The following details of a Graph are modeled:
    1. A directed edge between two nodes (with an optional weight)
    2. A directed edge between two nodes
    3. A edge from the node to the node (with an optional weight)
    4. Multiple edges between the two nodes with different weights

    The following input is recognised per line:
    1. a->b
    2. a->b [weight] (integer)

    The following are the methods availble in Graph:
    1. add_edge(node1, node2, weight):
        Add node1->node2 with the given weight
    2. del_edge(node1, node2, weight):
        Delete node1->node2 with the given weight
    3. input_edge
        input edge in the string format like above
    """
    
    def __init__(self, input=''):
        """
        input: a multi-line string of graph descriptions
        """
        # match any input according to the above specifications
        self.exp=r"([a-zA-Z]\w*)\s*->\s*([a-zA-Z]\w*)\s*(?:\[\s*(\d+)\s*\])?"
        self.graph = defaultdict(list)
        self.weights = defaultdict(list)
        inputLines = input.split('\n')
        #print(inputLines)
        for line in inputLines:
            self.parseLine(line)
    
    def parseLine(self, line):
        result = re.search(self.exp, line)
        if result:
            params = result.groups()
            node1 = params[0]
            node2 = params[1]
            weight = 0
            if params[2]:
                weight = int(params[2])
            self.add_edge(node1, node2, weight)
        
    def input_edge(self, line=''):
        if line:
            self.parseLine(line)

    def add_edge(self, node1, node2, weight=0):
        # Add only if it does not exist
        if node2 not in self.graph[node1]:
            self.graph[node1].append(node2)
        if weight not in self.weights[(node1, node2)]:
            self.weights[(node1, node2)].append(weight)

    def del_edge(self, node1, node2, weight=0):
        if (node1, node2) in self.weights:
            if weight in self.weights[(node1, node2)]:
                self.weights[(node1, node2)].remove(weight)
                if not self.weights[(node1, node2)]:
                    # empty list, remove the node1->node2 association as well
                    self.graph[node1].remove(node2)

    def __str__(self):
        output = ""
        for node1 in self.graph.keys():
            for node2 in self.graph[node1]:
                edge = "{}->{}".format(node1, node2)
                if (node1, node2) in self.weights:
                    if self.weights[(node1, node2)]:
                        for weight in self.weights[(node1, node2)]:
                            if (weight):
                                output += edge + "[{}]\n".format(weight)
                            else:
                                output += edge + "\n"
                    else:
                        output += "\n"
        return output.rstrip()

    def get_adjacent_nodes(self, node):
        if node in self.graph:
            return self.graph[node]
        else:
            # we dont directly call self.graph even though it can return []
            # because it will add to the dict as it is defaultdict
            return []

if __name__ == "__main__":
    g = Graph("""
        a -> b
        a->  c
        a->d [ 10 ]
        a->d[15]
        """)
    print(g)
    g.add_edge("b", "c", 13)
    g.del_edge("a", "d", 10)
    g.del_edge("a", "d", 15)
    g.input_edge("e->f")
    g.input_edge("a->e[11]")
    print(g)