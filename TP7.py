import math


class Fraction:
    """Class representing a fraction and operations on it

    Author : Thibault Delime
    Date : December 2023
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : numerator and denominator must be Integers.
        POST : create a Fraction as a new object, it is a reduced from.
        RAISES : ZeroDivisionError if den is 0.
        """
        if den == 0:
            raise ZeroDivisionError("denominator cant be equal to zero")
        elif type(num) == int and type(den) == int:
            if den < 0:
                num = - num
                den = - den
            gcd = math.gcd(num, den)
            self.__num = num // gcd
            self.__den = den // gcd
        else:
            raise ValueError("denominator and numerator must be integers !")

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : /
        POST : return a text who present the reduced form of the Object fraction.
        """
        if self.denominator == 1:
            return str(self.numerator)
        elif self.numerator == 0:
            return '0'
        else:
            return f'{self.numerator}/{self.denominator}'

    def as_mixed_number(self):
        """
        A mixed number is the sum of an integer and a proper fraction.
        That's means that the numerator is bigger than the denominator.

        PRE : /
        POST : Return a textual representation of the reduced form of the fraction as a mixed number
        """
        integer = self.numerator // self.denominator
        if integer == 0:
            return self.__str__()
        rest = self.numerator % self.denominator
        if rest == 0:
            return str(integer)
        return f"{integer} + {rest}/{self.denominator}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : /
         POST : Return a new Fraction object from the addition between arguments.
         RAISES : TypeError if other is not a Fraction object.
         """
        if isinstance(other, Fraction):
            num = self.numerator * other.denominator + self.denominator * other.numerator
            den = self.denominator * other.denominator
            return Fraction(num, den)
        else:
            raise TypeError

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : /
        POST : Return a new Fraction object from the subtraction between arguments.
        RAISES : TypeError if other is not a Fraction object.
        """
        if isinstance(other, Fraction):
            num = self.numerator * other.denominator - self.denominator * other.numerator
            den = self.denominator * other.denominator
            return Fraction(num, den)
        else:
            raise TypeError

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : /
        POST : Return a new Fraction object from the multiplication between arguments.
        RAISES : TypeError if other is not a Fraction object.
        """
        if isinstance(other, Fraction):
            num = self.numerator * other.numerator
            den = self.denominator * other.denominator
            return Fraction(num, den)
        else:
            raise TypeError

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : /
        POST : Return a new Fraction object from the division between arguments.
        RAISES : TypeError if other is not a Fraction object.
                ZeroDivisionError if the numerator is equal to 0.
        """
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError
            else:
                num = self.numerator * other.denominator
                den = self.denominator * other.numerator
            return Fraction(num, den)
        else:
            raise TypeError

    def __pow__(self, power):
        """Overloading of the ** operator for fractions

        PRE : The power value need to be an integer.
        POST : Return the power of a fraction.
        RAISES : ZeroDivisionError if the numerator is equal to 0.
        """
        if power == 0:
            return Fraction(1, 1)
        elif power < 0:
            if self.numerator == 0:
                raise ZeroDivisionError
            else:
                num = pow(self.denominator, - power)
                den = pow(self.numerator, - power)
                return Fraction(num, den)
        else:
            num = pow(self.numerator, power)
            den = pow(self.denominator, power)
            return Fraction(num, den)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : All arguments used need to be Fraction objects.
        POST : Return True if all arguments are the same and False if not.
        RAISES : TypeError if other is not a Fraction object.
        """
        if isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        else:
            raise TypeError

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : /
        POST : return the decimal value af a fraction object
        """
        return self.numerator / self.denominator

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : /
        POST : return True if the value of Fraction is equal to 0.
        """
        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : ?
        POST : return True if the reduced fraction is an integer
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : /
        POST : Return True if the absolute value of the fraction is less than one
        """

        return abs(self.numerator / self.denominator) < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : /
        POST : Return True if the numerator fraction is 1
        """
        return self.numerator == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacent if the absolute value of the difference them is a unit fraction

        PRE : All the arguments used must be Fraction objects
        POST : return True if the difference between the two fractions is a unit fraction
        RAISES : TypeError if other is not a Fraction object
        """
        if isinstance(other, Fraction):
            num = abs(self.numerator * other.denominator -
                      self.denominator * other.numerator)
            return num == 1
        else:
            raise TypeError
