from multiprocessing import Process, Manager
from multiprocessing.managers import BaseManager

class SimpleClass(object):
    def __init__(self):
        self.var = 0

    def set(self, value):
        self.var = value

    def get(self):
        return self.var

class SimpleClass2(object):
    def __init__(self):
        self.var = 0

    def set(self, value):
        self.var = value

    def get(self):
        return self.var

def change_obj_value(obj):
    obj.set(100)


if __name__ == '__main__':
    BaseManager.register('SimpleClass', SimpleClass)
    BaseManager.register('SimpleClass2', SimpleClass2)
    manager = BaseManager()
    manager.start()
    inst1 = manager.SimpleClass()
    inst2= manager.SimpleClass2()
    p1 = Process(target=change_obj_value, args=[inst2])
    p2 = Process(target=change_obj_value, args=[inst1])

    p1.start()
    p2.start()
    p2.join()
    p2.join()
    print inst1
    print inst1.get()
    print inst2                    # <__main__.SimpleClass object at 0x10cf82350>
    print inst2.get()        
