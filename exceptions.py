class fileNotFoundWarning(RuntimeWarning):
    def __init__(self, filename):
        self.f = filename
    def __str__(self):
        return 'File %s not found!' % self.f

class fileNotFoundError(RuntimeError):
    def __init__(self, filename):
        self.f = filename
    def __str__(self):
        return 'File %s not found, please exit manually and fix problem (or maybe just refresh the database)!' % self.f

class notMainError(RuntimeError):
    def __init__(self):
        pass
    def __str__(self):
        return 'Program is not ran as __main__, please re-run it!'

class deprecatedMethodWarning(PendingDeprecationWarning):
    def __init__(self, oldn, newn):
        self.oldn = oldn
        self.newn = newn
    def __str__(self):
        return 'Method %s will be deprecated soon, use %s instead.' % (self.oldn, self.newn)