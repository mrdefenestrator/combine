#!/usr/bin/env python3
'''Unit and end-to-end tests for the python combine module and cli
'''
import unittest
import subprocess
from combine import combine


class TestUnit(unittest.TestCase):
    def test_length_one_arrays(self):
        self.assertEqual(combine([1], [2]), [1, 2])

    def test_longer_arrays(self):
        self.assertEqual(combine([1, 2, 7, 9], [3, 6, 8]), [
                         1, 2, 3, 6, 7, 8, 9])

    def test_duplicates(self):
        self.assertEqual(combine([6, 8, 9], [1, 4, 6]), [1, 4, 6, 6, 8, 9])

    def test_empty(self):
        self.assertEqual(combine([], [1, 2, 3]), [1, 2, 3])

    def test_sorting(self):
        self.assertEqual(combine([5, 3, 1], [6, 4, 2]), [1, 2, 3, 4, 5, 6])


class TestCLI(unittest.TestCase):
    def test_error_with_no_args(self):
        self.assertEqual(subprocess.call(
            './combine.py', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL), 1)

    def test_success(self):
        self.assertEqual(subprocess.call(
            './combine.py [] []', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL), 0)

    def test_success_output(self):
        self.assertEqual(subprocess.check_output(
            './combine.py [1,3,5] [2,4,6]', shell=True), b'[1, 2, 3, 4, 5, 6]\n')

    def test_fail_on_bad_args(self):
        self.assertEqual(subprocess.call(
            './combine.py not arrays', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL), 1)


if __name__ == '__main__':
    unittest.main()
