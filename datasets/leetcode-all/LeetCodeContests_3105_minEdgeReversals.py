from typing import List

def minEdgeReversals(n: int, edges: List[List[int]]) -> List[int]:
    """
    There is a simple directed graph with n nodes labeled from 0 to n - 1. The graph would form a tree if its edges were bi-directional.
    
    You are given an integer n and a 2D integer array edges, where edges[i] = [ui, vi] represents a directed edge going from node ui to node vi.
    
    An edge reversal changes the direction of an edge, i.e., a directed edge going from node ui to node vi becomes a directed edge going from node vi to node ui.
    
    For every node i in the range [0, n - 1], your task is to independently calculate the minimum number of edge reversals required so it is possible to reach any other node starting from node i through a sequence of directed edges.
    
    Return an integer array answer, where answer[i] is the minimum number of edge reversals required so it is possible to reach any other node starting from node i through a sequence of directed edges.
    
    Example 1:
    
    [https://assets.leetcode.com/uploads/2023/08/26/image-20230826221104-3.png]
    
    Input: n = 4, edges = [[2,0],[2,1],[1,3]]
    Output: [1,1,0,2]
    Explanation: The image above shows the graph formed by the edges.
    For node 0: after reversing the edge [2,0], it is possible to reach any other node starting from node 0.
    So, answer[0] = 1.
    For node 1: after reversing the edge [2,1], it is possible to reach any other node starting from node 1.
    So, answer[1] = 1.
    For node 2: it is already possible to reach any other node starting from node 2.
    So, answer[2] = 0.
    For node 3: after reversing the edges [1,3] and [2,1], it is possible to reach any other node starting from node 3.
    So, answer[3] = 2.
    
    Example 2:
    
    [https://assets.leetcode.com/uploads/2023/08/26/image-20230826225541-2.png]
    
    Input: n = 3, edges = [[1,2],[2,0]]
    Output: [2,0,1]
    Explanation: The image above shows the graph formed by the edges.
    For node 0: after reversing the edges [2,0] and [1,2], it is possible to reach any other node starting from node 0.
    So, answer[0] = 2.
    For node 1: it is already possible to reach any other node starting from node 1.
    So, answer[1] = 0.
    For node 2: after reversing the edge [1, 2], it is possible to reach any other node starting from node 2.
    So, answer[2] = 1.
    
    
    Constraints:
    
     * 2 <= n <= 105
     * edges.length == n - 1
     * edges[i].length == 2
     * 0 <= ui == edges[i][0] < n
     * 0 <= vi == edges[i][1] < n
     * ui != vi
     * The input is generated such that if the edges were bi-directional, the graph would be a tree.
    """
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(4, [[2, 0], [2, 1], [1, 3]]) == [1,1,0,2]
    assert candidate(3, [[1, 2], [2, 0]]) == [2,0,1]
    assert candidate(2, [[0, 1]]) == [0,1]
    assert candidate(3, [[2, 0], [2, 1]]) == [1,1,0]
    assert candidate(4, [[0, 1], [3, 0], [2, 3]]) == [2,3,0,1]
    assert candidate(4, [[0, 2], [0, 3], [3, 1]]) == [0,2,1,1]
    assert candidate(4, [[0, 3], [1, 2], [2, 3]]) == [2,1,2,3]
    assert candidate(4, [[0, 3], [1, 2], [3, 1]]) == [0,2,3,1]
    assert candidate(4, [[0, 3], [2, 1], [3, 1]]) == [1,3,2,2]
    assert candidate(4, [[1, 0], [2, 0], [3, 2]]) == [3,2,2,1]
    assert candidate(5, [[0, 1], [0, 4], [2, 3], [4, 2]]) == [0,1,2,3,1]
    assert candidate(5, [[0, 1], [2, 0], [0, 4], [3, 4]]) == [2,3,1,2,3]
    assert candidate(5, [[0, 2], [0, 1], [3, 1], [4, 1]]) == [2,3,3,2,2]
    assert candidate(5, [[0, 2], [0, 1], [3, 1], [4, 3]]) == [2,3,3,2,1]
    assert candidate(5, [[0, 2], [1, 3], [1, 4], [2, 4]]) == [1,2,2,3,3]
    assert candidate(5, [[0, 2], [1, 3], [2, 3], [4, 2]]) == [2,3,3,4,2]
    assert candidate(5, [[0, 2], [2, 1], [2, 3], [4, 3]]) == [1,3,2,3,2]
    assert candidate(5, [[0, 3], [0, 4], [1, 2], [4, 1]]) == [0,2,3,1,1]
    assert candidate(5, [[1, 0], [3, 0], [0, 4], [2, 3]]) == [3,2,1,2,4]
    assert candidate(5, [[3, 0], [0, 4], [1, 3], [2, 3]]) == [3,1,1,2,4]
    assert candidate(6, [[0, 1], [0, 5], [1, 2], [3, 2], [2, 4]]) == [1,2,3,2,4,2]
    assert candidate(6, [[0, 1], [2, 1], [1, 5], [2, 3], [4, 3]]) == [2,3,2,3,2,4]
    assert candidate(6, [[0, 2], [0, 3], [0, 1], [0, 5], [1, 4]]) == [0,1,1,1,2,1]
    assert candidate(6, [[0, 2], [1, 3], [1, 2], [2, 4], [2, 5]]) == [1,1,2,2,3,3]
    assert candidate(6, [[0, 4], [1, 2], [3, 1], [5, 1], [4, 5]]) == [1,4,5,3,2,3]
    assert candidate(6, [[1, 0], [0, 4], [2, 4], [2, 3], [3, 5]]) == [2,1,2,3,3,4]
    assert candidate(6, [[1, 0], [3, 1], [1, 4], [2, 5], [4, 5]]) == [3,2,3,1,3,4]
    assert candidate(7, [[0, 5], [2, 0], [1, 3], [6, 2], [4, 3], [3, 5]]) == [5,4,4,5,4,6,3]
    assert candidate(7, [[0, 6], [2, 1], [6, 1], [2, 5], [5, 3], [6, 4]]) == [1,3,2,4,3,3,2]
    assert candidate(7, [[5, 0], [2, 0], [6, 1], [2, 4], [2, 3], [3, 6]]) == [2,4,1,2,2,1,3]
    assert candidate(8, [[0, 4], [0, 3], [7, 0], [1, 4], [2, 5], [2, 3], [6, 5]]) == [4,4,4,5,5,5,4,3]
    assert candidate(8, [[0, 5], [1, 0], [1, 6], [1, 2], [2, 3], [2, 7], [4, 7]]) == [2,1,2,3,2,3,2,3]
    assert candidate(8, [[1, 0], [7, 1], [2, 6], [5, 2], [3, 6], [5, 4], [5, 7]]) == [4,3,2,2,2,1,3,2]
    assert candidate(8, [[2, 0], [5, 0], [3, 1], [1, 4], [6, 2], [4, 5], [7, 5]]) == [7,4,6,3,5,6,5,5]
    assert candidate(8, [[4, 0], [0, 1], [1, 3], [3, 2], [6, 2], [2, 7], [5, 7]]) == [3,4,6,5,2,6,5,7]
    assert candidate(8, [[4, 0], [7, 1], [2, 3], [7, 2], [5, 3], [4, 6], [7, 6]]) == [3,3,3,4,2,3,3,2]
    assert candidate(9, [[0, 5], [0, 2], [0, 7], [0, 4], [7, 1], [3, 2], [6, 3], [8, 4]]) == [3,5,4,3,4,4,2,4,3]
    assert candidate(9, [[0, 5], [0, 6], [0, 2], [5, 1], [7, 2], [4, 2], [3, 6], [8, 4]]) == [4,6,5,4,4,5,5,4,3]
    assert candidate(9, [[0, 5], [7, 0], [1, 6], [1, 3], [2, 8], [3, 4], [3, 7], [7, 8]]) == [4,1,3,2,3,5,2,3,4]
    assert candidate(9, [[2, 0], [1, 6], [1, 5], [2, 3], [2, 5], [4, 5], [5, 7], [8, 7]]) == [4,3,3,4,3,4,4,5,4]
    assert candidate(9, [[7, 0], [0, 6], [1, 2], [2, 6], [3, 6], [4, 5], [5, 8], [8, 6]]) == [7,6,7,7,5,6,8,6,7]
    assert candidate(10, [[0, 1], [0, 2], [2, 4], [6, 2], [3, 9], [5, 4], [4, 8], [5, 7], [9, 6]]) == [4,5,5,2,6,5,4,6,7,3]
    assert candidate(10, [[0, 3], [0, 5], [0, 1], [8, 1], [6, 1], [2, 3], [4, 6], [9, 4], [5, 7]]) == [5,6,5,6,4,6,5,7,5,3]
    assert candidate(10, [[0, 5], [1, 3], [1, 9], [2, 7], [4, 2], [6, 3], [3, 4], [5, 4], [7, 8]]) == [3,3,6,4,5,4,3,7,8,4]
    assert candidate(10, [[1, 0], [0, 5], [6, 0], [2, 3], [4, 2], [2, 6], [8, 2], [2, 9], [8, 7]]) == [5,4,3,4,2,6,4,3,2,4]
    assert candidate(10, [[6, 0], [7, 0], [4, 1], [1, 9], [2, 7], [9, 2], [3, 7], [5, 7], [8, 9]]) == [9,5,7,7,4,7,8,8,5,6]
    assert candidate(10, [[7, 0], [1, 2], [1, 9], [2, 3], [2, 8], [5, 3], [4, 6], [6, 7], [7, 9]]) == [5,4,5,6,2,5,3,4,6,5]
    assert candidate(10, [[7, 0], [1, 5], [2, 6], [8, 2], [7, 3], [4, 5], [5, 6], [9, 7], [8, 9]]) == [6,3,4,6,3,4,5,5,3,4]
    assert candidate(11, [[0, 1], [1, 2], [8, 1], [2, 4], [3, 9], [3, 7], [6, 4], [5, 7], [5, 6], [10, 8]]) == [5,6,7,6,8,6,7,7,5,7,4]
    assert candidate(11, [[0, 3], [0, 2], [1, 4], [1, 5], [2, 9], [3, 5], [7, 6], [7, 9], [7, 8], [8, 10]]) == [2,3,3,3,4,4,4,3,4,4,5]
    assert candidate(11, [[0, 3], [0, 7], [0, 9], [0, 10], [1, 4], [4, 2], [2, 6], [6, 3], [5, 6], [7, 8]]) == [5,2,4,6,3,4,5,6,7,6,6]
    assert candidate(11, [[2, 0], [0, 9], [1, 5], [2, 8], [3, 5], [3, 8], [9, 4], [9, 6], [6, 10], [7, 10]]) == [4,3,3,3,6,4,6,6,4,5,7]
    assert candidate(11, [[6, 0], [0, 1], [1, 4], [2, 8], [9, 3], [4, 10], [5, 8], [5, 6], [6, 9], [10, 7]]) == [3,4,1,4,5,1,2,7,2,3,6]
    assert candidate(11, [[7, 0], [1, 0], [1, 6], [5, 1], [4, 2], [8, 2], [9, 2], [7, 3], [5, 9], [10, 5]]) == [6,5,6,6,5,4,6,5,5,5,3]
    assert candidate(11, [[8, 0], [6, 1], [7, 1], [1, 10], [3, 2], [4, 3], [3, 8], [5, 8], [8, 9], [9, 10]]) == [7,7,6,5,4,5,6,6,6,7,8]
    assert candidate(11, [[10, 0], [1, 2], [1, 10], [2, 8], [3, 9], [3, 5], [4, 6], [7, 4], [4, 8], [5, 8]]) == [6,4,5,4,5,5,6,4,6,5,5]
    assert candidate(12, [[0, 10], [1, 3], [1, 10], [2, 7], [2, 11], [3, 4], [5, 9], [5, 11], [6, 9], [9, 8], [9, 10]]) == [5,5,4,6,7,4,4,5,6,5,6,5]
    assert candidate(12, [[3, 0], [10, 0], [6, 0], [1, 9], [3, 2], [4, 6], [4, 7], [5, 11], [11, 7], [8, 10], [9, 11]]) == [9,5,9,8,7,6,8,8,7,6,8,7]
    assert candidate(12, [[4, 0], [11, 0], [1, 9], [1, 3], [6, 2], [2, 7], [2, 3], [3, 10], [4, 10], [5, 6], [10, 8]]) == [7,5,5,6,6,3,4,6,8,6,7,6]
    assert candidate(12, [[10, 0], [0, 3], [1, 6], [1, 8], [1, 5], [2, 3], [2, 4], [3, 5], [4, 7], [4, 11], [10, 9]]) == [3,4,3,4,4,5,5,5,5,3,2,5]
    assert candidate(13, [[0, 5], [1, 10], [2, 4], [2, 7], [10, 2], [3, 5], [5, 12], [11, 6], [6, 12], [8, 10], [8, 11], [10, 9]]) == [5,4,6,5,7,6,6,7,4,6,5,5,7]
    assert candidate(13, [[0, 11], [1, 4], [1, 8], [1, 3], [3, 2], [10, 3], [12, 3], [12, 5], [6, 11], [10, 7], [9, 10], [11, 12]]) == [4,6,8,7,7,7,4,7,7,5,6,5,6]
    assert candidate(13, [[5, 0], [0, 2], [0, 9], [10, 1], [6, 1], [7, 2], [2, 6], [3, 7], [8, 4], [4, 11], [4, 12], [9, 12]]) == [6,9,7,5,7,5,8,6,6,7,8,8,8]
    assert candidate(13, [[7, 0], [3, 1], [2, 4], [2, 8], [10, 2], [3, 10], [9, 5], [5, 7], [6, 11], [6, 12], [12, 7], [10, 12]]) == [7,4,5,3,6,5,4,6,6,4,4,5,5]
    assert candidate(14, [[0, 1], [0, 7], [2, 6], [2, 8], [11, 3], [4, 12], [4, 11], [5, 10], [7, 11], [13, 7], [8, 10], [10, 9], [9, 12]]) == [7,8,5,10,8,6,6,8,6,8,7,9,9,7]
    assert candidate(14, [[0, 1], [1, 2], [2, 8], [9, 2], [6, 2], [13, 2], [3, 4], [5, 4], [7, 5], [6, 10], [12, 6], [11, 7], [11, 10]]) == [6,7,8,9,10,9,7,8,9,7,8,7,6,7]
    assert candidate(14, [[0, 2], [0, 3], [0, 13], [1, 3], [2, 4], [8, 2], [11, 3], [12, 3], [4, 6], [5, 7], [7, 9], [7, 11], [10, 12]]) == [7,7,8,8,9,5,10,6,7,7,6,7,7,8]
    assert candidate(14, [[0, 4], [0, 8], [1, 3], [1, 13], [2, 9], [4, 11], [4, 12], [5, 11], [8, 6], [13, 6], [7, 9], [7, 8], [10, 8]]) == [6,6,6,7,7,7,8,6,7,7,6,8,8,7]
    assert candidate(14, [[0, 6], [5, 0], [2, 0], [12, 1], [13, 2], [12, 3], [4, 7], [5, 7], [7, 12], [8, 13], [9, 11], [9, 10], [10, 13]]) == [7,9,6,9,6,6,8,7,4,3,4,4,8,5]
    assert candidate(14, [[0, 9], [0, 11], [0, 5], [1, 6], [1, 11], [7, 2], [3, 5], [3, 12], [3, 13], [11, 4], [6, 10], [9, 7], [11, 8]]) == [2,2,5,2,4,3,3,4,4,3,4,3,3,3]
    assert candidate(14, [[0, 11], [1, 2], [1, 10], [1, 6], [3, 6], [4, 11], [10, 4], [5, 12], [13, 6], [8, 7], [8, 9], [8, 12], [8, 13]]) == [7,5,6,5,7,4,6,5,4,5,6,8,5,5]
    assert candidate(14, [[1, 0], [1, 8], [7, 2], [2, 11], [2, 13], [3, 9], [8, 3], [3, 11], [4, 12], [4, 8], [5, 11], [6, 10], [10, 12]]) == [7,6,8,8,6,8,5,7,7,9,6,9,7,9]
    assert candidate(14, [[1, 0], [11, 0], [6, 0], [7, 2], [2, 8], [10, 3], [4, 10], [5, 12], [12, 6], [13, 6], [7, 10], [9, 8], [8, 12]]) == [11,10,7,8,6,8,10,6,8,7,7,10,9,9]
    assert candidate(14, [[3, 0], [5, 0], [0, 7], [1, 8], [1, 4], [12, 2], [4, 3], [10, 3], [12, 5], [13, 6], [7, 13], [9, 10], [10, 11]]) == [7,4,6,6,5,6,10,8,5,4,5,6,5,9]
    assert candidate(15, [[0, 5], [1, 9], [4, 1], [1, 5], [14, 1], [2, 5], [4, 3], [4, 6], [5, 11], [5, 7], [10, 6], [7, 8], [13, 7], [14, 12]]) == [6,6,6,6,5,7,6,8,9,7,5,8,6,7,5]
    assert candidate(15, [[0, 6], [13, 0], [1, 2], [10, 1], [3, 12], [4, 11], [5, 12], [10, 7], [9, 7], [7, 13], [11, 8], [8, 9], [12, 11], [13, 14]]) == [10,8,9,3,4,3,11,8,6,7,7,5,4,9,10]
    assert candidate(15, [[0, 7], [12, 1], [5, 2], [4, 2], [3, 8], [3, 14], [12, 4], [4, 7], [5, 6], [10, 5], [11, 5], [6, 9], [7, 14], [13, 12]]) == [7,7,8,8,7,7,8,8,9,9,6,6,6,5,9]
    assert candidate(15, [[1, 0], [10, 1], [2, 8], [2, 3], [5, 3], [4, 8], [9, 5], [6, 12], [7, 12], [8, 7], [9, 11], [11, 10], [10, 13], [10, 14]]) == [7,6,4,5,4,4,6,6,5,3,5,4,7,6,6]
    assert candidate(15, [[2, 0], [0, 7], [0, 5], [1, 6], [1, 7], [3, 4], [8, 4], [10, 4], [5, 12], [5, 10], [11, 7], [9, 13], [10, 14], [13, 14]]) == [7,7,6,9,10,8,8,8,9,8,9,7,9,9,10]
    assert candidate(15, [[8, 0], [1, 0], [1, 13], [1, 14], [9, 2], [3, 13], [4, 11], [4, 14], [5, 8], [12, 6], [9, 6], [7, 8], [14, 9], [10, 13]]) == [8,7,10,7,7,6,10,6,7,9,7,8,9,8,8]
    assert candidate(15, [[12, 0], [0, 8], [1, 3], [2, 1], [2, 7], [12, 2], [9, 3], [4, 11], [11, 5], [5, 7], [6, 13], [6, 9], [8, 14], [10, 12]]) == [7,8,7,9,5,7,7,8,8,8,5,6,6,8,9]
    assert candidate(15, [[12, 0], [1, 12], [1, 7], [2, 12], [3, 7], [3, 14], [4, 6], [5, 6], [5, 7], [6, 8], [6, 10], [11, 6], [7, 13], [9, 14]]) == [8,6,6,6,6,6,7,7,8,6,8,6,7,8,7]
    assert candidate(16, [[0, 1], [5, 0], [0, 2], [0, 4], [2, 12], [10, 3], [3, 15], [4, 7], [8, 6], [6, 9], [7, 14], [7, 13], [11, 9], [13, 9], [10, 13]]) == [5,6,6,8,6,4,8,7,7,9,7,8,7,8,8,9]
    assert candidate(16, [[2, 0], [0, 4], [4, 1], [1, 11], [5, 2], [8, 3], [4, 3], [4, 13], [14, 4], [7, 5], [5, 12], [6, 9], [12, 9], [10, 14], [11, 15]]) == [7,9,6,9,8,5,6,4,8,7,6,10,6,9,7,11]
    assert candidate(16, [[8, 0], [1, 6], [10, 1], [8, 2], [3, 15], [14, 4], [12, 5], [13, 5], [8, 6], [6, 9], [6, 13], [11, 7], [7, 13], [15, 10], [11, 14]]) == [8,7,8,4,9,10,8,8,7,9,6,7,9,9,8,5]
    assert candidate(17, [[0, 4], [0, 9], [13, 1], [5, 1], [6, 2], [13, 2], [3, 8], [3, 15], [3, 9], [4, 5], [5, 10], [11, 6], [7, 16], [12, 9], [16, 9], [12, 14]]) == [7,10,10,7,8,9,9,6,8,8,10,8,7,9,8,8,7]
    assert candidate(17, [[0, 7], [15, 1], [2, 3], [2, 7], [3, 8], [15, 3], [5, 4], [4, 16], [6, 14], [16, 7], [16, 9], [10, 14], [10, 16], [16, 11], [12, 14], [15, 13]]) == [8,9,8,9,7,6,7,9,10,9,7,9,7,9,8,8,8]
    assert candidate(17, [[0, 10], [12, 0], [0, 14], [0, 7], [0, 16], [1, 8], [1, 7], [2, 8], [3, 5], [4, 15], [5, 9], [11, 5], [14, 6], [11, 7], [15, 8], [13, 16]]) == [8,8,8,8,7,9,10,9,9,10,9,8,7,8,9,8,9]
    assert candidate(17, [[0, 12], [1, 2], [1, 13], [1, 14], [4, 3], [3, 15], [5, 4], [10, 6], [14, 6], [6, 15], [7, 11], [8, 11], [13, 9], [10, 11], [15, 12], [16, 15]]) == [11,8,9,10,9,8,10,9,9,10,9,10,12,9,9,11,10]
    assert candidate(17, [[0, 13], [15, 0], [1, 5], [1, 6], [11, 1], [1, 13], [8, 2], [3, 16], [4, 16], [7, 14], [11, 8], [9, 10], [9, 16], [14, 12], [14, 15], [15, 16]]) == [8,8,9,7,7,9,9,5,8,7,8,7,7,9,6,7,8]
    assert candidate(17, [[8, 0], [0, 10], [6, 1], [1, 15], [15, 2], [3, 2], [12, 3], [9, 4], [5, 7], [13, 7], [9, 10], [10, 11], [10, 14], [13, 12], [16, 12], [14, 15]]) == [9,11,13,12,10,10,10,11,8,9,10,11,11,10,11,12,10]
    assert candidate(17, [[10, 0], [0, 5], [1, 8], [1, 16], [7, 2], [2, 8], [3, 5], [8, 3], [4, 11], [13, 4], [16, 6], [16, 9], [14, 12], [14, 13], [14, 15], [15, 16]]) == [8,6,6,8,7,9,8,5,7,8,7,8,6,6,5,6,7]
    assert candidate(18, [[0, 3], [16, 1], [1, 10], [2, 13], [2, 8], [14, 3], [4, 12], [5, 10], [13, 6], [7, 11], [10, 7], [9, 7], [14, 8], [9, 8], [9, 17], [12, 14], [13, 15]]) == [9,8,9,10,7,8,11,10,10,9,9,11,8,10,9,11,7,10]
    assert candidate(18, [[0, 10], [0, 17], [1, 3], [1, 2], [2, 9], [2, 17], [16, 3], [4, 7], [4, 13], [4, 6], [5, 12], [5, 17], [6, 17], [8, 15], [11, 8], [16, 11], [13, 14]]) == [6,5,6,6,5,6,6,6,7,7,7,6,7,6,7,8,5,7]
    assert candidate(18, [[11, 0], [5, 1], [1, 10], [1, 3], [1, 17], [14, 2], [2, 13], [3, 13], [4, 7], [4, 12], [4, 17], [6, 17], [7, 8], [15, 9], [16, 11], [11, 14], [14, 15]]) == [7,7,8,8,7,6,7,8,9,9,8,6,8,9,7,8,5,8]
    assert candidate(19, [[0, 3], [0, 5], [4, 0], [12, 1], [1, 5], [2, 17], [2, 4], [3, 13], [4, 8], [5, 7], [18, 6], [18, 8], [14, 9], [9, 15], [16, 9], [10, 12], [11, 17], [12, 16]]) == [8,8,6,9,7,9,8,10,8,9,6,6,7,10,8,10,8,7,7]
    assert candidate(19, [[0, 5], [0, 9], [14, 1], [2, 11], [3, 12], [3, 8], [10, 3], [4, 13], [4, 12], [6, 17], [10, 7], [7, 14], [8, 11], [16, 8], [9, 14], [9, 17], [15, 17], [15, 18]]) == [7,10,9,8,8,8,8,8,9,8,7,10,9,9,9,8,8,9,9]
    assert candidate(19, [[0, 12], [13, 1], [12, 1], [14, 2], [2, 11], [3, 9], [11, 3], [15, 4], [4, 11], [5, 12], [17, 6], [8, 7], [8, 10], [16, 8], [9, 12], [11, 18], [16, 18], [17, 18]]) == [11,13,8,10,8,11,10,11,10,11,11,9,12,12,7,7,9,9,10]
    assert candidate(19, [[0, 18], [8, 1], [5, 1], [9, 2], [6, 2], [3, 11], [17, 3], [4, 12], [4, 6], [18, 4], [14, 5], [5, 16], [6, 7], [16, 7], [17, 7], [15, 8], [10, 14], [14, 13]]) == [8,11,12,12,10,10,11,12,10,11,8,13,11,10,9,9,11,11,9]
    assert candidate(19, [[1, 0], [0, 13], [15, 0], [1, 9], [5, 2], [2, 13], [3, 12], [3, 16], [4, 12], [5, 7], [8, 6], [12, 8], [16, 10], [13, 10], [17, 11], [13, 11], [14, 13], [15, 18]]) == [9,8,9,9,9,8,12,9,11,9,11,11,10,10,9,8,10,10,9]


def test_check():
    check(minEdgeReversals)


### Metadata below ###
# question_id = 3105
# question_title = Minimum Edge Reversals So Every Node Is Reachable
# question_title_slug = minimum-edge-reversals-so-every-node-is-reachable
# question_difficulty = Hard
# question_category = Algorithms
# question_likes = 227
# question_dislikes = 3