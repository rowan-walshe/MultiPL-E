from typing import List


def height_checker(heights: List[int]) -> int:
    """
    A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
    You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).
    Return the number of indices where heights[i] != expected[i].
 
    Example 1:

    Input: heights = [1,1,4,2,1,3]
    Output: 3
    Explanation: 
    heights:  [1,1,4,2,1,3]
    expected: [1,1,1,2,3,4]
    Indices 2, 4, and 5 do not match.

    Example 2:

    Input: heights = [5,1,2,3,4]
    Output: 5
    Explanation:
    heights:  [5,1,2,3,4]
    expected: [1,2,3,4,5]
    All indices do not match.

    Example 3:

    Input: heights = [1,2,3,4,5]
    Output: 0
    Explanation:
    heights:  [1,2,3,4,5]
    expected: [1,2,3,4,5]
    All indices match.

 
    Constraints:

    1 <= heights.length <= 100
    1 <= heights[i] <= 100

    """
    ### Canonical solution below ###
    expected = sorted(heights)

    count = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1

    return count




### Unit tests below ###
def check(candidate):
	assert candidate([10,10,3,1,2,1,3,2,1,3]) == 8
	assert candidate(
    [1]) == 0
	assert candidate([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]) == 0
	assert candidate([1,2,3,4,5]) == 0
	assert candidate(
    [1,2,3,4]) == 0
	assert candidate([1,2,3,4,5,6,7,8,9,10]) == 0
	assert candidate([5,1,2,3,4]) == 5
	assert candidate(list(range(1, 101))) == 0
	assert candidate([3,2,1,3,2,1,3,2,1]) == 6
	assert candidate(
    [1,2,3,4,5]) == 0
	assert candidate( [5,1,2,3,4]) == 5
	assert candidate(
    [5,1,2,3,4]) == 5
	assert candidate(
    [3,2,5,1,4]) == 4
	assert candidate([2,2,2,2,2]) == 0
	assert candidate([10,9,8,7,6,5,4,3,2,1]) == 10
	assert candidate(
    [4,3,2,5,1]) == 5
	assert candidate([2,1,4,3,6,5,8,7,10,9]) == 10
	assert candidate([2,2,2,1,1,1,3,3,3]) == 6
	assert candidate(
    [2,5,4,3,1]) == 5
	assert candidate([1]) == 0
	assert candidate([1,1,4,2,1,3]) == 3
	assert candidate(list(range(100, 0, -1))) == 100
	assert candidate([1,1,1,2,2,2,3,3,3]) == 0
	assert candidate(
    [2,1,5,3,6,4,8,7,10,9]) == 10
	assert candidate([10,1,2,3,4,5,6,7,8,9]) == 10
	assert candidate( [1,2,3,4,5]) == 0
	assert candidate(
    [1,2,3,5,4]) == 2
	assert candidate(
    [1,2,3,4,4]) == 0
	assert candidate([1,1,1,1,1,1]) == 0
def test_check():
	check(height_checker)
# Metadata Difficulty: Easy
# Metadata Topics: array,sorting,counting-sort
# Metadata Coverage: 100
