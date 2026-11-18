def total_cents(lines):
    return sum(price_cents for price_cents, _quantity in lines)
