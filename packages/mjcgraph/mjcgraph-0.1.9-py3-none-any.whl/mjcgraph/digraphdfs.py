#!/usr/local/bin/python3

import sys

class DirectedDFSearch():
    def __init__(self, Digraph, s):
        self.marked = [False for i in range(Digraph.V)]
        self.edgeTo = [-1 for i in range(Digraph.V)]
        self.s = s
        self.dfs(Digraph, s)


    def dfs(self, Digraph, v):
        self.marked[v] = True
        for w in Digraph.adj(v):
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(Digraph, w)

    def marked(self, v):
        return self.marked[v]


    def has_path_to(self, v):
        return self.marked[v]


    def path_to(self, v):
        path = []
        if not self.has_path_to(v):
            return path
        x = v
        while x != self.s:
            path.append(x)
            x = self.edgeTo[x]
        path.append(self.s)
        return path

    def count(self):
        return sum([1 for x in self.marked if x == True]) - 1
