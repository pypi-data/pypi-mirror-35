# coding: utf-8
__version__ = '0.3.0'


class NonexequiException(Exception):
    def __init__(self, *args, **kwargs):
        super(NonexequiException, self).__init__(*args, **kwargs)
