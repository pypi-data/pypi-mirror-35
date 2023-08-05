import operator
from functools import reduce
from typing import Iterable, Sequence

import numpy as np

from bayesnet import DiscreteRandomVariable
from bayesnet.core import AbstractProbabilityMassFunction
from bayesnet.core import OrderedSet


class ProbabilityMassFunction(AbstractProbabilityMassFunction):

    def __init__(self,
                 variables: Sequence[DiscreteRandomVariable],
                 probabilities: Iterable[float] = None,
                 normalization: float = None):
        """Create a new probability mass function."""

        super().__init__(variables)

        # The default is to use the same probability for all outcomes.
        if probabilities is None:
            probabilities = np.full((self.size,), 1 / self.size,
                                    dtype=np.float64)
        else:
            probabilities = np.array(probabilities, dtype=np.float64)

        # The number of probabilities must match the number of outcomes.
        if self.size != probabilities.size:
            raise ValueError('The number of probabilities does not match '
                             'the number of possible outcomes ({} != {}).'
                             .format(self.size, probabilities.size))

        # By default, the table is normalized to 1.
        if normalization is None:

            normalization = probabilities.sum()
            if normalization == 0:
                raise ValueError('Cannot create a PMF with all 0 '
                                 'probabilities.')
            probabilities /= normalization

        else:
            if normalization == 0:
                raise ValueError('The normalization coefficient cannot be 0.')
            if np.abs(1 - probabilities.sum()) > 1e-8:
                raise ValueError('To supply a normalization coefficient, '
                                 'the probabilities must be normalized.')

        self._probabilities = probabilities
        self._normalization = normalization

    @property
    def probabilities(self) -> np.ndarray:
        return self._probabilities.copy()

    @probabilities.setter
    def probabilities(self, probabilities):
        self._probabilities = probabilities

    @property
    def normalization(self) -> float:
        """Get the normalization coefficient of the PMF."""
        return self._normalization

    @normalization.setter
    def normalization(self, normalization: float):
        """Set the normalization coefficient of the PMF."""
        self._normalization = normalization

    @property
    def unnormalized(self) -> np.ndarray:
        """The unnormalized probabilities of the PMF."""
        return self._probabilities * self._normalization

    def __add__(self, other: DiscreteRandomVariable) \
            -> 'ProbabilityMassFunction':
        """Syntactic sugar for append"""
        return self.append(other)

    def __eq__(self, other: 'ProbabilityMassFunction'):
        """Indicates if two PMFs are equal.

        Two PMFs are equal if they have the same variables (but not
        necessarily in the same order) and (almost) the same probabilities.

        """

        if self._variables != other._variables:
            return False

        # Reorder the variables so the order matches.
        other = other.reorder(self.variables)
        if not np.all(np.isclose(self.probabilities, other.probabilities)):
            return False

        return True

    def __getitem__(self, item) -> float:
        """Get the probabilities by index."""
        return self._probabilities.__getitem__(item)

    def __mul__(self, other: 'ProbabilityMassFunction') \
            -> 'ProbabilityMassFunction':
        """Product between two probability mass functions.

        The result of the product between to PMFs is a new PMF whose domain
        is the union of the input domains and with the probabilities
        multiplied accordingly.

        Args:
            other: The PMF of the right side of the product.

        Example:


            >>> from bayesnet import DiscreteRandomVariable
            >>> from bayesnet import ProbabilityMassFunction
            >>> a = DiscreteRandomVariable('a')
            >>> b = DiscreteRandomVariable('b')
            >>> c = DiscreteRandomVariable('c')
            >>> left = ProbabilityMassFunction([a, b], [0.1, 0.2, 0.3, 0.4])
            >>> right = ProbabilityMassFunction([b, c], [0.4, 0.3, 0.2, 0.1])
            >>> result = left * right
            >>> result.variables
            (a:(0, 1), b:(0, 1), c:(0, 1))

            >>> result.unnormalized
            array([ 0.04,  0.03,  0.04,  0.02,  0.12,  0.09,  0.08,  0.04])

        """

        # The variables of the result is the union of the variables of the
        # input.
        variables = self._variables | other._variables

        # Expand the two tables to contain all variables of the result.
        left = self
        right = other
        for variable in variables:
            if variable not in left:
                left = left.prepend(variable)
            if variable not in right:
                right = right.prepend(variable)

        # Reorder the inputs to match the output order.
        left = left.reorder(variables)
        right = right.reorder(variables)

        # Compute the element wise product of probabilities.
        probabilities = left.probabilities * right.probabilities
        normalization = probabilities.sum()
        probabilities /= normalization
        normalization *= left.normalization * right.normalization

        return ProbabilityMassFunction(variables, probabilities,
                                       normalization=normalization)

    def __radd__(self, other: DiscreteRandomVariable) \
            -> 'ProbabilityMassFunction':
        """Syntactic sugar for prepend"""
        return self.prepend(other)

    def __sub__(self, variable: 'DiscreteRandomVariable') \
            -> 'ProbabilityMassFunction':
        """Marginalizes a variable from a PMF.

        Marginalizes a variable from a PMF by summing it out. The result is
        a new PMF which does not depend on the variable.

        Args:
            variable: The variable to marginalize.

        Returns:
            A new PMF with no dependency on variable.

        Raises:
            ValueError: If the variable is not in the PMF.

        Example:

            >>> from bayesnet import DiscreteRandomVariable
            >>> from bayesnet.pmf import ProbabilityMassFunction
            >>> a = DiscreteRandomVariable('a')
            >>> b = DiscreteRandomVariable('b')
            >>> pmf = ProbabilityMassFunction([a, b])
            >>> marginal = pmf - b
            >>> marginal.variables
            (a:(0, 1),)

            >>> marginal.probabilities
            array([ 0.5,  0.5])

        """

        # The variable must be in the PMF.
        if variable not in self:
            raise ValueError('The variable is not in the PMF.')

        index = self.variables.index(variable)
        variables = self._variables - variable

        # Reshape the probabilities and sum out the variable.
        shape = tuple(len(v) for v in self.variables)
        probabilities = np.sum(self.probabilities.reshape(shape), axis=index)

        return ProbabilityMassFunction(variables, probabilities.ravel(),
                                       normalization=self.normalization)

    def append(self,
               variable: DiscreteRandomVariable) \
            -> 'ProbabilityMassFunction':
        """Appends a variable to the PMF and expands the probabilities.

        Adds the `variable` to the end of the set of variables contained in
        the table and expands its probabilities space by duplication. This
        generates a new PMF whose probabilities are independent of the new
        variable.

        :param variable: The variable to prepend to the PMF.

        :raises ValueError: If the variable is already in the table.

        """

        # If the variable is already part of the table, there is nothing to do.
        if variable in self:
            raise ValueError('The variable is already in the PMF.')

        variables = list(self.variables) + [variable]
        probabilities = np.repeat(self.probabilities, (len(variable),))
        probabilities /= len(variable)
        normalization = len(variable) * self.normalization

        return ProbabilityMassFunction(variables, probabilities,
                                       normalization=normalization)

    def prepend(self,
                variable: DiscreteRandomVariable) \
            -> 'ProbabilityMassFunction':
        """Prepends a variable to the PMF and expands the probabilities.

        Adds the variable to the front of the set of variables contained in
        the table and expands its probabilities space by duplication. This
        generates a new PMF whose probabilities are independent of the new
        variable.

        Args:
            variable: The variable to prepend to the PMF.

        Returns:
            A new PMF with the prepended variable.

        Raises:
            ValueError: If the variable is already in the table.

        """

        # If the variable is already part of the table, there is nothing to do.
        if variable in self:
            raise ValueError('The variable is already in the PMF.')

        variables = [variable] + list(self.variables)
        probabilities = np.tile(self.probabilities, (len(variable),))
        probabilities /= len(variable)
        normalization = len(variable) * self.normalization

        result = ProbabilityMassFunction(variables, probabilities,
                                         normalization=normalization)

        return result

    def reorder(self,
                variables: Sequence[DiscreteRandomVariable]) \
            -> 'ProbabilityMassFunction':
        """Reorders the variables of a PMF.

        Generates a new PMF by reordering the variables and the
        probabilities accordingly.

        Args:
            variables: An iterable of `bn.Variables`. The new order of the
                variables for the PMF.

        Returns:
            A new JointProbabilityMassFunction with its variables ordered
                according to `variables`.

        Raises:
            ValueError: If the supplied variables do not match those of the
                PMF.

        Example:

            >>> from bayesnet import DiscreteRandomVariable
            >>> from bayesnet.pmf import ProbabilityMassFunction
            >>> variables = [DiscreteRandomVariable('a'),
            ...              DiscreteRandomVariable('b')]
            >>> probabilities = [0.1, 0.2, 0.3, 0.4]
            >>> pmf = ProbabilityMassFunction(variables, probabilities)
            >>> pmf.variables
            (a:(0, 1), b:(0, 1))

            >>> pmf.probabilities
            array([ 0.1,  0.2,  0.3,  0.4])

            >>> reordered = pmf.reorder(variables[::-1])
            >>> reordered.variables
            (b:(0, 1), a:(0, 1))

            >>> reordered.probabilities
            array([ 0.1,  0.3,  0.2,  0.4])

        """

        if self._variables != variables:
            raise ValueError('The supplied variables do not match those of '
                             'the PMF.')

        # Find permutation that must be applied to the variables.
        order = [self.variables.index(v) for v in variables]

        # Reorder the probabilities accordingly.
        shape = tuple(len(v) for v in self.variables)
        probabilities = self._probabilities.reshape(shape).transpose(order)

        return ProbabilityMassFunction(variables, probabilities.ravel(),
                                       normalization=self.normalization)


