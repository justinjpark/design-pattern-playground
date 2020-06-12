# Implementing the singleton design pattern in Python

class Singleton():
    '''
    Singleton is a creational design pattern that lets you ensure a class creates only one instance, while providing a single global access point to that instance.
    '''

    __instance = None

    # return instance if it exists, if not create the one and only instance
    @staticmethod
    def get_instance():
        # Singleton() if Singleton.__instance is None else return Singleton.__instance
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    # assign static varible to new instance, if instance already exists then raise exception
    def __init__(self):
        # Singleton.__instance = self if Singleton.__instance is None else raise Exception('You cannot create another instance of Singleton')
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception('You cannot create another instance of Singleton')
