class fileNotFoundWarning(RuntimeWarning):
    def __init__(self, filename):
        self.f = filename
    def __str__(self):
        return 'File %s not found!' % self.f

class fileNotFoundError(RuntimeError):
    def __init__(self, filename):
        self.f = filename
    def __str__(self):
        return 'File %s not found, please exit manually and fix problem/refresh database!' % self.f