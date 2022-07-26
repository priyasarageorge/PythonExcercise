import unittest
import ex5


class DistanceCheck(unittest.TestCase):
    def test_line_from_points(self):
        point1, point2 = [[2, -1], [2, 1]]
        return_val = ex5.line_from_points(point1, point2)
        self.assertEqual(return_val, None)


if ex5 == '_main_':
    unittest.main()
