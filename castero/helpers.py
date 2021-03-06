import re


def third(n) -> int:
    """Calculates one-third of a given value.

    Args:
        n: the integer to calculate one-third of

    Returns:
        int: one-third of n, rounded down
    """
    return int(n / 3)


def median(arr):
    """Determines the median of a list of numbers.

    Args:
        arr: a list of ints and/or floats of which to determine the median

    Returns:
        int or float: the median value in arr
    """
    if len(arr) == 0:
        return None

    arr_sorted = sorted(arr)
    midpoint = int(len(arr) / 2)

    if len(arr) % 2 == 0:
        # even number of elements; get the average of the middle two
        result = (arr_sorted[midpoint - 1] + arr_sorted[midpoint]) / 2
    else:
        result = arr_sorted[midpoint]
    return result


def sanitize_path(path) -> str:
    """Replaces any characters in path that the file system may not support.

    This method replaces any non-alphanumeric characters with an underscore,
    with the exception of hyphens.

    Args:
        path: the original path

    Returns:
        str: the given path with potentially unsafe characters replaced
    """
    # adapted from https://stackoverflow.com/a/13593932
    path = re.sub('[^\w\-]', '_', path)
    return path
