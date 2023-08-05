#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A NonOverlappingPositions is a collections of positions in a text."""

from typing import Dict, List, Union

from .even_sized_sorted_set import EvenSizedSortedSet


class NonOverlappingPositions(EvenSizedSortedSet):
    """Test the possibility to extract the positions instead of the slices."""

    def __len__(self) -> int:
        """Give the number of positions in the instance."""
        return sum(
            stop - start for start, stop in zip(self.list[:-1:2], self.list[1::2])
        )

    def __getitem__(self, n: Union[int, slice]) -> Union[int, List[int]]:
        """
        Allow slice and integer catch of the elements of the string of `NonOverlappingPositions`.

        When an integer is given, returns a `slice` object.

        When a slice is passed to the `NonOverlappingIntervals`, returns a `NonOverlappingIntervals` instance with the corresponding intervals.
    

        Parameters
        ----------
        n : Union[int, slice]
            As for a list.

        Raises
        ------
        ValueError
            argument must be either integer or slice.

        Returns
        -------
        Union[slice, NonOverlappingIntervals]
            if n is an int, return an int, if n is a slice, return list of int.

        """
        if isinstance(n, int):
            return self.relative2absolute[n]
        elif isinstance(n, slice):
            L = self.relative2absolute.__len__()
            # capture the possible None, that can't be multiplied
            start = n.start if n.start is not None else 0
            # do not exceed the last element:
            stop = min(n.stop, L) if (n.stop is not None) else L
            # in case of negative stop
            stop = L + stop if stop < 0 else stop
            return [
                self.relative2absolute[i]
                for i in (
                    range(start, stop) if n.step is None else range(start, stop, n.step)
                )
            ]
        else:
            raise ValueError("argument must be either integer or slice")
        return None

    def __iter__(self) -> int:
        """Yield the positions that corresponds to the non-overlapping positions."""
        for i in range(len(self.relative2absolute)):
            yield self.relative2absolute[i]

    @property
    def relative2absolute(self) -> Dict[int, int]:
        """Overclass the `relative2absolute` dictionary of the mother class."""
        rel2abs, relpos = {}, 0
        for start, stop in zip(self.list[:-1:2], self.list[1::2]):
            for abspos in range(start, stop):
                rel2abs[relpos] = abspos
                relpos += 1
        return rel2abs
