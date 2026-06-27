# zar-trial-smoketest

A tiny pricing library used to smoke-test **ZAR**'s documentation-drift detection.
Code and docs start in sync; a later change introduces real drift on purpose.

## Usage

```python
from store import apply_discount, format_price, order_total

# Apply a 20% discount to a $50 item
price = apply_discount(50, 20)          # -> 40.0
print(format_price(price))              # -> "40.00 USD"

# Total an order
print(order_total([40.0, 12.5, 7.0]))   # -> 59.5
```

## API

- `apply_discount(price, percent)` — reduce `price` by `percent` percent.
- `format_price(amount, currency="USD")` — format a numeric amount as a price string.
- `order_total(items)` — sum a list of item prices into an order total.
