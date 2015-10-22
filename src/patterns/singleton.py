

class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):

    def __init__(self, mel, y):
        self.melcocho = mel
        self.y = y

    def set_x(self, x):
        self.melcocho = x

    def set_y(self, y):
        self.y = y

l = Logger(999, 12)
print(l.melcocho)
l.set_x(40)


l2 = Logger(999,12)
l2.set_x(50)
print(l.melcocho)
print(l2.melcocho)