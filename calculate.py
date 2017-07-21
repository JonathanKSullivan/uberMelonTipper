def tip(cost, percent):
    """ Returns a single tip amount given one percentage and one cost

    >>> calculate_tip(100, 25)
    25.0

    >>> calculate_tip(50, 10)
    5.0

    """
    return (percent/100.0) * cost

def tips(cost, percents):
    """ Returns a list of tip amounts given a list of percentage and one cost

    >>> calculate_tips(100, [5, 25, 10])
    [5.0 25.0, 10.0]

    """
    return [tip(cost, percent) for percent in percents]

import unittest
class tipTestCases(unittest.TestCase):
    """docstring for ClassName"""

    def test_tip(self):
        self.assertEqual(tip(100, 25), 25)
    
    def test_tips(self):
        self.assertEqual(tips(100, [5, 10, 15, 20]), [5, 10, 15, 20])

if __name__ == "__main__":
    unittest.main()
    