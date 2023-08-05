#coding=utf-8
from .printer import echo
from .printer import prompt
from .options import options
from .printer import style
from .validator import validator as Validator
from abc import abstractclassmethod
from abc import ABCMeta

class Select(metaclass=ABCMeta):

    @abstractclassmethod
    def show(self):pass
    
    @abstractclassmethod
    def selected(self):pass

    @abstractclassmethod
    def validation(self,rawInput,options):pass
    
    @abstractclassmethod
    def convertRawInput(self,rawInput):pass

class AbstractSelect(Select):
    def __init__(self,options,tip,errorMsg=None):
        self._options = options
        self._tip = tip
        self._errorMsg = errorMsg or '请检查输入格式，并确保输入在选项中!'
    
    @property
    def options(self):
        return self._options

    @property
    def errorMsg(self):
        return self._errorMsg

    @property
    def tip(self):
        return self._tip
    
    def convertRawInput(self,rawInput):
        return rawInput

    def show(self):
        for option in self.options.all():
            echo(option.string())
        echo("")
    
class SingleSelect(AbstractSelect):

    def __init__(self,options,tip,errorMsg=None):
        AbstractSelect.__init__(self,options,tip,errorMsg)
    
    def validation(self,rawInput,options):
        return rawInput in options.index
    
    def __validator(self):
        v = lambda input:self.validation(input,self.options)
        return Validator(v,self.errorMsg)

    def selected(self):
        validatedInput = prompt(self.tip,self.__validator())
        input = self.convertRawInput(validatedInput)
        return self.options.get(input)

class MulitSelect(AbstractSelect):
    def __init__(self,options,tip,separator=' ',errorMse=None):
        AbstractSelect.__init__(self,options,tip,errorMse)
        self._separator = separator
    
    def validation(self,rawInput,options):
        if self._separator not in rawInput:
            return rawInput in options.index
        inputs = rawInput.split(self._separator)
        for input in inputs:
            if input not in options.index:
                return False
        return True
    
    def __validator(self):
        v = lambda input:self.validation(input,self.options)
        return Validator(v,self.errorMsg)

    def convertRawInput(self,rawInput):
        return rawInput.split(self._separator) if self._separator in rawInput else [rawInput]

    def selected(self):
        validatedInput = prompt(self.tip,self.__validator())
        indexes = self.convertRawInput(validatedInput)
        return self.options.getWithIndex(indexes)


def confirm(tip):
    return prompt(tip).lower() == 'y'

def select(selector):
        selector.show()
        return selector.selected()

 

    