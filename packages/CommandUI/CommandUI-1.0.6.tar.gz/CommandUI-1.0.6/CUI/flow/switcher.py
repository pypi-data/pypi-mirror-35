#coding=utf-8
from functools import wraps
import inspect


from collections import Iterable
class Switcher():
    def __init__(self):
        self._funMap = {}
        self._start = ""

    def action(self,**kwargs):
        def decorate(fun):
            name = fun.__name__
            callMap = kwargs
            @wraps(fun)
            def wrapper(*args, **kwargs):
                data = fun(*args, **kwargs)

                if not data:
                    return

                funKey = None
                results = []

                if type(data) == str or inspect.isfunction(data):
                    funKey = data
                elif isinstance(data,Iterable):
                    funKey,*results = data
                
                if inspect.isfunction(funKey):
                    nextFunName = funKey.__name__
                elif type(funKey) == str:
                    nextFunName = callMap.get(funKey)
                    if not nextFunName:
                        raise ValueError("can't find a function name mapped by `{}`".format(funKey))
                else:
                    raise TypeError('the first return value must str or function type')
                self.__call(nextFunName,*results)

                return data

            if not self._funMap: self._start = name
            self._funMap[name] = wrapper
            return wrapper
            
        return decorate

    
    def run(self,*arg,**kwargs):
        self._funMap[self._start](*arg,*kwargs)

    def __call(self,name,*args):
        if args:
            self._funMap[name](*args)
        else:
            self._funMap[name]()