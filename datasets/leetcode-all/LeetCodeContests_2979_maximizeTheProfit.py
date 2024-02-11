from typing import List

def maximizeTheProfit(n: int, offers: List[List[int]]) -> int:
    """
    You are given an integer n representing the number of houses on a number line, numbered from 0 to n - 1.
    
    Additionally, you are given a 2D integer array offers where offers[i] = [starti, endi, goldi], indicating that ith buyer wants to buy all the houses from starti to endi for goldi amount of gold.
    
    As a salesman, your goal is to maximize your earnings by strategically selecting and selling houses to buyers.
    
    Return the maximum amount of gold you can earn.
    
    Note that different buyers can't buy the same house, and some houses may remain unsold.
    
    Example 1:
    
    Input: n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]]
    Output: 3
    Explanation: There are 5 houses numbered from 0 to 4 and there are 3 purchase offers.
    We sell houses in the range [0,0] to 1st buyer for 1 gold and houses in the range [1,3] to 3rd buyer for 2 golds.
    It can be proven that 3 is the maximum amount of gold we can achieve.
    
    Example 2:
    
    Input: n = 5, offers = [[0,0,1],[0,2,10],[1,3,2]]
    Output: 10
    Explanation: There are 5 houses numbered from 0 to 4 and there are 3 purchase offers.
    We sell houses in the range [0,2] to 2nd buyer for 10 golds.
    It can be proven that 10 is the maximum amount of gold we can achieve.
    
    
    Constraints:
    
     * 1 <= n <= 105
     * 1 <= offers.length <= 105
     * offers[i].length == 3
     * 0 <= starti <= endi <= n - 1
     * 1 <= goldi <= 103
    """
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(5, [[0, 0, 1], [0, 2, 2], [1, 3, 2]]) == 3
    assert candidate(5, [[0, 0, 1], [0, 2, 10], [1, 3, 2]]) == 10
    assert candidate(4, [[1, 3, 10], [1, 3, 3], [0, 0, 1], [0, 0, 7]]) == 17
    assert candidate(4, [[0, 0, 6], [1, 2, 8], [0, 3, 7], [2, 2, 5], [0, 1, 5], [2, 3, 2], [0, 2, 8], [2, 3, 10], [0, 3, 2]]) == 16
    assert candidate(15, [[5, 5, 10], [2, 6, 6], [8, 11, 5], [7, 11, 9], [2, 4, 1], [3, 8, 5], [0, 6, 9], [0, 10, 5], [5, 10, 8], [4, 5, 1]]) == 20
    assert candidate(10, [[1, 6, 1], [0, 1, 10], [3, 6, 2], [0, 5, 10], [0, 0, 3], [0, 0, 4], [1, 1, 4], [0, 6, 7], [4, 4, 1]]) == 12
    assert candidate(11, [[7, 8, 6], [6, 6, 4], [4, 6, 9], [6, 7, 4], [5, 5, 8], [1, 5, 9], [7, 7, 8], [1, 2, 5], [0, 2, 9], [1, 3, 8], [0, 2, 7], [2, 2, 8]]) == 29
    assert candidate(3, [[0, 0, 6], [0, 1, 8], [1, 2, 1], [0, 1, 4], [0, 1, 2], [0, 0, 7], [0, 0, 6], [0, 0, 5]]) == 8
    assert candidate(4, [[0, 1, 9], [1, 1, 4]]) == 9
    assert candidate(11, [[1, 10, 6], [1, 10, 5], [0, 2, 7], [0, 0, 8], [8, 10, 7]]) == 15
    assert candidate(3, [[0, 1, 8], [1, 1, 6], [2, 2, 7], [0, 2, 6], [0, 2, 2], [0, 0, 6], [0, 0, 9], [0, 1, 4]]) == 22
    assert candidate(6, [[0, 2, 4]]) == 4
    assert candidate(10, [[5, 9, 3], [1, 5, 8], [0, 0, 6], [5, 8, 10]]) == 16
    assert candidate(5, [[1, 1, 3], [1, 1, 3], [0, 0, 8], [1, 3, 8], [0, 2, 1], [3, 3, 9], [0, 0, 7], [0, 2, 3], [0, 0, 5], [0, 3, 10], [1, 3, 10], [4, 4, 6], [0, 1, 1], [2, 4, 10]]) == 26
    assert candidate(13, [[2, 2, 5], [1, 8, 10], [2, 3, 3]]) == 10
    assert candidate(2, [[1, 1, 8], [1, 1, 8], [1, 1, 10], [1, 1, 7], [0, 0, 7], [0, 0, 3], [0, 1, 8], [0, 0, 4], [0, 0, 4], [0, 0, 7], [0, 0, 10], [0, 1, 4], [1, 1, 1], [0, 1, 5]]) == 20
    assert candidate(3, [[0, 1, 7], [1, 1, 3], [0, 0, 2], [1, 1, 6], [0, 0, 10], [1, 1, 7], [0, 2, 3], [0, 1, 2], [0, 0, 7]]) == 17
    assert candidate(5, [[0, 0, 5], [1, 3, 9], [0, 2, 2], [1, 1, 6], [1, 2, 10], [0, 2, 10], [1, 1, 3]]) == 15
    assert candidate(10, [[0, 1, 9], [5, 6, 10], [1, 3, 8], [1, 9, 7], [7, 8, 1], [2, 7, 1], [0, 8, 7], [1, 6, 6], [1, 4, 4], [0, 5, 4], [0, 0, 3], [0, 8, 6]]) == 22
    assert candidate(4, [[0, 0, 1], [0, 0, 10], [0, 2, 1], [0, 0, 6], [0, 3, 10], [0, 1, 5], [1, 2, 10], [0, 0, 2], [3, 3, 1], [0, 0, 9], [0, 1, 2], [0, 0, 4], [1, 3, 5], [1, 1, 1]]) == 21
    assert candidate(9, [[0, 3, 10], [5, 6, 5], [1, 5, 2], [1, 8, 9], [1, 1, 9], [1, 7, 1], [3, 7, 9], [2, 3, 2], [4, 6, 1], [4, 5, 7], [2, 2, 2], [6, 8, 10], [1, 3, 10], [1, 4, 10]]) == 28
    assert candidate(10, [[0, 2, 2]]) == 2
    assert candidate(10, [[2, 7, 4], [2, 4, 9], [1, 8, 7], [0, 4, 3]]) == 9
    assert candidate(6, [[0, 1, 4], [1, 2, 4], [0, 1, 10], [1, 2, 4], [2, 2, 5], [1, 1, 8], [2, 3, 2], [4, 4, 4], [0, 0, 3]]) == 20
    assert candidate(1, [[0, 0, 8], [0, 0, 3], [0, 0, 8], [0, 0, 8], [0, 0, 5], [0, 0, 9], [0, 0, 6], [0, 0, 1], [0, 0, 8], [0, 0, 1], [0, 0, 5], [0, 0, 9], [0, 0, 2]]) == 9
    assert candidate(15, [[8, 10, 5], [4, 12, 6], [6, 11, 7], [8, 11, 3], [7, 13, 1], [7, 7, 8], [8, 10, 5], [0, 11, 3], [1, 1, 9], [2, 11, 6], [3, 11, 8]]) == 22
    assert candidate(10, [[5, 6, 9], [0, 2, 9]]) == 18
    assert candidate(11, [[7, 9, 5], [0, 0, 8], [6, 6, 3], [4, 9, 1], [3, 7, 5], [0, 4, 7]]) == 16
    assert candidate(7, [[0, 2, 9], [2, 4, 8], [0, 3, 6], [4, 4, 10], [2, 2, 2], [1, 1, 10], [0, 0, 8], [4, 4, 9], [4, 4, 4], [3, 3, 5], [2, 5, 2], [0, 3, 6], [3, 4, 5]]) == 35
    assert candidate(9, [[3, 8, 1], [0, 6, 7], [0, 3, 6], [1, 6, 2], [2, 3, 10], [3, 3, 2], [1, 2, 2], [1, 3, 9], [0, 0, 7], [1, 2, 9], [5, 5, 4], [5, 6, 6], [1, 5, 5], [0, 1, 2], [0, 6, 1]]) == 24
    assert candidate(8, [[0, 0, 7], [0, 1, 8], [1, 1, 1], [2, 2, 7], [2, 3, 1]]) == 15
    assert candidate(8, [[6, 6, 5], [0, 1, 7], [1, 7, 10]]) == 12
    assert candidate(13, [[0, 9, 5], [6, 8, 7], [0, 0, 3], [4, 4, 2], [1, 9, 7], [9, 12, 9], [1, 2, 9], [1, 1, 10], [3, 3, 3], [0, 3, 3], [4, 8, 5], [0, 0, 9], [7, 10, 7]]) == 40
    assert candidate(11, [[2, 5, 1]]) == 1
    assert candidate(3, [[0, 0, 9], [0, 2, 6], [1, 1, 1], [1, 2, 10], [0, 0, 10], [0, 0, 4], [0, 2, 7], [0, 0, 1], [0, 0, 9], [2, 2, 5]]) == 20
    assert candidate(5, [[1, 1, 3], [1, 2, 1], [0, 2, 3], [1, 1, 10], [3, 3, 3], [2, 4, 3], [0, 3, 5], [4, 4, 2], [2, 3, 10], [3, 3, 8], [3, 3, 9], [0, 2, 8], [0, 2, 2], [1, 1, 3], [0, 0, 8]]) == 30
    assert candidate(13, [[6, 9, 3], [6, 9, 6], [5, 12, 10], [11, 12, 4], [4, 4, 2], [0, 7, 8], [2, 6, 6], [6, 6, 4]]) == 12
    assert candidate(3, [[0, 2, 9], [1, 1, 8], [0, 1, 1], [2, 2, 4], [2, 2, 1], [0, 0, 4], [1, 1, 9], [0, 0, 6], [0, 1, 7]]) == 19
    assert candidate(3, [[1, 2, 8], [0, 0, 1], [0, 1, 1], [0, 0, 3], [1, 2, 2], [0, 0, 7], [0, 0, 10], [1, 1, 6]]) == 18
    assert candidate(2, [[0, 0, 3], [1, 1, 10], [0, 1, 6]]) == 13
    assert candidate(3, [[0, 0, 9], [1, 1, 1], [0, 2, 7], [1, 1, 7], [1, 2, 6], [0, 0, 8], [0, 2, 3], [1, 2, 10], [2, 2, 3], [2, 2, 5]]) == 21
    assert candidate(5, [[2, 3, 2], [0, 1, 7], [0, 1, 1], [0, 0, 9], [2, 4, 1], [3, 4, 5], [1, 3, 10], [0, 0, 8]]) == 19
    assert candidate(15, [[4, 6, 9], [4, 10, 9], [3, 5, 4], [0, 2, 6], [3, 13, 7], [1, 11, 6], [1, 8, 4], [4, 12, 4], [3, 8, 8], [13, 13, 7], [4, 12, 3]]) == 22
    assert candidate(8, [[1, 5, 9], [0, 4, 9], [0, 0, 3], [1, 2, 9], [0, 0, 10], [4, 7, 9], [7, 7, 2], [0, 2, 6], [1, 1, 5], [1, 4, 3], [2, 4, 8], [0, 1, 1], [2, 3, 1]]) == 28
    assert candidate(4, [[0, 2, 7], [2, 3, 9], [2, 3, 2], [1, 2, 1], [1, 2, 9], [0, 3, 7], [0, 2, 9], [1, 2, 8], [0, 3, 10], [0, 3, 8], [0, 0, 5], [2, 2, 6]]) == 14
    assert candidate(12, [[0, 0, 4], [5, 8, 2], [2, 2, 10], [3, 5, 7], [1, 2, 1], [5, 7, 8], [8, 11, 3]]) == 25
    assert candidate(2, [[0, 0, 7], [0, 1, 3], [0, 0, 8]]) == 8
    assert candidate(4, [[2, 3, 8], [0, 1, 1], [3, 3, 2]]) == 9
    assert candidate(14, [[2, 12, 4], [7, 11, 4], [4, 4, 5], [0, 1, 6], [3, 4, 1], [4, 11, 9], [10, 12, 7], [7, 12, 1], [11, 11, 1], [0, 0, 5], [12, 12, 8], [6, 7, 6]]) == 26
    assert candidate(10, [[1, 4, 6], [7, 9, 9], [1, 4, 5], [8, 8, 2], [4, 7, 1], [6, 8, 8], [2, 3, 1], [0, 1, 4]]) == 15
    assert candidate(7, [[2, 5, 5], [1, 2, 9], [1, 3, 7], [2, 4, 3], [0, 0, 6], [0, 0, 1], [4, 4, 9], [1, 5, 7], [2, 2, 10]]) == 25
    assert candidate(11, [[0, 4, 10]]) == 10
    assert candidate(3, [[0, 1, 10], [1, 2, 2], [0, 2, 6], [0, 0, 1], [0, 0, 3], [0, 1, 8], [0, 0, 2], [2, 2, 8], [0, 0, 3], [2, 2, 3], [1, 2, 6], [0, 0, 4], [1, 2, 5]]) == 18
    assert candidate(14, [[11, 11, 4], [1, 11, 10], [11, 12, 2], [7, 8, 2]]) == 10
    assert candidate(2, [[0, 0, 1], [0, 0, 1], [1, 1, 9], [0, 0, 1], [1, 1, 2], [0, 1, 10]]) == 10
    assert candidate(6, [[0, 5, 6], [1, 2, 10], [0, 2, 4], [2, 4, 5], [4, 4, 6], [2, 2, 2], [0, 0, 7], [2, 5, 9], [2, 2, 3]]) == 23
    assert candidate(6, [[0, 0, 7], [2, 5, 5]]) == 12
    assert candidate(10, [[2, 3, 2], [0, 1, 6], [0, 0, 2], [1, 1, 5], [3, 3, 8], [2, 8, 7], [1, 7, 8], [0, 1, 4], [7, 7, 8], [1, 3, 7], [5, 5, 10], [2, 6, 6], [0, 0, 4], [5, 7, 4], [1, 9, 4]]) == 35
    assert candidate(10, [[0, 2, 4], [1, 4, 7], [0, 1, 10], [0, 5, 1]]) == 10
    assert candidate(12, [[0, 5, 6], [4, 10, 9], [7, 11, 10], [10, 11, 1], [6, 10, 1], [2, 2, 6]]) == 16
    assert candidate(11, [[3, 7, 8], [2, 7, 10], [3, 9, 3]]) == 10
    assert candidate(4, [[0, 0, 3], [0, 2, 6], [0, 0, 1], [1, 1, 2], [0, 2, 8], [1, 1, 3], [1, 3, 8], [1, 1, 10], [1, 2, 7], [1, 1, 8], [0, 0, 9]]) == 19
    assert candidate(1, [[0, 0, 9]]) == 9
    assert candidate(3, [[0, 1, 5], [0, 0, 5], [0, 0, 6], [0, 1, 6], [0, 2, 10], [1, 2, 6], [0, 0, 9], [1, 2, 9]]) == 18
    assert candidate(4, [[0, 0, 2], [2, 3, 9], [0, 1, 8], [0, 0, 9], [0, 0, 1], [3, 3, 9], [1, 2, 1], [1, 3, 5], [0, 1, 4], [0, 1, 4]]) == 19
    assert candidate(3, [[0, 0, 7], [2, 2, 1], [1, 1, 3], [0, 0, 3], [1, 1, 7], [0, 1, 5], [0, 2, 3], [1, 1, 5], [0, 1, 10], [1, 1, 5], [1, 1, 6], [0, 1, 3], [0, 0, 8], [1, 2, 7], [1, 1, 4]]) == 16
    assert candidate(14, [[5, 7, 2], [1, 5, 3], [11, 13, 2], [12, 12, 5], [4, 5, 6], [5, 10, 2], [4, 10, 8], [1, 1, 4], [4, 4, 2], [3, 7, 9], [5, 10, 1], [0, 3, 2]]) == 18
    assert candidate(11, [[1, 1, 5], [4, 4, 9], [0, 0, 1], [1, 3, 3], [3, 7, 4], [3, 9, 6], [7, 10, 2], [3, 7, 5], [4, 4, 8], [7, 8, 10], [1, 3, 7], [1, 4, 5], [0, 0, 10]]) == 36
    assert candidate(13, [[4, 9, 9], [1, 9, 8], [1, 9, 8], [0, 0, 8], [8, 11, 3], [2, 3, 6], [9, 9, 10], [5, 12, 1], [4, 6, 4]]) == 28
    assert candidate(5, [[2, 2, 7], [0, 2, 10], [2, 3, 10]]) == 10
    assert candidate(10, [[0, 4, 6], [1, 1, 1], [0, 5, 1], [1, 6, 3], [8, 9, 1], [2, 3, 7], [2, 3, 10], [1, 2, 1], [0, 0, 8], [3, 5, 5], [0, 0, 10]]) == 22
    assert candidate(4, [[0, 1, 1], [0, 0, 9], [1, 1, 8], [3, 3, 1], [1, 1, 5], [0, 0, 9], [0, 1, 9], [0, 0, 7], [2, 2, 2], [2, 3, 5], [1, 1, 10], [1, 2, 8]]) == 24
    assert candidate(7, [[0, 1, 9], [0, 1, 4], [0, 0, 3], [0, 0, 1], [1, 6, 5], [4, 6, 9], [4, 5, 7], [0, 0, 3], [1, 5, 9], [0, 2, 2]]) == 18
    assert candidate(12, [[8, 8, 6], [8, 8, 6], [1, 10, 7], [0, 0, 3], [9, 10, 7], [1, 7, 2], [1, 1, 1], [2, 3, 6], [0, 11, 1], [1, 8, 5], [1, 5, 7], [1, 2, 4], [9, 9, 5], [0, 3, 1]]) == 23
    assert candidate(15, [[5, 6, 3], [2, 2, 7], [0, 0, 5], [1, 7, 10], [11, 14, 5], [13, 14, 1], [2, 12, 1], [0, 4, 5], [0, 6, 2], [6, 9, 10], [3, 5, 2], [0, 1, 1], [1, 14, 1], [1, 6, 1]]) == 29
    assert candidate(7, [[1, 1, 5], [1, 1, 4], [0, 0, 9], [1, 1, 6], [0, 6, 4], [2, 6, 3], [2, 5, 9], [0, 6, 3], [0, 2, 1], [1, 1, 6], [4, 5, 5]]) == 24
    assert candidate(1, [[0, 0, 5], [0, 0, 3], [0, 0, 4], [0, 0, 8], [0, 0, 10], [0, 0, 6], [0, 0, 7], [0, 0, 7], [0, 0, 7], [0, 0, 3], [0, 0, 4], [0, 0, 5]]) == 10
    assert candidate(7, [[2, 2, 3], [2, 6, 4], [4, 6, 5], [0, 0, 4], [1, 1, 4], [2, 3, 1], [2, 4, 3], [0, 2, 8], [1, 3, 10], [1, 3, 2], [1, 6, 7], [0, 6, 9], [2, 2, 2], [1, 1, 9], [4, 4, 2]]) == 21
    assert candidate(12, [[0, 0, 7], [0, 2, 3], [0, 7, 2], [2, 3, 1], [2, 11, 6], [2, 10, 2], [1, 3, 6], [4, 7, 9], [7, 9, 3], [4, 6, 1], [5, 6, 8], [0, 2, 4], [0, 0, 3], [5, 5, 9], [2, 5, 3]]) == 25
    assert candidate(9, [[1, 8, 4], [5, 6, 5], [0, 2, 6], [4, 5, 4]]) == 11
    assert candidate(8, [[0, 4, 6], [2, 3, 6], [2, 5, 9], [2, 6, 7], [6, 6, 5], [4, 4, 4], [1, 1, 5], [2, 5, 7]]) == 20
    assert candidate(13, [[0, 6, 10]]) == 10
    assert candidate(6, [[0, 1, 2], [0, 0, 9], [3, 3, 10], [0, 3, 7], [0, 0, 2], [0, 0, 3], [2, 2, 2], [2, 3, 2], [5, 5, 6], [0, 1, 2], [0, 5, 2]]) == 27
    assert candidate(14, [[3, 12, 7], [1, 3, 2], [4, 11, 3], [0, 1, 7], [1, 5, 2], [1, 1, 4]]) == 14
    assert candidate(14, [[0, 0, 3], [0, 1, 3], [1, 11, 3], [6, 7, 6], [7, 7, 5], [1, 2, 8], [7, 10, 9]]) == 20
    assert candidate(13, [[0, 12, 7], [2, 2, 4], [2, 2, 8], [3, 3, 2], [1, 11, 5], [1, 7, 2]]) == 10
    assert candidate(1, [[0, 0, 2], [0, 0, 8], [0, 0, 1]]) == 8
    assert candidate(1, [[0, 0, 1], [0, 0, 4], [0, 0, 7], [0, 0, 2], [0, 0, 5], [0, 0, 1], [0, 0, 4], [0, 0, 2], [0, 0, 6], [0, 0, 6], [0, 0, 3], [0, 0, 3]]) == 7
    assert candidate(1, [[0, 0, 6], [0, 0, 6], [0, 0, 3], [0, 0, 6], [0, 0, 6], [0, 0, 10], [0, 0, 1], [0, 0, 2]]) == 10
    assert candidate(9, [[4, 6, 7], [1, 3, 10]]) == 17
    assert candidate(13, [[2, 6, 3], [1, 12, 6], [2, 11, 3], [7, 7, 2], [5, 12, 4], [0, 1, 2], [0, 1, 8], [1, 1, 3], [6, 6, 4], [8, 9, 7], [8, 8, 2], [2, 2, 2], [0, 0, 9], [9, 11, 7], [8, 9, 7]]) == 29
    assert candidate(8, [[0, 1, 8], [0, 0, 6], [5, 5, 9]]) == 17
    assert candidate(1, [[0, 0, 10], [0, 0, 3], [0, 0, 8], [0, 0, 9], [0, 0, 1], [0, 0, 8], [0, 0, 2], [0, 0, 7], [0, 0, 10], [0, 0, 8], [0, 0, 5], [0, 0, 3], [0, 0, 2], [0, 0, 4]]) == 10
    assert candidate(9, [[0, 2, 6], [1, 3, 5], [1, 1, 5], [2, 3, 10], [4, 8, 4], [5, 8, 5], [6, 6, 10]]) == 25
    assert candidate(6, [[0, 0, 7]]) == 7
    assert candidate(8, [[1, 1, 5], [1, 2, 9], [1, 2, 6], [0, 3, 6], [1, 1, 10], [3, 4, 1], [3, 5, 3], [1, 5, 8], [0, 2, 6], [5, 7, 9]]) == 20
    assert candidate(14, [[3, 4, 4], [6, 8, 1], [0, 4, 1]]) == 5
    assert candidate(11, [[4, 4, 2], [1, 2, 7], [2, 8, 10], [1, 1, 3], [8, 10, 4], [1, 2, 1], [4, 6, 10]]) == 21
    assert candidate(11, [[1, 8, 1], [1, 5, 5], [0, 1, 3], [10, 10, 10], [1, 1, 8], [1, 2, 1], [2, 3, 10], [2, 10, 10], [2, 2, 9], [0, 9, 4]]) == 28
    assert candidate(6, [[2, 2, 6], [0, 1, 2], [2, 2, 2]]) == 8


def test_check():
    check(maximizeTheProfit)


### Metadata below ###
# question_id = 2979
# question_title = Maximize the Profit as the Salesman
# question_title_slug = maximize-the-profit-as-the-salesman
# question_difficulty = Medium
# question_category = Algorithms
# question_likes = 603
# question_dislikes = 19