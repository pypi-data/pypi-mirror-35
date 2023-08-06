import numpy


def _empirical_p_val_vectorized_left(data, values, standard_approximation=True):
    """
    """
    i = 0
    p_vals = numpy.zeros(len(values))
    for value_idx, value in enumerate(values):
        if data[i] <= value:
            while i < len(data) and data[i] <= value:
                i += 1
            i -= 1
            p_vals[value_idx] = ((i + 1 + (0, 1)[bool(standard_approximation)]) / (
                    len(data) + (0, 1)[bool(standard_approximation)]))
        else:
            p_vals[value_idx] = (0, 1)[bool(standard_approximation)] / (
                    len(data) + (0, 1)[bool(standard_approximation)])

    return p_vals


def _empirical_p_val_vectorized_right(data, values, standard_approximation=True):
    """
    """
    values = values[::-1]
    data = data[::-1]
    i = 0
    p_vals = numpy.zeros(len(values))
    for value_idx, value in enumerate(values):
        if data[i] >= value:
            while i < len(data) and data[i] >= value:
                i += 1
            i -= 1
            p_vals[value_idx] = ((i + 1 + (0, 1)[bool(standard_approximation)]) / (
                    len(data) + (0, 1)[bool(standard_approximation)]))
        else:
            p_vals[value_idx] = (0, 1)[bool(standard_approximation)] / (
                    len(data) + (0, 1)[bool(standard_approximation)])
    return p_vals[::-1]


def empirical_p_val(data, values, tail='both', standard_approximation=True, is_sorted=False):
    """
    Given an unsorted vector of observed data :param:`data`, returns the standard approximation
    (adds pseudocount of 1 to prevent 0 p-values) to the empirical p-value for :param:`value`
    using either a one-sided or two-sided significance test.

    :param:`tail` must be 'left', 'right' (for a one-sided test) or 'both' (for a two-sided test)
    """
    if tail not in ('left', 'right', 'both'):
        raise ValueError('Invalid value for parameter :tail:, {}'.format(tail))

    try:
        len(values)
    except TypeError:
        is_vector = False
        value = values
    else:
        is_vector = True

    if is_vector and not is_sorted:
        data = sorted(data)
        value_sort_idx = numpy.argsort(values)
        restore_values_sort_idx = numpy.argsort(values)
        values = values[value_sort_idx]
        del (value_sort_idx)

    if tail in ('left', 'both'):
        if is_vector:
            left_p_val = _empirical_p_val_vectorized_left(data, values, standard_approximation=standard_approximation)
        else:
            left_p_val = (numpy.sum(numpy.less_equal(data, value)) + 1) / (len(data) + 1)

    if tail in ('right', 'both'):
        if is_vector:
            right_p_val = _empirical_p_val_vectorized_right(data, values, standard_approximation=standard_approximation)
        else:
            right_p_val = (numpy.sum(numpy.greater_equal(data, value)) + 1) / (len(data) + 1)

    if tail == 'left':
        p_vals = left_p_val
    elif tail == 'right':
        p_vals = right_p_val
    else:
        p_vals = numpy.minimum(numpy.minimum(left_p_val, right_p_val) * 2, 1)

    if is_vector and not is_sorted:
        p_vals = p_vals[restore_values_sort_idx]

    return p_vals
