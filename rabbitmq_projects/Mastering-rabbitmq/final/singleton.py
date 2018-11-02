
class Singleton(type):
    #_instance = {}
    _instance={}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance=super(Singleton, cls).__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]