def map(subdomain: OrderedSet, domain: OrderedSet):
    """Returns a map between two domains"""

    augmented_subdomain = subdomain | domain

    nb_states = tuple(len(v) for v in augmented_subdomain)
    zipped = list(zip(nb_states, augmented_subdomain))
    new_shape = tuple(s if v in subdomain else 1 for s, v in zipped)
    reps = tuple(1 if v in subdomain else s for s, v in zipped)

    size = reduce(operator.mul, (len(v) for v in subdomain))
    subindices = np.tile(np.arange(size).reshape(new_shape), reps)
    new_order = tuple(augmented_subdomain.index(v) for v in domain)

    return subindices.transpose(new_order).ravel()


class ProbabilityMassFunctionMarginal(ProbabilityMassFunction):

    def __init__(self,
                 pmf: ProbabilityMassFunction,
                 variable: DiscreteRandomVariable):
        """Marginal of a PMF."""

        # The variable must be in the PMF.
        if variable not in pmf:
            raise ValueError('The variable is not in the PMF.')

        variables = pmf.variables - variable
        super().__init__(variables)

        self._variable = variable
        self._pmf = pmf
        self._index = pmf.variables.index(variable)

        # Compute the probabilities.
        self.update()

    def __recur__(self):
        """Returns the PMF used to compute the marginal."""
        return self._pmf,

    def update(self):

        # Reshape the probabilities and sum out the variable.
        shape = tuple(len(v) for v in self._pmf.variables)
        self.probabilities = np.sum(self._pmf.probabilities.reshape(shape),
                                    axis=self._index).ravel()
        self.normalization = self._pmf.normalization


class ProbabilityMassFunctionProduct(ProbabilityMassFunction):

    def __init__(self, left, right, max_nb_variables=25):
        """A table that is the result of the product of two tables"""

        domain = left.variables | right.variables

        # Verify that the domain is not immense.
        if len(domain) >= max_nb_variables:
            raise ValueError('The resulting table has more than 65k states.')

        super().__init__(domain)

        self.left = left
        self.right = right

        self._left_map = map(left.variables, domain)
        self._right_map = map(right.variables, domain)

        self.update()

    def __recur__(self):
        """Returns the PMFs used to compute the product."""
        return self.left, self.right

    def update(self):
        """Updates the result table of the product"""

        probabilities = \
            self.left.probabilities[self._left_map] * \
            self.right.probabilities[self._right_map]

        normalization = probabilities.sum()
        probabilities /= normalization
        normalization *= self.left.normalization * self.right.normalization

        self.probabilities = probabilities
        self.normalization = normalization
