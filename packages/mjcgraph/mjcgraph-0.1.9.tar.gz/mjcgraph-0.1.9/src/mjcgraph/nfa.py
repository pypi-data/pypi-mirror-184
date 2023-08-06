#!/usr/local/bin/python3

import sys
from mjcgraph import digraph
from collections import deque

class NFA():
    def __init__(self, regexp):
        self.re = regexp.strip()
        self.M = len(self.re)
        self.G = digraph.Digraph(self.M + 1)
        ops = deque()

        for i in range(self.M):
            print(f'i: {i}, re[{i}]: {self.re[i]}')
            lp = i
            if self.re[i] == '(' or self.re[i] == '|':
                ops.append(i)
            elif self.re[i] == ')':
                opr = ops.pop()
                if self.re[opr] == '|':
                    lp = ops.pop()
                    self.G.add_edge(lp, opr+1)
                    self.G.add_edge(opr, i)
                else:
                    lp = opr
            if i < self.M-1 and self.re[i+1] == '*':
                print('*')
                self.G.add_edge(lp, i+1)
                self.G.add_edge(i+1, lp)
            if self.re[i] == '(' or self.re[i] == '*' or self.re[i] == ')':
                self.G.add_edge(i, i+1)

            print(ops)


    def recognizes(self, text):
        pass




if __name__ == '__main__':
    nfa = NFA('((A*B|AC)D)')
    print(nfa.re)
    print(nfa.M)
    assert nfa.M == 11
    print(nfa.G.to_string())
