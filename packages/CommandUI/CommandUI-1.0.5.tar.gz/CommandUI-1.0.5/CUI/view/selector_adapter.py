#coding=utf-8
from .selector import select,SingleSelect,MulitSelect
from .options import options,Option

def singleSelect(items,tip):
    selector = SingleSelect(options(*items),tip)
    return select(selector)

def mulitSelect(items,tip):
    result = select(MulitSelect(options(*items).append(Option('a','全选','all')),tip,separator=','))
    if 'a' in result.index:
        return options(*items)
    else:
        return result