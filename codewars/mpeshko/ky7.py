"""Auto-formatted with proper docstrings and variable renaming."""
import math

def new_avg(arr, newavg):
    """Calculate the required donation to reach the desired average.

    Args:
        arr (list of float): Existing donations.
        newavg (float): Target average after next donation.

    Returns:
        int: The minimum donation required.

    Raises:
        ValueError: If the computed donation is not positive.
    """
    total = newavg * (len(arr) + 1)
    donation = int(math.ceil(total - sum(arr)))
    if donation <= 0:
        raise ValueError("Expected donation must be more than 0.")
    return donation

def series_sum(number):
    """Return the sum of the series 1 + 1/4 + 1/7 + ... up to n terms, rounded to 2 decimals.

    Args:
        number (int): Number of terms in the series.

    Returns:
        str: Sum as string with 2 decimal places.
    """
    if number == 0:
        return "0.00"
    total = 0.0
    for i in range(number):
        total += 1.0 / (1 + 3 * i)
    return "{0:.2f}".format(total)
