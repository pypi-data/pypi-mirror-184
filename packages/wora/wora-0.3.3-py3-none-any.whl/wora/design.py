
_register = {}

# Singleton design pattern
def singleton(cls):
   def wrapper(*args, **kw):
       if cls not in _register:
           instance = cls(*args, **kw)
           _register[cls] = instance
       return _register[cls]

   wrapper.__name__ = cls.__name__
   return wrapper

# Singleton Metaclass
class Singleton(type):
    ''' Manage only a single global instance of this class across python modules '''
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

