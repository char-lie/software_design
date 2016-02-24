from unittest import defaultTestLoader
from TransactionManager import TransactionManagerBase

test_cases = [TransactionManagerBase]

tests = [defaultTestLoader.loadTestsFromTestCase(test) for test in test_cases]

