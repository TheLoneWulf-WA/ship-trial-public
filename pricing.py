"""Small pricing helpers for an order."""


def subtotal(items):
    """Sum of quantity * unit_price over (quantity, unit_price) pairs."""
    return sum(quantity * unit_price for quantity, unit_price in items)


def apply_discount(total, percent):
    """Take percent off total. percent must be between 0 and 100."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(total * (100 - percent) / 100, 2)
