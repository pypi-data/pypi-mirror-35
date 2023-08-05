#coding=utf-8
from .printer import echo as print
from wcwidth import wcswidth

def nonAscii(str):

    return wcswidth(str) - len(str)

# 修复python中存在中文时对齐问题
def align(str,width,style):
    f = {
        'left':lambda s,w:s.ljust(w),
        'right':lambda s,w:s.rjust(w),
        'center':lambda s,w:s.center(w)
    }
    if style not in f.keys():style = 'center'
    
    return f[style](str,width-nonAscii(str))

def die(tip,code=1,**kwargs):
    print(tip,**kwargs)
    exit(code)

def hr(num,char='-'):
    s = ''
    for _ in range(num):
        s += char
    print(s)
