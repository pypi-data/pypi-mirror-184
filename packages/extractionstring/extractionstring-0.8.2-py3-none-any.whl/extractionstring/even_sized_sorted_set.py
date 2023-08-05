#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
`EvenSizedSortedSet` class represents a collection of non-overlapping intervals.

One can compare two `EvenSizedSortedSet` instances using the non-overlapping order `<` and `>` or the overlapping-order `<=` and `>=` when two `EvenSizedSortedSet` instances overlap.

Since a `EvenSizedSortedSet` can be seen as a selection of a set of positions, one can apply the basic set operations to two `EvenSizedSortedSet` instances, in order to construct more elaborated objects.
"""

from typing import Generator, List, Tuple, Union


class EvenSizedSortedSet(list):
    """An `EvenSizedSortedSet` object is basically a collection of sorted integers without duplicated entity, and whose length is an even number.

    As an iterator an `EvenSizedSortedSet` will yield tuples of integers, representing the start and stop positions of each sub-intervals given by two-consecutive integers in the `EvenSizedSortedSet`.

    In addition it has basic ordering and set-like methods as well.
    
    `EvenSizedSortedSet` attributes are just a collection of unique sorted integers. Then a collection of non-overlapping intervals can be represented as a list, e.g. (10,12,16,18,22,26) that represents the integers {10,11 , 16,17 , 22,23,24,25} corresponding to the integer positions of an other iterable (in `ExtractionString` the iterable is a string for instance).

    Each even-positioned element will be considered as a start index, while each consecutive odd-positioned element will be considered as a stop index, i.e. one sees the elements of an `EvenSizedSortedSet` as a collection `[start0, stop0, start1, stop1, start2, stop2, ...]` where each `[start, stop]` object is a sub-set of the `EvenSizedSortedSet` instance. The indexes can then be used in an other iterable (such as e.g. a string) to construct non-overlapping intervals.

    One can pass the collection of integers in any order, the instanciation will sort them and make each integer unique. This could be confusing, for instance giving (2,4,6,8,8,9,10,12,7,10) may be thought as giving the ensemble of intervals `(2,4) U (6,8) U (8,9) U (10,12) U (7,10)` which is equal to `(2,4) U (6,12)` in terms of intervals, whereas the instantiation will give an `EvenSizedSortedSet` representing (2,4,6,8,9,10,12). This is the only way to represent in a unique fashion a non-overlapping object, and attribute a hash function to it. In short, the algebra or recovering several intervals is not done at instanciation, and one may use `append` or `remove` methods later (and their extensions: `union`, `intersection`, `symmetric difference` and `difference`).

    Raise a `ValueError` in case the number of unique sorted integers is not even.    
    """

    def __init__(self, *integers):
        if not integers:  # empty object
            super().__init__([])
            return None
        esss = sorted(set(integers))
        if len(esss) % 2 != 0:
            raise ValueError("takes only even number of unique sorted integers")
        super().__init__(esss)
        return None

    def __repr__(self) -> str:
        """Return the intervals in a readable way."""
        mess = "{}".format(self.__class__.__name__)
        mess += "[" + ";".join(f"({start},{stop})" for start, stop in self)
        mess += "]"
        return mess

    @property
    def list(self) -> List[int]:
        """The list of unique sorted integers.
        
        In particular, this serves as a tool to instanciate a new object.


        Returns
        -------
        List[int]
            a list of even sized sorted integers, that can be fed to a new `EvenSizedSortedSet` instance


        Examples
        --------
        >>> esss = EvenSizedSortedSet(2,4,8,12)
        >>> new_esss = EvenSizedSortedSet(*esss.list)
        """
        return list(super().__iter__())

    def __iter__(self) -> Generator[None, None, Tuple[int, int]]:
        """Iter over the tuples formed by the start and stop positions of the
        object."""
        for i in range(0, super().__len__(), 2):
            start = super().__getitem__(i)
            stop = super().__getitem__(i + 1)
            yield start, stop

    def __len__(self) -> int:
        """The number of sub-sets in the `EvenSizedSortedSet`."""
        return super().__len__() // 2

    def __abs__(self) -> int:
        """The number of integers contained in all sub-sets."""
        return sum(stop - start for start, stop in self)

    def __bool__(self) -> bool:
        """Return `True` if the `EvenSizedSortedSet` is non-empty, otherwise return `False`"""
        return bool(len(self))

    def __hash__(self) -> hash:
        """Return the hash value of the tuple representation of the ordered list of even number of non-equals integers."""
        return hash(tuple(self.list))

    def __get_condition_temp(self, start: int, stop: int,
                             ) -> Tuple[bool, bool, List[int], List[int]]:
        """Utility for the append and remove range methods."""
        start, stop = (start, stop) if start < stop else (stop, start)
        start_, stop_ = start - 0.5, stop + 0.5
        intervals = sorted(self.list + [start_, stop_])
        start_pos, stop_pos = intervals.index(start_), intervals.index(stop_)
        condition1 = start_pos % 2
        condition2 = (stop_pos - start_pos) % 2
        temp2 = intervals[stop_pos + 1 :]
        temp1 = intervals[:start_pos]
        return condition1, condition2, temp1, temp2

    def append(self, start: int, stop: int) -> 'EvenSizedSortedSet':
        """Append an interval (start and stop positions) to the actual object. If a position is inside a previous sub-set or extend a previous sub-set, the collection of sub-sets evolves accordingly such as always representing some `EvenSizedSortedSet`.
        
        Returns self (appends in-place)"""
        condition1, condition2, temp1, temp2 = self.__get_condition_temp(start, stop)
        if not condition1 and condition2:
            temp1.extend([start, stop])
        elif not condition1 and not condition2:
            temp1.extend([start])
        elif condition1 and not condition2:
            temp1.extend([stop])
        temp1.extend(temp2)
        self.__init__(*temp1)
        return self

    def append_intervals(self, *starts_stops) -> 'EvenSizedSortedSet':
        """Append a list of start, stop positions.
        
        This method applies `append_range` several times, see its documentation for more details.
        """
        if len(starts_stops) % 2 != 0:
            raise ValueError("must receive even number of elements")
        intervals = sorted(starts_stops)
        for start, stop in zip(intervals[:-1:2], intervals[1::2]):
            self.append(start, stop)
        return self

    def extend(self, nonov) -> 'EvenSizedSortedSet':
        """Add many positions to the `EvenSizedSortedSet`"""
        return self.append_intervals(*nonov)

    def remove(self, start: int, stop: int) -> 'EvenSizedSortedSet':
        """Remove the interval (start, stop) from `EvenSizedSortedSet`.
        
        If a position is outside a previous sub-set or truncate a previous sub-set, the collection of sub-sets evolves accordingly such as always representing some `EvenSizedSortedSet`.
        
        Returns self (removes in-place).
        """
        condition1, condition2, temp1, temp2 = self.__get_condition_temp(start, stop)
        if not condition1 and not condition2:
            temp1.extend([stop])
        elif condition1 and not condition2:
            temp1.extend([start])
        elif condition1 and condition2:
            temp1.extend([start, stop])
        temp1.extend(temp2)
        self.__init__(*temp1)
        return self

    def remove_intervals(self, *starts_stops) -> 'EvenSizedSortedSet':
        """Remove a list of start, stop positions.
        
        This method applies `remove` several times, see its documentation for more details.
        """
        if len(starts_stops) % 2 != 0:
            raise ValueError("must receive even number of elements")
        intervals = sorted(starts_stops)
        for start, stop in zip(intervals[:-1:2], intervals[1::2]):
            self.remove(start, stop)
        return self

    def append_empty(self, position: int) -> 'EvenSizedSortedSet':
        """Append an empty interval (in the form `(x,x)` in the main object) either to the left or right position of the list of intervals.
        
        This clearly violates the definition of the `EvenSizedSortedSet`, so the empty interval that is added is supposed to be withdrawn at any implementation of the so-generated interval list.

        Examples
        --------
        >>> esss = EvenSizedSortedSet(2,4,6,8)
        >>> esss.append_empty(0)  # returns (2,2,2,4,6,8)
        >>> new_esss = EvenSizedSortedSet(*esss.list)  # returns (2,4,6,8)

        so the extra 2 have been withdrawn, due to the definition of a `EvenSizedSortedSet`.
        """
        if position == 0:
            m = self[0] if self else 0
            super().insert(0, m)
            super().insert(0, m)
        elif position == -1:
            m = self[-1] if self else 0
            super().extend([m, m])
        else:
            mess = "the position is either 0 or -1 to append on left or right"
            mess += " of the EvenSizedSortedSet"
            raise ValueError(mess)
        return self

    def interval_index(self,
                       position: int,
                       outside_index: slice=slice(0, 0)):
        """Finds the index of the interval into which the position is included."""
        if position in self.list:
            index = super().index(position)
            flag = 2 * (index % 2) - 1
            # right border is not in the interval:
            index = index // 2 if flag != 1 else outside_index
        else:
            index = sorted(
                self.list
                + [
                    position,
                ]
            ).index(position)
            # not in an interval: return None, else the position in self
            index = outside_index if index % 2 == 0 else index // 2
        return index

    def __contains__(self, s: Union[int, 'EvenSizedSortedSet']) -> bool:
        """Is `s` inside the `EvenSizedSortedSet`?
        
        If the object to be compared with is an `EvenSizedSortedSet`, returns `True` in case the intervals are overlapping.
        If the object is an `int`, returns `True` if the position is in the `EvenSizedSortedSet`.

        Parameters
        ----------
        s : int or EvenSizedSortedSet
            The object to be compared with.

        Raises
        ------
        ValueError
            requires either an `int` or an `EvenSizedSortedSet` object.

        Returns
        -------
        bool
            True in case `s` is inside `EvenSizedSortedSet`. False if not.

        """
        if isinstance(s, int):
            b = any(start <= s and s < stop for start, stop in self)
        elif isinstance(s, EvenSizedSortedSet):
            b = any(
                start1 <= start2 and stop1 >= stop2
                for start1, stop1 in self
                for start2, stop2 in s
            )
        else:
            raise ValueError("requires an int or an EvenSizedSortedSet object")
        return b

    def is_subset(self, s: Union[Tuple[int, int], 
                                 'EvenSizedSortedSet']) -> bool:
        """If the object to be compared with as an `EvenSizedSortedSet`, returns True in case its (start, stop) is in the sub-set of the present object, otherwise returns False.
        
        If the object to be compared with is a len-2 tuple, returns True if the positions is in the present object, otherwise returns False.

        Parameters
        ----------
        s : int or EvenSizedSortedSet
            The object to be compared with.

        Raises
        ------
        ValueError
            requires either an `int` or an `EvenSizedSortedSet` object.
            
        """
        if isinstance(s, tuple):
            start, stop = s
            b = (start, stop) in [s for s in self]
        elif isinstance(s, EvenSizedSortedSet):
            b = (s.start, s.stop) in [s for s in self]
        else:
            raise ValueError(
                "requires a tup of int or an EvenSizedSortedSet object"
            )
        return b

    @property
    def start(self) -> int:
        """Returns the start position (an int) of the first sub-set.
        Make sense only for contiguous `EvenSizedSortedSet` of length 1.
        Raises an `IndexError` in case of empty object."""
        return super().__getitem__(0)

    @property
    def stop(self) -> int:
        """Returns the stop position (an int) of the last sub-set.
        Make sense only for contiguous `EvenSizedSortedSet` of length 1.
        Raises an `IndexError` in case of empty object."""
        return super().__getitem__(-1)

    def __lt__(self, esss: 'EvenSizedSortedSet') -> bool:
        """Returns `True` if the actual `EvenSizedSortedSet` is entirely on the left of the given `EvenSizedSortedSet`. Otherwise returns `False`.
        Make sense only for contiguous `EvenSizedSortedSet` of length 1."""
        return self.stop <= esss.start

    def __gt__(self, esss: 'EvenSizedSortedSet') -> bool:
        """Returns `True` if the actual `EvenSizedSortedSet` is entirely on the right of the given `EvenSizedSortedSet`. Otherwise returns `False`.
        Make sense only for contiguous `EvenSizedSortedSet` of length 1."""
        return esss.stop <= self.start

    def __le__(self, esss: 'EvenSizedSortedSet') -> bool:
        """Returns `True` if the actual `EvenSizedSortedSet` is partly on the
        left of the given `EvenSizedSortedSet`. Otherwise returns `False`.
        Make sense only for contiguous EvenSizedSortedSet of length 1."""
        exception = self.start == esss.start and self.stop < esss.stop
        return self.start < esss.start < self.stop or exception

    def __ge__(self, esss: 'EvenSizedSortedSet') -> bool:
        """Returns `True` if the actual `EvenSizedSortedSet` is partly on the right of the given `EvenSizedSortedSet`. Otherwise returns `False`.
        Make sense only for contiguous `EvenSizedSortedSet` of length 1."""
        exception = self.start == esss.start and esss.stop < self.stop
        return esss.start < self.start < esss.stop or exception

    def __add__(self, esss: 'EvenSizedSortedSet') -> 'EvenSizedSortedSet':
        """Alias for the union of two `EvenSizedSortedSet` instances."""
        return self.union(esss)

    def __sub__(self, esss: 'EvenSizedSortedSet') -> 'EvenSizedSortedSet':
        """Alias for the difference of two `EvenSizedSortedSet` instances."""
        return self.difference(esss)

    def __mul__(self, esss: 'EvenSizedSortedSet') -> 'EvenSizedSortedSet':
        """Alias for the intersection of two `EvenSizedSortedSet` instances."""
        return self.intersection(esss)

    def __truediv__(self, esss: 'EvenSizedSortedSet') -> 'EvenSizedSortedSet':
        """Alias for the symmetric difference of two `EvenSizedSortedSet` instances."""
        return self.symmetric_difference(esss)

    def union(self, esss: 'EvenSizedSortedSet') -> 'EvenSizedSortedSet':
        """
        Takes an `EvenSizedSortedSet` object as entry, and returns a new `EvenSizedSortedSet` instance representing the union of the two `EvenSizedSortedSet` instances.
        Returns a new instance of `EvenSizedSortedSet`.
        """
        newNonOv = self.__class__(*self.list).append_intervals(*esss.list)
        return newNonOv

    def difference(self, esss: 'EvenSizedSortedSet') -> 'EvenSizedSortedSet':
        """
        Takes an `EvenSizedSortedSet` object as entry, and returns a new `EvenSizedSortedSet` instance representing the difference of the two `EvenSizedSortedSet` instances.
        Returns a new instance of `EvenSizedSortedSet`.
        """
        newNonOv = self.__class__(*self.list).remove_intervals(*esss.list)
        return newNonOv

    def intersection(self, esss: 'EvenSizedSortedSet') -> 'EvenSizedSortedSet':
        """
        Takes an `EvenSizedSortedSet` object as entry, and returns a new `EvenSizedSortedSet` instance representing the intersection of the two `EvenSizedSortedSet` instances.
        Returns a new instance of `EvenSizedSortedSet`.
        """
        # one uses the fact that AxB = A+B-(A-B)-(B-A)
        # A-B
        AmB = self.__class__(*self.list).remove_intervals(*esss.list)
        # B-A
        BmA = self.__class__(*esss.list).remove_intervals(*self.list)
        # A+B
        newNonOv = self.__class__(*self.list).append_intervals(*esss.list)
        # A+B - (A-B)
        newNonOv.remove_intervals(*AmB.list)
        # A+B - (A-B) - (B-A)
        newNonOv.remove_intervals(*BmA.list)
        return newNonOv

    def symmetric_difference(self, esss: 'EvenSizedSortedSet') -> 'EvenSizedSortedSet':
        """
        Takes an `EvenSizedSortedSet` object as entry, and returns a new `EvenSizedSortedSet` instance representing the symmetric difference of the two `EvenSizedSortedSet` instances.
        Returns a new instance of `EvenSizedSortedSet`.
        """
        # one uses the fact that A/B = (A-B)+(B-A)
        # A-B
        AmB = self.__class__(*self.list).remove_intervals(*esss.list)
        # B-A
        BmA = self.__class__(*esss.list).remove_intervals(*self.list)
        # does the union of intervals: (A-B)+(B-A)
        newNonOv = self.__class__(*AmB.list).append_intervals(*BmA.list)
        return newNonOv

    def apply(self, string: str, subtoksep: str = chr(32)) -> str:
        """Extract the sub-parts of the `string` that correspond to the `EvenSizedSortedSet` object.
        Returns a string composed by the sub-strings of each sub-set, joined by the `subtoksep` (default is white space)."""
        return subtoksep.join(string[start:stop] for start, stop in self)
