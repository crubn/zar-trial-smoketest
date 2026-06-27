"""Tiny order-pricing helpers used to smoke-test ZAR's doc-drift detection.

The README documents these functions; code and docs start in sync.
"""


def apply_discount(price, percent):
    """Reduce ``price`` by ``percent`` percent and return the new price.

    Args:
        price: The original price as a number.
        percent: Discount percentage in the range 0-100.

    Returns:
        The discounted price as a float.
    """
    return price * (1 - percent / 100)


def format_price(amount, currency="USD"):
    """Format ``amount`` as a human-readable price string.

    Args:
        amount: The numeric amount to format.
        currency: ISO currency code, defaults to ``"USD"``.

    Returns:
        A string like ``"40.00 USD"``.
    """
    return f"{amount:.2f} {currency}"


def order_total(items):
    """Sum the prices in ``items`` (a list of numbers) into an order total.

    Args:
        items: A list of item prices.

    Returns:
        The summed total as a number.
    """
    return sum(items)
