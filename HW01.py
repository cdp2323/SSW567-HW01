"""
Created on Wed 1/29/2020
@author: danping cai
"""

import unittest  # this makes Python unittest module available


def classify_triangle(side1, side2, side3):
    """
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
    """
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "NotATriangle"
    else:
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            return 'NotATriangle'
        if side1 == side2 == side3:
            return 'Equilateral'
        elif side1 == side2 or side1 == side3 or side2 == side3:
            return 'Isoceles'
        elif side1 * side1 + side2 * side2 == side3 * side3 or side1 * side1 + side3 * side3 == \
                side2 * side2 or side2 * side2 + side3 * side3 == side1 * side1:
            return 'Right'
        else:
            return "Scalene"


class TestTriangles(unittest.TestCase):
    """
    Test class
    """

    def test_classify_triangle(self):
        """
        Test function
        :return: None
        """
        side1, side2, side3 = (3, 4, 5)
        self.assertNotEqual(classify_triangle(side1, side2, side3), 'NotATriangle')
        side1, side2, side3 = (200, 999, 0)
        self.assertEqual(classify_triangle(side1, side2, side3), 'NotATriangle')
        side1, side2, side3 = (5, 2, 7)
        self.assertEqual(classify_triangle(side1, side2, side3), 'NotATriangle')
        side1, side2, side3 = (2, 3, 4)
        self.assertEqual(classify_triangle(side1, side2, side3), 'Scalene')
        side1, side2, side3 = (9, 9, 9)
        self.assertEqual(classify_triangle(side1, side2, side3), 'Equilateral')
        side1, side2, side3 = (90, 90, 90)
        self.assertNotEqual(classify_triangle(side1, side2, side3), 'Right')
        side1, side2, side3 = (4, 4, 2)
        self.assertEqual(classify_triangle(side1, side2, side3), 'Isoceles')


if __name__ == '__main__':
    unittest.main()
