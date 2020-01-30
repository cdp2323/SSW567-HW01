# -*- coding: utf-8 -*-
"""
Created on Wed 1/29/2020

@author: danping cai
"""

import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    if a<=0 or b<=0 or c<=0:
        return "NotATriangle"
    else:
        if a + b <= c or a + c <= b or b + c <= a:
            return 'NotATriangle'
        if a == b == c:
            return 'Equilateral'
        elif a == b or a == c or b == c:
            return 'Isoceles'
        elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
            return 'Right'    
        else:
            return "Scalene"
        


class TestTriangles(unittest.TestCase):
    def test_classifyTriangle(self):
        a,b,c = (3,4,5)
        self.assertNotEqual(classifyTriangle(a,b,c),'NotATriangle')
        a,b,c = (200,999,0)
        self.assertEqual(classifyTriangle(a,b,c),'NotATriangle')
        a,b,c = (5,2,7)
        self.assertEqual(classifyTriangle(a,b,c),'NotATriangle')
        a,b,c = (2,3,4)
        self.assertEqual(classifyTriangle(a,b,c),'Scalene')
        a,b,c = (9,9,9)
        self.assertEqual(classifyTriangle(a,b,c),'Equilateral')
        a,b,c = (90,90,90)
        self.assertNotEqual(classifyTriangle(a,b,c),'Right')
        a,b,c = (4,4,2)
        self.assertEqual(classifyTriangle(a,b,c),'Isoceles')
        

if __name__ == '__main__':
    try:
        a = float(input('Please enter the first side length:'))
        b = float(input('Please enter the second side length:'))
        c = float(input('Please enter the third side length:'))
    except ValueError:
        print("please enter arabic numbers only")
    else:
        print(classifyTriangle(a,b,c))
    
    unittest.main() 