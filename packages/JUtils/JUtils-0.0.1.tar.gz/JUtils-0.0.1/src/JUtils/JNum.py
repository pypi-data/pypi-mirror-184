#Functions for handling numbers

def sgn(n: float) -> int:
    """Returns the sign of a number.

    Parameters:
        n: An int/float number.

    Returns:
        An int representing the sign of 'n'. 1 if 'n' is positive, -1 if 'n'
        is negative, and 0 if 'n' is zero.
    """
    return int(n/abs(n))

def contain(n: float, limDown: float, limUp: float) -> float:
    """Clamps a number within a given range.

    Parameters:
        n (float): The number to be clamped.
        limDown (float): The lower bound of the range.
        limUp (float): The upper bound of the range.

    Returns:
        'n' if it is within the range, or the nearest bound if 'n' is outside
        the range.
    """
    return max(limDown, min(n, limUp))