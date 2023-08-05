#coding=utf-8
from functools import wraps
from inspect import getargspec
class Switcher():
    def __init__(self):
        self._funMap = {}
        self._callMap = {}
        self._start = ""
        self._funArg = {}

    def route(self,name,**kwargs):
        def decorate(fun):
            @wraps(fun)
            def wrapper(*args, **kwargs):
                data = fun(*args, **kwargs)
                if not data:
                    return  
                # 对于string类型，我们希望的展开结果是:a,b = "string" -> a="string",b=[]
                # 实际上的展开结果是: a="s",b="tring"，所以需要包装一下
                envelopData = data
                if type(data) == str:    
                    envelopData = (data,[])
                    
                funKey,*result = envelopData 
                nextFunRoute = self._callMap[name].get(funKey)
                if not nextFunRoute:
                    raise KeyError("unknow call map [{}] !".format(funKey))
                nextFun = self._funMap.get(nextFunRoute)
                if not nextFun:
                    raise KeyError("unknow route name [{}],ensure it has been registered!".format(nextFunRoute))
                if self._funArg[nextFunRoute].args: 
                    nextFun(*result)
                else:
                    nextFun() 
                return data

            if not self._funMap: self._start = name
            self._funMap[name] = wrapper
            self._funArg[name] = getargspec(fun)
            self._callMap[name] = kwargs
            return wrapper
            
        return decorate

    def run(self,*arg,**kwargs):
        self._funMap[self._start](*arg,*kwargs)
