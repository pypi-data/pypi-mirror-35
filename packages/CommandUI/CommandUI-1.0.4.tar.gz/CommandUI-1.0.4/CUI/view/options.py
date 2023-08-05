#coding=utf-8
class Option(object):

    def __init__(self,index,content,value=None,formatter=False):
        self._index = index
        self._content = content
        self._value = value or content
        self._formatter = formatter or (lambda index,content:'[{}] {}'.format(index,content))
    
    def string(self): return self._formatter(self._index,self._content)

    def equal(self,index): return self._index == index 
    
    @property
    def index(self):
        return self._index
    
    @property
    def content(self):
        return self._content
    
    @property
    def value(self):
        return self._value
    
    def zipped(self):
        return (self.index,self.content,self.value)
    
    def __call__(self):
        return self.value

class Options(object):
    def __init__(self,options):
        self._options = options

    def get(self,index):
        for option in self.all():
            if option.equal(index):
                return option
        raise KeyError("index {} not find!".format(index)) 
    
    def getWithIndex(self,indexes):
        results = []
        for option in self.all():
            if option.index in indexes:
                results.append(option)
        return Options(results)

    def append(self,option):
        assert(isinstance(option,Option))
        self._options.append(option)
        return self

    @property
    def index(self):
        return list(map(lambda option:option.index,self._options))

    @property
    def value(self):
        return list(map(lambda option:option.value,self._options))

    @property
    def content(self):
        return list(map(lambda option:option.content,self._options))
    
    def zipped(self):
        return list(zip(self.index,self.content,self.value))

    def all(self):
        return self._options
    
    def __call__(self):
        return self.value

def options(*contents,formatter=None):
    indexes = range(len(contents))
    values = contents
    if indexes:
        assert(len(indexes)==len(contents))
    if values:
        assert(len(indexes)==len(values))
    _options = zip(indexes,contents,values)
    results = []
    for (index,content,value) in _options:
        results.append(Option(str(index),content,value,formatter))
    return Options(results)

def optionsFromTuple(optionsTuple,formatter=None):
    results = []
    for index,content,*value in optionsTuple:
        results.append(Option(str(index),content,*value,formatter=formatter))
    return Options(results)