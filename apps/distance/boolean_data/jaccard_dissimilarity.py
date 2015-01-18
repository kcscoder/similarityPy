# coding=utf-8
import operator

from apps.distance.distance import Distance


__author__ = 'cenk'


class JaccardDissimilarity(Distance):
    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]

            if len(point_a) == len(point_b):
                and_list = map(operator.and_, point_b, point_a)
                xor_list = map(operator.xor, point_b, point_a)

                and_count = and_list.count(True)
                xor_count = xor_list.count(True)

                try:
                    self._result = (float(xor_count) / (xor_count + and_count))
                except:
                    raise
            else:
                raise ArithmeticError("You cant calculate hamming distance of array has different sizes.")

        else:
            raise ArithmeticError("You must enter two array to find squared euclidean distance.")