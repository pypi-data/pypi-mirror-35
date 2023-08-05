#coding=utf-8
from collections import namedtuple
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit import prompt as _prompt
from .validator import validator as _validator
import cgi

class Context():
    def __init__(self,indent=0,quote='',end='\n',fg='',bg='',font=''):
        self.indent = indent
        self.quote = quote
        self.end = end
        self.fg = fg
        self.bg = bg
        self.font = font

class Session():
    printer = None

    def __init__(self,**kwargs):
        self.context = Context(**kwargs)
        
    def __enter__(self):
        Session.printer = Printer(self.context)
    
    @classmethod
    def getPrinter(self,**kwargs):
        if Session.printer:
            if kwargs:
                old = Session.printer.context.__dict__.copy()
                for k,v in kwargs.items():
                    old[k] = v
                return Printer(Context(**old))
            else: 
                return Session.printer
        else:
            return Printer(Context(**kwargs))
       
    def __exit__(self, type, value, trace):
        Session.printer = None

class Printer():
    def __init__(self,context = Context()):
        self.context = context
        fg = context.fg
        bg = context.bg
        self._sytle =  {'line':'<u fg="{}" bg="{}">{}</u>'.format(fg,bg,'{}'),
                 'bold':'<b fg="{}" bg="{}">{}</b>'.format(fg,bg,'{}'),
                 '':'<p fg="{}" bg="{}">{}</p>'.format(fg,bg,'{}')
        }

    def __indent(self):
       
        times = self.context.indent
        if times == 0:
            return ''
        prefix = ''
        prefix += self.context.quote or ' '
        for _ in range(times-1):
            prefix += " "
        return prefix

    def __styleText(self,*content):
        font = self._sytle.get(self.context.font)
        indent = self.__indent()
        content = str(content) and ' '.join(list([str(item) for item in content]))
        return HTML(indent + font.format(cgi.escape(content)))

    def print(self,*content):
        print_formatted_text(self.__styleText(*content),end=self.context.end,flush=True)
    
    def prompt(self,content,**args):
        return _prompt(self.__styleText(content),**args)

def indent(indent,quote=''):
    return Session(indent=indent,quote=quote)

def color(fg,bg=''):
    return Session(fg=fg,bg=bg)

def font(f):
    return Session(font=f)

def style(**kwargs):
    return Session(**kwargs)

def echo(*x,**kwargs):
    Session.getPrinter(**kwargs).print(*x)

def prompt(x,validator=None,**kwargs):
    validator = validator or _validator(lambda input:True,'')
    return Session.getPrinter(**kwargs).prompt(x,validator=validator)

def success(*itmes):
    echo(*itmes,fg='green')

def faild(*itmes):
    echo(*itmes,fg='red')

def warning(*itmes):
    echo(*itmes,fg='yellow')