def tip(cost, percent):
    """ Returns a single tip amount given one percentage and one cost

    >>> calculate_tip(100, 25)
    25.0

    >>> calculate_tip(50, 10)
    5.0

    """
    pass

def tips(cost, percents):
    """ Returns a list of tip amounts given a list of percentage and one cost

    >>> calculate_tips(100, [5, 25, 10])
    [5.0 25.0, 10.0]

    """
    pass

import unittest
class tipTestCases(unittest.Testcase):
    """docstring for ClassName"""

    def test_calculate_tip(self, arg):
        self.assertEqual(calculate_tip(100, 25), 25)
    
    def test_calculate_tips(self, arg):
        self.assertEqual(calculate_tips(100, [5, 10, 15, 20]), [5, 10, 15, 20])

if __name__ == "__main__":
    unittest.main()
    