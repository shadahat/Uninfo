######### Author :  Nowshad #########

class Iterator(object):

    def __init__(self, iterable_object):
        self.list = iterable_object
        self.index = (iterable_object.__len__())-1 # Shahin helped

    def __iter__(self):
        return self


    def hasnext(self):
        if (self.index < 0):
            return False
        else:
            return True

    def next(self):
        ret = self.list[self.index]
        self.index = int(self.index - 1)
        return ret