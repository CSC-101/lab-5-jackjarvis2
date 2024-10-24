import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3

    def test_add_times_basic(self):
        t1 = data.Time(1, 30, 45)
        t2 = data.Time(2, 45, 30)
        result = lab5.add_times(t1, t2)
        self.assertEqual(str(result), "04:16:15")

    def test_add_times_wrap_around(self):
        t1 = data.Time(23, 59, 59)
        t2 = data.Time(0, 0, 1)
        result = lab5.add_times(t1, t2)
        self.assertEqual(str(result), "00:00:00")

    # Part 4
    def test_descending1(self):
        self.assertTrue(lab5.is_descending([5.0, 4.0, 3.0, 2.0, 1.0]))

    def test_empty_list1(self):
        self.assertTrue(lab5.is_descending([]))

    # Part 5
    def test_largestbetween1(self):
        self.assertEqual(lab5.largest_between([1, 3, 2, 5, 4], 1, 3), 3)
    def test_largetbetween2(self):
        self.assertEqual(lab5.largest_between([1, 3, 2, 5, 4], 0, 2), 1)
    def test_largestbetween3(self):
        self.assertEqual(lab5.largest_between([1,2,3,4,5],2,0),None)
    # Part 6
    def test_furthest_from_the_origin1(self):
        # Test with normal points
        points1 = [data.Point(1, 1), data.Point(2, 2), data.Point(3, 3)]
        self.assertEqual(lab5.furthest_from_origin(points1), 2)

    def test_furthest_from_the_origin2(self):
        points2 = [data.Point(-1, -1), data.Point(1, -1), data.Point(2, 2)]
        self.assertEqual(lab5.furthest_from_origin(points2), 2)




if __name__ == '__main__':
    unittest.main()
