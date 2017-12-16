# coding:utf-8


class Singoleton(object):
    """
    Design Pattern: Singleton
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            org = super(Singoleton, cls)
            cls.__instance = org.__new__(cls, *args, **kwargs)
        return cls.__instance


if __name__ == '__main__':
    pass
