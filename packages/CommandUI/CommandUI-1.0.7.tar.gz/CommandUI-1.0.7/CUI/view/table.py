#coding=utf-8
from .printer import echo
from .tools import hr,nonAscii,align
class Table():
    """
        显示表格数据。
        data: 表格数据,{'title1':[1,2,3,...,],'title2':[2,3,4,...,]}
        width: 每一列的长度，如果为'auto'，则自动确定
        border: 是否显示边框
        placeholder: 占位符，由于每一列长度可能不一样，当某列的一些元素不存在时显示该占位符
        align: 对齐方式。'left':左对齐,'right':右对齐,'center':居中对齐
    """
    def __init__(self,data,width='auto',border=True,placeholder='-',align='center'):
        self._title = list(data.keys())
        self._columns = data.values()
        self._border = border
        self._placeholder = placeholder
        self._maxRow = max([len(col) for col in self._columns]) # 最大行数
        self._align = align
        self._width = self.__detectColWidth() if width=='auto' else [width]*len(self._title) #每一列的宽度，如果 width='auto' 则宽度为字符数+2
        self._sumWidth = sum(self._width) + len(self._title) + 1

    def __detectColWidth(self):
        width = []
        for index,col in enumerate(self._columns):
            colWithTitle = col + [self._title[index]]
            maxWidthPerCol = self.__detectWidth(colWithTitle)
            width.append(maxWidthPerCol)
        return width

    def __detectWidth(self,items):
       
        # 每个字符串的宽度 = 字符数 + 非ascii字符数 + 2(显示边距)
        itemWidth = lambda item : len(str(item)) + nonAscii(str(item)) + 2 

        return max([itemWidth(item) for item in items])


    def __displayBorder(self):
        if not self._border:
            return
        border = '+'
        index = 0
        while index != len(self._title):
            for _ in range(self._width[index]):
                border += '-'
            border += '+'
            index += 1
        echo(border)


    def __getRow(self,index):
        row = []
        for col in self._columns:
            if index >= len(col):
                row.append(self._placeholder)
            else:
                row.append(str(col[index]))
        return row

    def __toString(self,row):
        rowStr = ''
        if self._border:
            rowStr += '|'
        for index,item in enumerate(row):
            rowStr += align(item,self._width[index],self._align)
            if self._border:
                rowStr += '|'
        return rowStr

    def __displayRow(self,row,**kwargs):
        
        echo(self.__toString(row),**kwargs)

    def __displayTitle(self):
        self.__displayBorder()
        self.__displayRow(self._title,font='bold')
        self.__displayBorder()

    def display(self):
        self.__displayTitle()
        
        for index in range(self._maxRow):
            row = self.__getRow(index)
            self.__displayRow(row)

        self.__displayBorder()
        
def table(data,**kwarg):
    """
        显示表格数据。
        data: 表格数据,{'title1':[1,2,3,...,],'title2':[2,3,4,...,]}
        width: 每一列的长度，如果为'auto'，则自动确定
        border: 是否显示边框
        placeholder: 占位符，由于每一列长度可能不一样，当某列的一些元素不存在时显示该占位符
        align: 对齐方式。'left':左对齐,'right':右对齐,'center':居中对齐
    """
    Table(data,**kwarg).display()

def buildTableData(titles,columns):
    if len(titles) != len(columns):
        raise ValueError("length of titles length don't equal columns")
    return { title:columns[index] for index,title in enumerate(list(titles)) }