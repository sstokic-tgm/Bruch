from __future__ import division, print_function, unicode_literals


class Bruch(object):
    """
    Bruch
    :param int zaehler: numerator
    :param int nenner: denominator
    :ivar int zaehler: numerator
    :ivar int nenner: denominator
    """

    def __iter__(self):

        return (self.zaehler, self.nenner).__iter__()

    def __init__(self, zaehler=0, nenner=1):
        """
        constructor
        :raise TypeError: inkompatible Typen
        :param zaehler: Bruch oder int
        :param nenner: int - darf nicht 0 sein
        """
        if isinstance(zaehler, Bruch):
            self.zaehler, self.nenner = zaehler
            return
        elif type(zaehler) is not int:
            raise TypeError('incompatible type:' + type(zaehler).__name__)
        elif type(nenner) is not int:
            raise TypeError('incompatible type:' + type(nenner).__name__)
        if nenner == 0:
            raise ZeroDivisionError
        self.zaehler = zaehler
        self.nenner = nenner

    def __float__(self):

        return self.zaehler / self.nenner

    def __int__(self):

        return int(self.__float__())

    def __neg__(self):

        return Bruch(-self.zaehler, self.nenner)

    def __radd__(self, zaehler):

        return self.__add__(zaehler)

    def __add__(self, zaehler):

        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:' + type(zaehler).__name__ + ' + Bruch()')
        nennerNeu = self.nenner * n2
        zaehlerNeu = z2 * self.nenner + n2 * self.zaehler
        return Bruch(zaehlerNeu, nennerNeu)

    def __complex__(self):

        return complex(self.__float__())

    def __rsub__(self, left):

        if type(left) is int:
            z2 = left
            nennerNeu = self.nenner
            zaehlerNeu = z2 * self.nenner - self.zaehler
            return Bruch(zaehlerNeu, nennerNeu)
        else:
            raise TypeError('incompatible types:' + type(left).__name__ + ' - Bruch()')

    def __sub__(self, zaehler):

        return self.__add__(zaehler * -1)

    def __rmul__(self, zaehler):

        return self.__mul__(zaehler)

    def __mul__(self, zaehler):

        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:' + type(zaehler).__name__ + ' * Bruch()')
        z2 *= self.zaehler
        n2 *= self.nenner
        return Bruch(z2, n2)

    def __pow__(self, p):

        if type(p) is int:
            return Bruch(self.zaehler ** p, self.nenner ** p)
        else:
            raise TypeError('incompatible types:' + type(p).__name__ + ' should be an int')

    def __rdiv__(self, other):

        return self.__rtruediv__(other)

    def __rtruediv__(self, left):

        if type(left) is int:
            z2 = left * self.nenner
            if self.zaehler == 0:
                raise ZeroDivisionError
            return Bruch(z2, self.zaehler)
        else:
            raise TypeError('incompatible types:' + type(left).__name__ + ' / Bruch()')

    def __div__(self, other):

        return self.__truediv__(other)

    def __truediv__(self, zaehler):

        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:' + type(zaehler).__name__ + ' / Bruch()')
        if z2 == 0:
            raise ZeroDivisionError
        return self.__mul__(Bruch(n2, z2))

    def __invert__(self):

        return Bruch(self.nenner, self.zaehler)

    def __repr__(self):

        # Vor der Ausgabe wird gekuerzt!
        shorten = Bruch.gcd(self.zaehler, self.nenner)
        self.zaehler //= shorten
        self.nenner //= shorten
        # Nenner stehts positiv
        if self.nenner < 0:
            self.nenner *= -1
            self.zaehler *= -1

        if self.nenner == 1:
            return "(%d)" % self.zaehler
            # return "({:d})".format(self.zaehler)
        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)
            # return "({:d}/{:d})".format(self.zaehler, self.nenner)

    @staticmethod  # not necessary in python >= 3.x
    def __makeBruch(other):

        if isinstance(other, Bruch):
            return other
        elif type(other) is int:
            b = Bruch(other, 1)
            return b
        else:
            raise TypeError('incompatible types:' + type(other).__name__ + ' not an int nor a Bruch')

    def __eq__(self, other):

        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner == other.zaehler * self.nenner

    def __ne__(self, other):

        return not self.__eq__(other)

    def __gt__(self, other):

        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner > other.zaehler * self.nenner

    def __lt__(self, other):

        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner < other.zaehler * self.nenner

    def __ge__(self, other):

        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner >= other.zaehler * self.nenner

    def __le__(self, other):

        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner <= other.zaehler * self.nenner

    def __abs__(self):

        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __iadd__(self, other):

        other = Bruch.__makeBruch(other)
        self = self + other
        return self

    def __isub__(self, other):

        other = Bruch.__makeBruch(other)
        self = self - other
        return self

    def __imul__(self, other):

        other = Bruch.__makeBruch(other)
        self = self * other
        return self

    def __idiv__(self, other):

        return self.__itruediv__(other)

    def __itruediv__(self, other):

        other = Bruch.__makeBruch(other)
        self = self / other
        return self

    @classmethod
    def gcd(cls, x, y):

        x, y = abs(x), abs(y)
        if x < y: x, y = y, x

        while y != 0:
            x, y = y, x % y
        return x