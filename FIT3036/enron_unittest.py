from degree_centrality import degree, weighted_degree
from closeness_centrality import closeness
from eigenvector_centrality import eigenvector
import unittest

class TestCentralityMetrics(unittest.TestCase):
    def test_closeness_j(self):
        test_table = [[1, 2, 5], [0, 2, 4], [1, 1, 3, 4, 5], [2, 4, 5], [1, 2, 3], [0, 2, 3]]

        result = closeness(test_table)
        for i in range(len(result)):
            result[i] = result[i][1]
        self.assertEqual(result, [0.8333333333333334,
                                  0.7142857142857143,
                                  0.7142857142857143,
                                  0.7142857142857143,
                                  0.7142857142857143,
                                  0.7142857142857143])

    def test_degree(self):
        test1 = [[1,2,5],[0,2,4],[0,1,3,4,5],[2,4,5],[1,2,3],[0,2,3]]
        test2 = []
        test3 = [[]]

        self.assertEqual(degree(test1), [3,3,5,3,3,3])
        # Empty graph
        self.assertEqual(degree(test2), [])
        # Graph with no edges
        self.assertEqual(degree(test3), [0])

    def test_weighted_degree(self):
        test_table = [[1, 2, 5], [0, 2, 4], [0, 1, 3, 4, 5], [2, 4, 5], [1, 2, 3], [0, 2, 3]]
        test_matrix = [[0, 2, 1, 0, 0, 1],
                       [1, 0, 1, 0, 3, 0],
                       [1, 1, 0, 1, 1, 1],
                       [0, 0, 4, 0, 1, 1],
                       [0, 1, 1, 1, 0, 0],
                       [1, 0, 1, 1, 0, 0]]

        # Same as degree (alpha = 0)
        result = weighted_degree(test_table, test_matrix, 0)
        for i in range(len(result)):
            result[i] = result[i][1]
        self.assertEqual(result, [5,3,3,3,3,3])

        # Same as edge weights (alpha = 1)
        result = weighted_degree(test_table, test_matrix, 1)
        for i in range(len(result)):
            result[i] = result[i][1]
        self.assertEqual(result, [13,9,9,8,7,6])

        # Mix of degree and weight (alpha = 0.5)
        result = weighted_degree(test_table, test_matrix, 0.5)
        for i in range(len(result)):
            result[i] = result[i][1]
        self.assertEqual(result, [8.06225774829855,
                                  5.196152422706632,
                                  5.196152422706632,
                                  4.898979485566357,
                                  4.58257569495584,
                                  4.242640687119285])

    def test_eigenvector(self):
        test_table = [[1, 2, 5], [0, 2, 4], [1, 1, 3, 4, 5], [2, 4, 5], [1, 2, 3], [0, 2, 3]]
        test_matrix = [[0, 2, 1, 0, 0, 1],
                       [1, 0, 1, 0, 3, 0],
                       [1, 1, 0, 1, 1, 1],
                       [0, 0, 4, 0, 1, 1],
                       [0, 1, 1, 1, 0, 0],
                       [1, 0, 1, 1, 0, 0]]

        result = eigenvector(degree(test_table), test_matrix, 0.000001)
        for i in range(len(result)):
            result[i] = result[i][1]
        self.assertEqual(result, [0.5538629995078169,
                                  0.4466681701394005,
                                  0.40542295448339855,
                                  0.35907684386178224,
                                  0.32181903803691775,
                                  0.3112103444581005])

if __name__ == '__main__':
    unittest.main(exit=False)
