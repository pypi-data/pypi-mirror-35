#coding=utf-8
from .printer import echo
from wcwidth import wcswidth
def hr(num,char='-'):
    s = ''
    for _ in range(num):
        s += char
    echo(s)

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
