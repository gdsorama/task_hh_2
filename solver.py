# -*- coding: utf-8 -*-
"""
модуль определения деления чисел в k-ичной системе счисления
определение результата деления a/b в k-той системе счисления
результат представлен в виде строки. В случае бесконечной периодической дроби,
период заключается в скобки.
Пример входных данных:
1 2 8
1 12 10
Пример выходных данных:
0.4
0.08(3)
"""
from math import modf
import unittest
digits = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L',
22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W',
33: 'X', 34: 'Y', 35: 'Z', 36: 'a', 37: 'b', 38: 'c', 39: 'd', 40: 'e', 41: 'f', 42: 'g', 43: 'h',
44: 'i', 45: 'j', 46: 'k', 47: 'l', 48: 'm', 49: 'n', 50: 'o', 51: 'p', 52: 'q', 53: 'r', 54: 's',
55: 't', 56: 'u', 57: 'v', 58: 'w', 59: 'x', 60: 'y', 61: 'z', 62: '!', 63: '@', 64: '#', 65: '$',
66: '%', 67: '^', 68: '&', 69: '*', 70: '(', 71: ')', 72: '_', 73: '+', 74: '=', 75: '-', 76: '[',
77: ']', 78: '{', 79: '}', 80: ';', 81: ':', 82: '|', 83: '/', 84: '?', 85: '.', 86: ','}
maxlen = 15

def getdk(d4):
    """анализирует дробную часть числа, ищет в ней повторения"""
    for i in xrange(0, len(d4)):
        for j in xrange(1, len(d4)):
            if j*int((len(d4)-i-j)/j)>=j and all([d4[i:i+j]==d4[i+j:][t:t+j] for t in xrange(0, j*int((len(d4)-i-j)/j), j)]):
                return d4[:i] + '(%s)' % d4[i:][i:i+j]
    return d4


def solver(a, b, k):
    """определение результата деления a/b в k-той системе счисления
    результат представлен в виде строки. В случае бесконечной периодической дроби,
    период заключается в скобки.
    Пример входных данных:
    1 2 8
    1 12 10
    Пример выходных данных:
    0.4
    0.08(3)"""
    if k > len(digits):
        print u'k are too long. There no symbols in dictionary to print result number.'
        return

    # получаем результат деления в десятичной системе счисления
    r10 = float(a)/float(b)

    # целую и дробную части числа будем преобразовывать по отдельности
    f1, f2 = modf(r10)
    #print 'k10 mantissa: %f, k10 d4: %f'  % (f2, f1)
    currentMod = int(f2)
    # целая часть числа в k-й системе счисления
    mantissa = ''
    while currentMod >= k:
        d = currentMod % k
        mantissa = digits[d] + mantissa
        currentMod = int(currentMod / k)
    mantissa = digits[currentMod] + mantissa

    # преобразуем дробную часть числа. Максимальную длину дробной части берём 13
    d4 = ''
    n = 0
    while f1 > 0:
        d4 += str(int(f1*k))
        f1 = modf(f1*k)[0]
        n += 1
        if n > maxlen:
            break
    print 
    return '%s.%s' % (str(mantissa), getdk(d4))


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.data = [(1, 2, 8), (1, 12, 10)]

    def test_01(self):
        self.assertEqual(solver(*self.data[0]), '0.4')


    def test_02(self):
        self.assertEqual(solver(*self.data[1]), '0.08(3)')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolver)
    unittest.TextTestRunner(verbosity=3).run(suite)
