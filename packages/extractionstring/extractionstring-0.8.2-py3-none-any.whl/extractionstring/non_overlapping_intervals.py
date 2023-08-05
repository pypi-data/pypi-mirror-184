#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""`NonOverlappingIntervals` class represents a collection of non-overlapping intervals."""

from typing import Union

from .even_sized_sorted_set import EvenSizedSortedSet


class NonOverlappingIntervals(EvenSizedSortedSet):
    """A `NonOverlappingIntervals` object is basically a collection of sorted integers without duplicated entity, and whose length is an even number.

    As an iterator a `NonOverlappingIntervals` will yield slices objects.

    In addition it has basic ordering and set-like methods as well.
    """

    def __getitem__(self, n: Union[int, slice]) -> Union[slice, EvenSizedSortedSet]:
        """
        Allow slice and integer catch of the elements of the string of `NonOverlappingIntervals`.

        When an integer is given, returns a `slice` object.

        When a slice is passed to the `NonOverlappingIntervals`, returns a `NonOverlappingIntervals` instance with the corresponding intervals.
    

        Parameters
        ----------
        n : Union[int, slice]
            As for a list.

        Raises
        ------
        IndexError
            list index out of range.
        ValueError
            argument must be either integer or slice.

        Returns
        -------
        Union[slice, NonOverlappingIntervals]
            if n is an int, return a slice, if n is a slice, return a NonOverlappingIntervals.

        """
        if isinstance(n, int):
            if n >= len(self):
                raise IndexError("list index out of range")
            # in case n=-1, stop is None, not 0
            stop = 2 * n + 2 if 2 * n + 2 else None
            return slice(*self.list.__getitem__(slice(2 * n, stop)))
        elif isinstance(n, slice):
            L = 2 * super().__len__()
            # capture the possible None, that can't be multiplied
            start = 2 * n.start if (n.start is not None) else 0
            # do not exceed the last element:
            stop = min(2 * n.stop, L) if (n.stop is not None) else L
            # in case of negative stop
            stop = L + stop if stop < 0 else stop
            # step can be 0 or None
            step = max(2 * n.step - 2, 0) if n.step else 0
            intervals = []
            pos = start
            while pos < stop:
                intervals.extend([self.list[pos], self.list[pos + 1]])
                pos += 2 + step
            return self.__class__(*intervals)
        else:
            raise ValueError("argument must be either integer or slice")

    def __iter__(self) -> slice:
        """
        Yield the slices that corresponds to the non-overlapping intervals.

        Yields
        ------
        slice(start, stop) : slice
            with only start and stop parameters, step is always 1.

        """
        for start, stop in zip(self.list[:-1:2], self.list[1::2]):
            yield slice(start, stop)

    def __repr__(self) -> str:
        """
        Return the intervals in a readable way.

        Returns
        -------
        mess : str
            string describing the object.

        """
        mess = "{}".format(self.__class__.__name__)
        mess += "[" + ";".join(f"({s.start},{s.stop})" for s in self)
        mess += "]"
        return mess

    def __abs__(self) -> int:
        """
        Return the total number of positions inside the NonOverlappingIntervals.

        Returns
        -------
        int
            total number of integers contained in the object.

        """
        return sum(sl.stop - sl.start for sl in self)
