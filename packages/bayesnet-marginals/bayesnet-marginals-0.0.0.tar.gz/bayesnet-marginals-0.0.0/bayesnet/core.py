import operator
from abc import abstractmethod
from itertools import product
from functools import reduce
from typing import Iterable
from typing import Sequence
from typing import Generator
from typing import Tuple

import numpy as np

from recur.abc import Recursive


class AbstractProbabilityMassFunction(Recursive):

    def __init__(self, variables: Sequence['DiscreteRandomVariable']):
        """Create a new probability mass function."""

        # The variables must all be discrete random variables.
        if not all([isinstance(v, DiscreteRandomVariable) for v in variables]):
            raise TypeError('The variables must be instances of the'
                            'bn.DiscreteRandomVariable class.')

        # The variables are ordered and cannot have duplicates.
        self._variables = OrderedSet(variables)

        # The size of the table if the number of possible outcomes.
        self._size = reduce(operator.mul, (len(v) for v in self.variables))

    @property
    def events(self) -> Generator[Tuple, None, None]:
        """Returns a generator for the events of the PMF."""
        domains = tuple(v.domain for v in self.variables)
        return (e for e in product(*domains))

    @property
    def nb_variables(self) -> int:
        """The number of variables of the PMF."""
        return len(self.variables)

    @property
    @abstractmethod
    def probabilities(self) -> np.ndarray:
        """Returns the probabilities of the PMF

        Returns the probabilities of the PMF, which is a numpy array of
        float with as many elements as there are combinations of states of
        the variables of the PMF.

        """
        pass

    @property
    def size(self) -> int:
        """The number of possible outcomes of the mass function."""
        return self._size

    @property
    def variables(self) -> 'OrderedSet[DiscreteRandomVariable]':
        """Returns the variables of the PMF

        Returns the variables of the PMF, which is an immutable ordered set
        of discrete variables.

        """
        return self._variables

    def __recur__(self) -> Iterable['AbstractProbabilityMassFunction']:
        """Return the source PMFs. For a pure PMF, there are none."""
        return ()

    def __contains__(self, variable) -> bool:
        """Indicates if variable is included in the variables of the PMF."""
        return variable in self._variables

    def __repr__(self) -> str:
        """Unambiguous string representation for PMFs."""
        return 'PMF over {} with {} events'.format(self.variables, self.size)

    def __str__(self) -> str:
        """Readable string representation for PMFs."""

        out = ''

        # Build the header.
        for variable in self.variables:
            out += '{:<5} '.format(variable.symbol[:5])
        out += '\n'
        out += '------' * self.nb_variables
        out += '----\n'

        # Add the probabilities for each event.
        for i, event in enumerate(self.events):
            for subevent in event:
                out += '{:<5} '.format(subevent)
            out += '{:>4.2f}\n'.format(self[i])

        return out


class OrderedSet(tuple):

    def __new__(cls, iterable):
        """Represents an ordered sequence of unique items.

        The `OrderedSet` implements an immutable ordered sequence of
        unique items.

        Args:
            iterable: An `Iterable`. The items of the set. Must not contain
                duplicates.

        Raises:
            ValueError: If the iterable contains duplicates.

        """

        # The iterable must not contain duplicates.
        if len(set(iterable)) != len(iterable):
            raise ValueError(
                'The iterable must not contain duplicates.')

        self = tuple.__new__(cls, iterable)

        return self

    def __and__(self, *others):
        """Intersection between `OrderedSet`s.

        The intersection of `OrderedSet`s returns a new `OrderedSet` with
        items common to all sets. The items appear in the same order as in the
        first set.

        Args:
            *others: Any number of `OrderedSet`. The other sets to be
                intersected.

        Returns:
            A new instance of `OrderedSet` with the items common to all
            supplied sets.

        """

        variables = []
        for variable in self:
            for other in others:
                if variable not in other:
                    break
            else:
                variables.append(variable)

        return OrderedSet(variables)

    def __eq__(self, other):
        return set(self) == set(other)

    def __ge__(self, other):
        return set(self) >= set(other)

    def __gt__(self, other):
        return set(self) > set(other)

    def __le__(self, other):
        return set(self) <= set(other)

    def __lt__(self, other):
        return set(self) < set(other)

    def __or__(self, other):
        """Union of `OrderedSet`s"""

        # We do not use the set __or__ to preserve order.
        iterable = self + other
        unique = sorted(set(iterable), key=iterable.index)

        return OrderedSet(unique)

    def __ne__(self, other):
        return set(self) != set(other)

    def __sub__(self, item):
        """Subtraction of an item from an `OrderedSet`.

        Args:
            item: An `object`. The item is removed from the set.

        Returns:
            A new `OrderedSet` with the item removed.

        Raises:
            ValueError: If the item is not in the set.

        """

        # If the item is not in the domain, it cannot be removed.
        if item not in self:
            raise ValueError(
                "The item {} is not an item or the set {}."
                .format(item, self))

        return OrderedSet([v for v in self if v != item])


class DiscreteRandomVariable(object):
    def __init__(self, symbol: str, domain: Sequence[object]=None):

        """Represents a discrete random variable in a Bayesian network.

        A `DiscreteRandomVariable` associates a set of possible outcomes
        to a symbol.

        Parameters:
            symbol: The symbol associated with the variable.
            domain: The possible outcomes of the variable. Must not contain
                duplicates.

        Raises:
            ValueError: If the domain contains duplicates.

        Examples:
            A variable representing a coin toss might be created using where 0
            and 1 represent head and tails, respectively.

            >>> coin = DiscreteRandomVariable('coin', (0, 1))
            >>> coin
            coin:(0, 1)

        """

        if domain is None:
            domain = (0, 1)

        if len(set(domain)) != len(domain):
            raise ValueError('The domain contains duplicate outcomes.')

        self._symbol = symbol
        self._domain = tuple(domain)

    @property
    def domain(self) -> Tuple:
        """The possible outcomes of the variable."""
        return self._domain

    @property
    def symbol(self) -> str:
        """The symbol associated with the variable."""
        return self._symbol

    def __len__(self) -> int:
        """The number of possible outcomes of the variable."""
        return len(self._domain)

    def __repr__(self) -> str:
        """Unambiguous string representation of a variable."""
        return '{}:{}'.format(self.symbol, self.domain)
