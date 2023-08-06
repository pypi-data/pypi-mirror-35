"""Module for programatically working with financial quarters."""

import math
import calendar
import datetime


def _is_valid_quarter(quarter):
    """Is quarter within 1..4?"""
    return quarter and quarter > 0 and quarter <= 4


class QuarterDelta(object):
    """Class to represent differences between financial quarters."""

    def __init__(self, quarters=0, years=0):
        """Initialize QuarterDelta instance."""
        # If years or quarters is not int, throw an error.
        for val in years, quarters:
            if not isinstance(val, int):
                val_type = type(val)
                raise TypeError('integer argument expected, got {}'.format(
                    val_type))

        # Normalize values such that self.quarters is in the range [0,3].
        quotient, remainder = divmod(quarters, 4)
        self._years = years + quotient
        self._quarters = remainder

    @property
    def years(self):
        """Access read-only attribute years."""
        return self._years

    @property
    def quarters(self):
        """Access read-only attribute quarters."""
        return self._quarters

    def __repr__(self):
        """Representation of QuarterDelta instance."""
        return 'quarter.{0}({1}, {2})'.format(
            self.__class__.__name__,
            self._years,
            self._quarters)

    def __str__(self):
        """String conversion of QuarterDelta instance."""
        plural = lambda val: '' if val == 1 else 's'
        return '{0} {1}, {2} {3}'.format(
            self._years,
            'year' + plural(self._years),
            self._quarters,
            'quarter' + plural(self._quarters))

    def __add__(self, other):
        """Add two QuarterDeltas together."""
        if isinstance(other, QuarterDelta):
            return self.__class__(
                years=self._years + other.years,
                quarters=self._quarters + other.quarters)
        else:
            return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):
        """Subtract QuarterDelta from this QuarterDelta."""
        if isinstance(other, QuarterDelta):
            return self + -other
        else:
            return NotImplemented

    def __rsub__(self, other):
        """Subtract this QuarterDelta from QuarterDelta."""
        if isinstance(other, QuarterDelta):
            return -self + other
        else:
            return NotImplemented

    def __neg__(self):
        """Negate this QuarterDelta."""
        return self.__class__(
            years=-self._years,
            quarters=-self._quarters)

    def __pos__(self):
        """+ operator."""
        return self

    def __abs__(self):
        """Absolute value of a QuarterDelta."""
        if self.years < 0:
            return -self
        else:
            return self

    def __mul__(self, other):
        """Multiply QuarterDelta by an int."""
        if isinstance(other, int):
            return self.__class__(
                years=self._years * other,
                quarters=self._quarters * other)
        else:
            return NotImplemented

    __rmul__ = __mul__

    def __div__(self, other):
        """Divide QuarterDelta by an int."""
        if isinstance(other, int):
            quarters = self._years * 4 + self._quarters
            return self.__class__(years=0, quarters=quarters // other)
        else:
            return NotImplemented

    __floordiv__ = __div__

    def __eq__(self, other):
        """Equality operator."""
        if isinstance(other, QuarterDelta):
            return (
                self._years == other.years
                and self._quarters == other.quarters)
        else:
            return False

    def __ne__(self, other):
        """Not-equals operator."""
        return not self == other

    def __lt__(self, other):
        """Less-than operator."""
        if isinstance(other, QuarterDelta):
            return (
                self._years * 4 + self._quarters
                < other.years * 4 + other.quarters)
        else:
            raise TypeError(
                "can't compare {} to {}".format(
                    type(self).__name__,
                    type(other).__name__))

    def __le__(self, other):
        """LTE operator."""
        return self < other or self == other

    def __ge__(self, other):
        """GTE operator."""
        return not self < other

    def __gt__(self, other):
        """Greater-than operator."""
        return not self < other or self == other

    def __bool__(self):
        """Provide "if delta" functionality."""
        return self._years != 0 or self._quarters != 0


class Quarter(object):
    """Class to represent financial quarters in the vein of datetime."""

    def __init__(self, year, quarter):
        """Initialize Quarter."""
        if _is_valid_quarter(quarter):
            self._year = year
            self._quarter = quarter
        else:
            raise ValueError('quarter must be in 1..4')

    @property
    def year(self):
        """Access read-only attribute year."""
        return self._year

    @property
    def quarter(self):
        """Access read-only attribute quarter."""
        return self._quarter

    def __repr__(self):
        """Representation of Quarter."""
        return 'quarter.{0}({1}, {2})'.format(
            self.__class__.__name__,
            self._year,
            self._quarter)

    def iso_format(self):
        """Return a string in the vein of ISO (EX: 2018-Q1)."""
        return '{0}-Q{1}'.format(self._year, self._quarter)

    __str__ = iso_format

    def replace(self, year=None, quarter=None):
        """Return a new Quarter instance with specified values."""
        return Quarter(
            year or self._year,
            quarter or self._quarter)

    def __add__(self, other):
        """Add a QuarterDelta to self."""
        if isinstance(other, QuarterDelta):
            self_delta = QuarterDelta(self._year, self._quarter - 1)
            delta_sum = self_delta + other
            return Quarter(
                delta_sum.years,
                delta_sum.quarters + 1)
        else:
            return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):
        """Subtract a Quarter or QuarterDelta from self."""
        if isinstance(other, QuarterDelta):
            return self + -other
        elif isinstance(other, Quarter):
            self_quarters = self._year * 4 + self._quarter - 1
            other_quarters = other.year * 4 + other.quarter - 1
            return QuarterDelta(quarters=self_quarters - other_quarters)
        else:
            return NotImplemented

    def __eq__(self, other):
        """Equality operator."""
        if isinstance(other, Quarter):
            return (
                self._year == other.year
                and self._quarter == other.quarter)
        else:
            return False

    def __ne__(self, other):
        """Not-equals operator."""
        return not self == other

    def __lt__(self, other):
        """Less-than operator."""
        if isinstance(other, Quarter):
            return (
                self._year * 4 + self._quarter - 1
                < other.year * 4 + other.quarter - 1)
        else:
            return NotImplemented

    def __le__(self, other):
        """LTE operator."""
        return self < other or self == other

    def __gt__(self, other):
        """Greater-than operator."""
        return not self < other or self == other

    def __ge__(self, other):
        """GTE operator."""
        return not self < other

    @classmethod
    def from_date(cls, date):
        """Create Quarter instance from a datetime.date object."""
        year = date.year
        quarter = int(math.ceil(date.month / float(3)))
        return Quarter(year, quarter)

    def start_date(self):
        """Get start date of quarter."""
        return datetime.date(
            year=self.year,
            month=self.quarter * 3 - 2,
            day=1)

    def end_date(self):
        """Get end date of quarter."""
        end_month = self.quarter * 3
        return datetime.date(
            year=self.year,
            month=end_month,
            day=calendar.monthrange(self.year, end_month)[1])


def quarter_range(start, end, step=QuarterDelta(1)):
    """Get range of quarters."""
    curr = start
    while curr != end:
        yield curr
        curr += step
