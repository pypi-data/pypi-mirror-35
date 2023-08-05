from .probability_combiner import ProbabilityCombiner


class FirstFeatureProbability(ProbabilityCombiner):
    def combine(self, p_values, ref_p_values=None):
        """
        Takes a list of p_values and combines them into a single p_value by choosing the p_value of the first feature.
        :param p_values: a list of p_values of features.
        :param ref_p_values: p-values of reference observations (if needed).
        :return: The combined p-value.
        """

        # assert p_values is a list
        assert type(p_values) == list

        # check that p_values is not empty
        if len(p_values) == 0:
            raise ValueError('The given list of p_values is empty')

        # check that all elements in p_values are floats
        if not all(isinstance(x, (int, float)) for x in p_values):
            raise ValueError('The elements in p_values should all be of the type \'float\'')

        p = p_values[0]

        return p
