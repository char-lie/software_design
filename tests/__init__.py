from unittest import defaultTestLoader
import src

test_cases = src.test_cases

tests = [defaultTestLoader.loadTestsFromTestCase(test) for test in test_cases]

