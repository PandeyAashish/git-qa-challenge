import unittest
from tests.home.test_git import GitPageTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(GitPageTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
