#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
`ExtractionString` class extracts a substring from a parent string.

Its main original methods are

  - `partition(start,stop)` : which partitions the initial `ExtractionString` in three new `ExtractionString` instances, collected in a unique `ExtractionStrings` instance (see below)
  - `split([start,end, start2,end2, ...])` : which splits the `ExtractionString` in several instances grouped in a a list of `ExtractionString` objects
  - `slice(start, stop, size, step)` : which slices the initial string from position `start` to position `stop` by `step` in sub-strings of size `size`, all grouped in a list of `ExtractionString` objects

In addition, one can compare two `ExtractionString` using the non-overlapping order `<` and `>` or the overlapping-order `<=` and `>=` when two `ExtractionString`s overlap.

Finally, since a `ExtractionString` can be seen as a selection of a set of character positions from the parent string, one can apply the basic set operations to two `ExtractionString`s, in order to construct more elaborated `ExtractionString` instance.

"""

import warnings
from typing import Dict, List, Tuple, Union

from .even_sized_sorted_set import EvenSizedSortedSet as ESSS


# UTILITIES


class BoundaryWarning(Warning):
    """Warning when using ExtractionString."""

    pass


def _isExtractionString(extraction_string) -> bool:
    """Return True if `extraction_string` has all the attributes of an ExtractionString instance. False if not."""
    bools = [
        hasattr(extraction_string, attr)
        for attr in ["string", "intervals", "subtoksep"]
    ]
    return all(bools)


def _checkExtractionString(extraction_string):
    """Raise a ValueError in case `extraction_string` is not a proper ExtractionString instance."""
    if not _isExtractionString(extraction_string):
        raise ValueError("Accepts only ExtractionString instance")
    return None


def _checkSameString(obj1, obj2):
    """Raise a TypeError in case the two objects have not the same `.string` attribute. Raise an AttributeError in case at least one of the objects has no attribute `.string`."""
    if str(obj1.string) != str(obj2.string):
        s = obj1.__class__.__name__
        mess = "can only compare {} objects having same {}.string".format(s, s)
        raise TypeError(mess)
    return None


class ExtractionString:
    
    """`ExtractionString` object is basically a collection of a parent string named `string`, and a `intervals` collection (list of pairs of int) of positions. Its basic usage is its `str` method, which consists in a string extracted from all intervals defined in the `intervals` list, and joined by the `subtoksep` separator.
    
    
    Parameters
    ----------
    string : str
        parent string. Default is `str()`
    intervals : EvenSizedSortedSet or list of int
        a list of intervals, default is None, in which case the intervals are calculated to contain the entire string
    subtoksep : str
        a string, preferably of length 1, default is a white space `chr(32)`
    """

    def __init__(self,
                 string: str = "",
                 intervals: ESSS = None,
                 subtoksep: str = chr(32),
                 **kwargs) -> None:
        if isinstance(string, ExtractionString):
            _keys = ["string", "intervals", "subtoksep"]
            args = {k: v for k, v in string.__dict__.items() if k in _keys}
            self._init_extractstring(**args)
        else:
            self._init_extractstring(
                string=string, intervals=intervals, subtoksep=subtoksep
            )
        self._add_intervals_methods()
        return None

    def _init_extractstring(self, 
                            string: str = "", 
                            intervals: ESSS = None, 
                            subtoksep: str = chr(32)) -> None:
        self.string = str(string)
        self.subtoksep = str(subtoksep)
        # construct the intervals only when it is not passed as argument
        # keep empty list in case it is a list
        if isinstance(intervals, type(None)):
            self.intervals = ESSS(0, len(self.string)) if len(self.string) else ESSS()
        elif isinstance(intervals, ESSS):
            self.intervals = intervals
        else:
            self.intervals = ESSS(*intervals)
        if self.intervals:
            self._cut_intervals()
        return None

    def _add_intervals_methods(self) -> None:
        self.append = self.intervals.append
        self.remove = self.intervals.remove
        self.append_intervals = self.intervals.append_intervals
        self.remove_intervals = self.intervals.remove_intervals
        return None

    def _cut_intervals(self) -> None:
        """Withdraw the parts of the intervals that are beyond the string length."""
        start, stop = self.intervals.stop, len(self.string)
        start, stop = (start, stop) if start <= stop else (stop, start)
        self.intervals.remove(start, stop)
        start, stop = self.intervals.start, 0
        start, stop = (start, stop) if start <= stop else (stop, start)
        self.intervals.remove(start, stop)
        return None

    def _startstop(self, start: int, stop: int) -> Tuple[int, int]:
        """
        Tool function to catch the edge of the constructed string in the following methods.

        Works for both the Token and Tokens classes, if obj is passed as self.
        Recast start and stop inside the Token.string coordinates in case obj is a Token.string.

        Raise a BoundaryWarning in case at least one of the the start or stop has been changed.
        """
        start_, stop_ = start, stop
        if not stop and stop != 0:
            stop = len(self)
        if stop < 0 or stop > len(self):
            stop = len(self)
        if start > stop:
            start = stop
        if start < 0:
            start = 0
        if start_ != start or stop_ != stop:
            mess = "At least one of the boundaries has been modified"
            warnings.warn(mess, category=BoundaryWarning)
        return start, stop

    def __len__(self) -> int:
        """Return the length of the string associated with the ExtractionString."""
        length = sum(stop - start for start, stop in self.intervals)
        length += (len(self.intervals) - 1) * len(self.subtoksep)
        return max(length, 0)  # in case intervals is empty, length<0

    def __repr__(self) -> str:
        """Return the two main elements (namely the `string` and the `intervals` attributes) of a `ExtractionString` instance in a readable way."""
        mess = "{}".format(self.__class__.__name__)
        mess += "('{}', ".format(str(self))
        mess += "[" + ";".join(
            "(" + str(start) + "," + str(stop) + ")" for start, stop in self.intervals
        )
        mess += "])"
        return mess

    def __hash__(self) -> hash:
        """Make the Span object hashable, such that it can serve for set and dict.keys. Span is constructed on the unicity of the Span object, that is, this is the hash of the string made of the parent string, plus the string representation of the instance, including subtoksep. Everything is then converted to hash function."""
        return hash(tuple(self.intervals.list) + (self.string, self.subtoksep))

    def __str__(self) -> str:
        """`str(ExtractionString)` method returns the recombination of the extract of each `ExtractionString.subExtractionString` from the `ExtractionString.string` attribute corresponding to all its `ExtractionString.intervals` attribute, and joined by the `ExtractionString.subtoksep` character."""
        return self.intervals.apply(self.string, subtoksep=self.subtoksep)

    def __contains__(self, s: Union[str, 'ExtractionString']) -> bool:
        """If the object to be compared with is a ExtractionString related to the same string as this instance, check whether the intervals are overlapping. Otherwise, check whether the string str(s) (which transforms the other ExtractionString instance in a string in case s is not related to the same string) is a sub-string of the `ExtractionString` instance."""
        try:
            _checkExtractionString(s)
        except ValueError:
            b = str(s) in str(self)
        else:
            if s.string == self.string:
                b = any(
                    start1 <= start2 and stop1 >= stop2
                    for start1, stop1 in self.intervals
                    for start2, stop2 in s.intervals
                )
            else:
                b = False
        return b

    def __bool__(self) -> bool:
        """Return `True` if the `ExtractionString.intervals` is non-empty, otherwise return `False`."""
        return bool(len(self))

    def __getitem__(self, n: Union[int, slice]) -> str:
        """Allow slice and integer catch of the elements of the string of `ExtractionString`.

        Return a string.

        Note: As for the usual Python string, a slice with positions outside str(ExtractionString) will outcome an empty string, whereas ExtractionString[x] with x>len(ExtractionString) would results in an IndexError.
        """
        return str(self)[n]

    def get_extraction(self, n: int) -> 'ExtractionString':
        """
        Get the ExtractionString associated to the intervals elements n (being an integer or a slice).

        Return a ExtractionString object.
        Raise an IndexError in case n is larger than the number of intervals in self.intervals.
        """
        if len(self.intervals) <= n:
            raise IndexError(f"max index: {len(self.intervals)}")
        extract = self.__class__(
            string=self.string,
            intervals=self.intervals[2 * n: 2 * n + 2],
            subtoksep=self.subtoksep,
        )
        return extract

    @property
    def extractions(self) -> List['ExtractionString']:
        """Get the ExtractionString associated to each ExtractionString.intervals in a ExtractionString object.

        Return a list of ExtractionString objects.
        """
        return [self.get_extraction(i) for i in range(len(self.intervals))]

    def __eq__(self, extract) -> bool:
        """
        Verify whether the actual instance of ExtractionString and an extra ones have the same attributes.

        Returns a boolean.

        Raise a ValueError when one object is not a ExtractionString instance
        """
        bools = [
            extract.string == self.string,
            extract.intervals == self.intervals,
            extract.subtoksep == self.subtoksep,
        ]
        return all(bools)

    def __neq__(self, extract) -> bool:
        """
        Verify whether the actual instance of ExtractionString and an extra have any differing attribute.

        Returns a boolean.

        Raise a ValueError when one object is not a ExtractionString instance
        """
        bools = [
            extract.string != self.string,
            extract.intervals != self.intervals,
            extract.subtoksep != self.subtoksep,
        ]
        return any(bools)

    def copy(self) -> 'ExtractionString':
        """Copy the actual instance. Returns a new one."""
        new = self.__class__(
            string=self.string,
            intervals=self.intervals.copy(),
            subtoksep=self.subtoksep,
        )
        return new

    def __add__(self, extracst: 'ExtractionString') -> 'ExtractionString':
        """If the two `ExtractionString` objects have same strings, returns a new `ExtractionString` object with combined intervals of the initial ones."""
        return self.union(extracst)

    def __sub__(self, extracst: 'ExtractionString') -> 'ExtractionString':
        """If the two `ExtractionString` objects have same strings, returns a new `ExtractionString` object with intervals of self with `ExtractionString` intervals removed. Might returns an empty `ExtractionString`."""
        return self.difference(extracst)

    def __mul__(self, extracst: 'ExtractionString') -> 'ExtractionString':
        """If the two `ExtractionString` objects have same strings, returns a new `ExtractionString` object with intervals of self having intersection with `ExtractionString` intervals removed. Might returns an empty `ExtractionString`."""
        return self.intersection(extracst)

    def __truediv__(self, extracst: 'ExtractionString') -> 'ExtractionString':
        """If the two `ExtractionString` objects have same strings, returns a new `ExtractionString` object with intervals of self having symmetric difference with `ExtractionString` intervals removed. Might returns an empty `ExtractionString`."""
        return self.symmetric_difference(extracst)

    @property
    def start(self) -> int:
        """Return the starting position (an integer) of the first interval. Make sense only for contiguous `ExtractionString`."""
        return self.intervals[0]

    @property
    def stop(self) -> int:
        """Return the ending position (an integer) of the last intervals. Make sense only for contiguous `ExtractionString`."""
        return self.intervals[-1]

    def __lt__(self, extracst: 'ExtractionString') -> 'ExtractionString':
        """Return `True` if `ExtractionString` is entirely on the left of `extracst` (the `ExtractionString` object given as parameter). Make sense only for contiguous `ExtractionString` and non-empty ones."""
        _checkSameString(self, extracst)
        return self.intervals < extracst.intervals

    def __gt__(self, extracst: 'ExtractionString') -> 'ExtractionString':
        """Return `True` if `ExtractionString` is entirely on the right of `extracst` (the `ExtractionString` object given as parameter). Make sense only for contiguous `ExtractionString` and non-empty ones."""
        _checkSameString(self, extracst)
        return self.intervals > extracst.intervals

    def __le__(self, extracst: 'ExtractionString') -> 'ExtractionString':
        """Return `True` if `ExtractionString` is partly on the left of `extracst` (the `ExtractionString` object given as parameter). Make sense only for contiguous `ExtractionString` and non-empty ones."""
        _checkSameString(self, extracst)
        return self.intervals <= extracst.intervals

    def __ge__(self, extracst: 'ExtractionString') -> 'ExtractionString':
        """Return `True` if `ExtractionString` is partly on the right of `extracst` (the `ExtractionString` object given as parameter). Make sense only for contiguous `ExtractionString` and non-empty ones."""
        _checkSameString(self, extracst)
        return self.intervals >= extracst.intervals

    def _set_method_constructor(self,
                                method_name: str,
                                extracst: 'ExtractionString',
                                ) -> 'ExtractionString':
        """Apply the method of the `EvenSizedSortedSet` to the intervals in `extracst`."""
        _checkSameString(self, extracst)
        newIntervals = getattr(self.intervals, method_name)(extracst.intervals)
        newExtractionString = self.__class__(
            string=self.string,
            subtoksep=self.subtoksep,
            intervals=newIntervals,
        )
        return newExtractionString

    def union(self, extracst: 'ExtractionString') -> 'ExtractionString':
        """Take a `ExtractionString` object as entry, and return a new `ExtractionString` instance whose `ExtractionString.intervals` given by the union of the actual `ExtractionString.intervals` with the new `ExtractionString.intervals`, when one sees the `intervals` attributes as sets of positions of each instance.        

        Parameters
        ----------
        extracst : ExtractionString
            A ExtractionString object with same parent string (`ExtractionString.string`) and eventually different intervals that the actual instance.

        Returns
        -------
        new_extracst : ExtractionString
            An `ExtractionString` object with `new_extracst.intervals` given by the union of `new_extracst.intervals` and `extracst.intervals`.
        
        Raises
        ------
            ValueError
                in case the entry is not an `ExtractionString` instance.
            TypeError
                in case the span.string is not the same as `ExtractionString.string`.
        """
        return self._set_method_constructor("union", extracst)

    def difference(self, extracst: 'ExtractionString') -> 'ExtractionString':
        """Take a `ExtractionString` object as entry, and return a new `ExtractionString` instance whose `ExtractionString.intervals` given by the difference of the actual `ExtractionString.intervals` with the new `ExtractionString.intervals`, when one sees the `intervals` attributes as sets of positions of each instance.        

        Parameters
        ----------
        extracst : ExtractionString
            A ExtractionString object with same parent string (`ExtractionString.string`) and eventually different intervals that the actual instance.

        Returns
        -------
        new_extracst : ExtractionString
            An `ExtractionString` object with `new_extracst.intervals` given by the sdifference of `new_extracst.intervals` and `extracst.intervals`.
        
        Raises
        ------
            ValueError
                in case the entry is not an `ExtractionString` instance.
            TypeError
                in case the span.string is not the same as `ExtractionString.string`.
        """
        return self._set_method_constructor("difference", extracst)

    def intersection(self, extracst: 'ExtractionString') -> 'ExtractionString':
        """Take a `ExtractionString` object as entry, and return a new `ExtractionString` instance whose `ExtractionString.intervals` given by the intersection of the actual `ExtractionString.intervals` with the new `ExtractionString.intervals`, when one sees the `intervals` attributes as sets of positions of each instance.        

        Parameters
        ----------
        extracst : ExtractionString
            A ExtractionString object with same parent string (`ExtractionString.string`) and eventually different intervals that the actual instance.

        Returns
        -------
        new_extracst : ExtractionString
            An `ExtractionString` object with `new_extracst.intervals` given by the intersection of `new_extracst.intervals` and `extracst.intervals`.
        
        Raises
        ------
            ValueError
                in case the entry is not an `ExtractionString` instance.
            TypeError
                in case the span.string is not the same as `ExtractionString.string`.
        """
        return self._set_method_constructor("intersection", extracst)

    def symmetric_difference(self,
                             extracst: 'ExtractionString',
                             ) -> 'ExtractionString':
        """Take a `ExtractionString` object as entry, and return a new `ExtractionString` instance whose `ExtractionString.intervals` given by the symmetric difference of the actual `ExtractionString.intervals` with the new `ExtractionString.intervals`, when one sees the `intervals` attributes as sets of positions of each instance.        

        Parameters
        ----------
        extracst : ExtractionString
            A ExtractionString object with same parent string (`ExtractionString.string`) and eventually different intervals that the actual instance.

        Returns
        -------
        new_extracst : ExtractionString
            An `ExtractionString` object with `new_extracst.intervals` given by the symmetric difference of `new_extracst.intervals` and `extracst.intervals`.
        
        Raises
        ------
            ValueError
                in case the entry is not an `ExtractionString` instance.
            TypeError
                in case the span.string is not the same as `ExtractionString.string`.
        """
        return self._set_method_constructor("symmetric_difference", extracst)

    @property
    def relative2absolute(self) -> Dict[int, int]:
        """Construct the mapping between the absolute and relative coordinates. The relative coordinates that correspond to the artificial string given by the `subtoksep` are associated to a None value.

        For instance, the string `0123__678` corresponding to the intervals `(10,14);(20,23)` and the `subtoksep` `'__'` will have a `relative2absolute` mapping as `{0:10, 1:11, 2:12, 3:13, 4:None, 5:None, 6:20, 7:21, 8:22}`
        """
        rel2abs = {}
        relative = 0
        if len(self.intervals):
            start, stop = self.intervals[0:2]
            for absolute in range(start, stop):
                rel2abs[relative] = absolute
                relative += 1
        for start, stop in zip(self.intervals[2:-1:2], self.intervals[3::2]):
            for _ in range(len(self.subtoksep)):
                rel2abs[relative] = None
                relative += 1
            for absolute in range(start, stop):
                rel2abs[relative] = absolute
                relative += 1
        return rel2abs

    def get_relative2absolute(self, position: int) -> int:
        """Give the absolute position from a relative one.

        Parameters
        ----------
        position : int
            position in the relative string (the child one).

        Raises
        ------
        IndexError
            index out of range.

        Returns
        -------
        position: int
            position in the absolute string (the parent one).

        """
        try:
            position_ = self.relative2absolute[position]
        except KeyError:
            raise IndexError(f"index out of range: {position}")
        return position_

    def relative_to_absolute(self,
                             start: int,
                             stop: int,
                             step=1) -> Tuple[int, int, int, int]:
        """Shift the start and stop that represent positions in relative coordinates into start and stop in absolute coordinates.        

        Parameters
        ----------
        start : int
            position of the first character in the relative (child) string.
        stop : int
            position of the last character in the relative (child) string.
        step : int, optional
            step between two characters. The default is 1.

        Returns
        -------
        start : int
            position of the first character in the absolute (parent) string.
        stop : int
            position of the last character in the absolute (parent) string.
        nb_None_left : int
            number of empty characters at the left of the parent string.
        nb_None_right : int
            number of empty characters at the left of the parent string.
        """
        start_ = self.get_relative2absolute(start)
        nb_None_left = 0
        while start_ is None:
            start += step
            nb_None_left += 1
            start_ = self.get_relative2absolute(start)
        stop_ = self.get_relative2absolute(stop - 1)
        nb_None_right = 0
        while stop_ is None:
            stop -= step
            nb_None_right += 1
            stop_ = self.get_relative2absolute(stop - 1)
        return start_, stop_ + 1, nb_None_left, max(nb_None_right, 0)

    def extract(self, start: int, stop: int) -> 'ExtractionString':
        """Give the `ExtractionString` that is comprised in between the `start` and `stop` of the string representation of the actual object.
        

        Parameters
        ----------
        start : int
            position of the first character one wants to extract in the relative (child) string.
        stop : int
            position of the last character one wants to extract in the relative (child) string.

        Returns
        -------
        extraction : ExtractionString
            a copy of the actual instance, with modified `intervals` attribute.

        """
        extraction = self.copy()
        if start == stop:  # empty extraction
            extraction.intervals = ESSS()
            return extraction
        start_, stop_, nb_None_left, nb_None_right = self.relative_to_absolute(
            start, stop
        )
        intervals = extraction.intervals.intersection(ESSS(start_, stop_))
        extraction.intervals = intervals
        if nb_None_left and nb_None_right:
            # we are on a None all along: add the required number of empty
            for _ in range(stop - start + 1):  # +1 to generate the correct string
                extraction.intervals.append_empty(0)
        else:
            for _ in range(nb_None_left):
                extraction.intervals.append_empty(0)
            for _ in range(nb_None_right):
                extraction.intervals.append_empty(-1)
        return extraction

    def partition(self,
                  start: int,
                  stop: int,
                  remove_empty: bool = False) -> List['ExtractionString']:
        """Split the `ExtractionString.string`.

        Returns three `ExtractionString` objects :
        
         - `string[:start]`
         - `string[start:stop]`
         - `string[stop:]`
         
        and put all non-empty `ExtractionString` objects in a list of `ExtractionString` instances.

        It acts a bit like the `str.partition(s)` method of the Python `string` object, but `ExtractionString.partition` takes `start` and `stop` argument instead of a string.
        

        Parameters
        ----------
        start : int
            Starting position of the splitting sequence. 
        stop : int
            Ending position of the splitting sequence.
        remove_empty : bool, optional
            If `True`, returns a `list of ExtractionString` instance with only non-empty `ExtractionString` objects. The default is `False`. See `__bool__()` method for non-empty `ExtractionString`. 

        Returns
        -------
        list of `ExtractionString`
            The `list` object containing the different `ExtractionString` objects.
        """
        start, stop = (start, stop) if start < stop else (stop, start)
        list_extract = [
            self.extract(0, start),
            self.extract(start, stop),
            self.extract(stop, len(self)),
        ]
        if bool(remove_empty):
            list_extract = [x for x in list_extract if x]
        return list_extract

    def split(self,
              cuts,
              remove_empty: bool = False) -> List['ExtractionString']:
        """Split a text as many times as there are range entities in the cuts list.

        Return a list of `ExtractionString` instances.

        This is a bit like `str.split(s)` method from Python `string` object, except one has to feed `ExtractionString.split` with a full list of `start, stop` pair of integers instead of the string 's' in `str.split(s)`/ If the `start, stop` pair in cuts are given by a regex re.finditer search on `str(ExtractionString)`, the two methods give the same thing.


        Parameters
        ----------
        cuts : a list of pairs of int `start, stop`
            Basic usage is to take these cuts from [`re.finditer`](https://docs.python.org/3/library/re.html#re.finditer). The start/end integers are given in the relative coordinate system, that is, in terms of the position in `str(ExtractionString)`.
        remove_empty : bool, optional
            If `True`, returns a list of `ExtractionString` instance with only non-empty `ExtractionString` objects. The default is `False`. See `__bool__()` method for non-empty `ExtractionString`.

        Raises
        ------
        ValueError
            requires even number of starts and stops.

        Returns
        -------
        list_extract : list of `ExtractionString`
            The `list` object containing the different `ExtractionString` objects.

        """
        if len(cuts) % 2 == 1:
            raise ValueError("Requires even number of starts and stops")
        list_extract = []
        if len(cuts) > 0 and cuts[0] != 0:
            list_extract.append(self.extract(0, cuts[0]))
        for start, stop in zip(cuts[1:-1:2], cuts[2::2]):
            list_extract.append(self.extract(start, stop))
        # append the last element
        if len(cuts) > 0 and cuts[-1] != len(self):
            list_extract.append(self.extract(cuts[-1], len(self)))
        if remove_empty:
            list_extract = [s for s in list_extract if s]
        return list_extract

    def slice(self,
              start: int = 0,
              stop: int = None,
              size: int = 1,
              step: int = 1,
              remove_empty: bool = False) -> List['ExtractionString']:
        """Cut the `ExtractionString.string` in overlapping sequences of strings of size `size` by `step`, put all these sequences in separated `ExtractionString` objects, and finally put all theses objects in a list of `ExtractionString` instances..
        

        Parameters
        ----------
        start : int, optional
            The relative position where to start slicing the ExtractionString. The default is 0.
        stop : int, optional
            The relative position where to stop slicing the ExtractionString. The default is None.
        size : int, optional
            The size of the string in each subsequent ExtractionString objects. The default is 1.
        step : int, optional
            The number of characters skipped from one ExtractionString object to the next one. A character is given by `str(ExtractionString)` (called relative position). The default is 1.
        remove_empty : bool, optional
            If `True`, returns a list of `ExtractionString` instance with only non-empty `ExtractionString` objects. The default is `False`. See `__bool__()` method for non-empty `ExtractionString`.

        Returns
        -------
        list_extract : list of `ExtractionString`
            The `list` object containing the different `ExtractionString` objects.

        """
        start, stop = self._startstop(start, stop)
        list_extract = [self.extract(i, i + size) 
                        for i in range(start, stop - size + 1, step)]
        if remove_empty:
            list_extract = [s for s in list_extract if s]
        return list_extract
