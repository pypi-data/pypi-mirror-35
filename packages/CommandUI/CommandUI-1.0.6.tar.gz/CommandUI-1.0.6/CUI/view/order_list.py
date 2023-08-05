#coding=utf-8
from .printer import echo as print

def orderList(items,indexes = None,formatter = None):
    indexes = indexes or range(len(items))
    formatter = formatter or (lambda index,item: "[{}]".format(index).ljust(5)+str(item))
    for i,item in enumerate(items):
        print(formatter(indexes[i],item))

def unorderList(items,index='*'):
    indexes = list([index for item in items])
    formatter = lambda i,item : i+"  "+str(item)
    orderList(items,indexes,formatter)
