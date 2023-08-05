#coding=utf-8
from prompt_toolkit.validation import Validator
def validator(callable,tip):
    return Validator.from_callable(callable,tip)
