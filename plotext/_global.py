import sys

platform = 'windows' if sys.platform in {'win32', 'cygwin'} else 'unix' # the platform (unix or windows) you are using plotext in

class memorize: # it memorise the arguments of a function, when used as its decorator, to reduce computational time
    def __init__(self, function):
        self.f = function
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]
