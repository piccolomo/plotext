# Runner of the plotext test suite, gathering the tests of every module beside this one

import unittest


# The modules holding the tests, in the order they are run
module_names = ["primitives", "plots", "dates", "fixed_bugs", "hashes"]


# Run every test and print the outcome, as in plotext.test()
def test():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    for module_name in module_names:
        module = __import__("plotext._tests." + module_name, fromlist = [module_name])
        suite.addTests(loader.loadTestsFromModule(module))
    runner = unittest.TextTestRunner()
    return runner.run(suite)


if __name__ == '__main__':
    test()
