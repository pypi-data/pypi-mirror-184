#!/usr/local/bin/python3

from src.mjcgraph import graph
from src.mjcgraph import dfs
from src.mjcgraph import draw

import unittest

class TestDFSearch(unittest.TestCase):

    def test_test(self):
        G = graph.Graph('data/mediumG.txt')

        dfsearch = dfs.DFSearch(G, 0)
        self.assertTrue(dfsearch.has_path_to(200))

        self.assertTrue(len(dfsearch.path_to(0)) == 1)
        self.assertEqual(len(dfsearch.path_to(200)), 71)


if __name__ == '__main__':
    unittest.main()
