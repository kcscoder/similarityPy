# coding=utf-8
"""
Created on 18 January 2014
@author: Cenk Bircanoglu
"""


class Mean:
    def __init__(self):
        self._data = []
        self.counter = 0
        self.total = 0

    def calculate(self, data, is_tuple=False, index=None):
        if is_tuple:
            self._data = [obj[index] for obj in data]
        else:
            self._data = data

        return self.__algorithm()

    def __algorithm(self):
        try:
            return float(sum(self._data)) / len(self._data)
        except ZeroDivisionError:
            raise ZeroDivisionError("integer division or modulo by zero")



