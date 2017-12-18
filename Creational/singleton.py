# coding:utf-8


class Singleton(object):
    """
    Design Pattern: Singleton
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            org = super(Singleton, cls)
            cls.__instance = org.__new__(cls, *args, **kwargs)

        return cls.__instance

    def __init__(self):
        pass


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    print s1.value
    print s2.value
