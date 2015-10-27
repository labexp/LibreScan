
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):

    def __init__(self):
        self.melcocho = 0
        self.y = 0

    def set_x(self, x):
        self.melcocho = x

    def set_y(self, y):
        self.y = y

l = Logger()
l.set_x(40)


l2 = Logger()
l2.set_x(50)
print(l.melcocho)
print(l2.melcocho)
