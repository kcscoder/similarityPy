# coding=utf-8
import operator

from apps.distances.distance import Distance


__author__ = 'cenk'


class HammingDistance(Distance):
    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]

            if len(point_a) == len(point_b):
                try:
                    point_a = point_a.lower()
                    point_b = point_b.lower()
                except:
                    pass
                try:
                    equality_list = map(operator.eq, point_b, point_a)
                    self._result = equality_list.count(False)
                except:
                    raise
            else:
                raise ArithmeticError("You cant calculate hamming distance of array has different sizes.")

        else:
            raise ArithmeticError("You must enter two array to find squared euclidean distance.")