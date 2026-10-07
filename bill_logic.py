"""Pure calculation functions (no Streamlit here, so they are easy to test)."""

from menu_data import COUPONS, MENU, SERVICE_CHARGE_PERCENT


def get_price_lookup():
    """Return {item name: price} for every item on the menu."""
    return {name: price for items in MENU.values() for name, (_, price) in items.items()}


def get_emoji_lookup():
    """Return {item name: emoji} for every item on the menu."""
    return {name: emoji for items in MENU.values() for name, (emoji, _) in items.items()}


def build_order(quantities):
    """Turn {item: quantity} into a list of order lines (only items with qty > 0)."""
    prices = get_price_lookup()
    emojis = get_emoji_lookup()
    order = []
    for name, qty in quantities.items():
        qty = int(qty or 0)
        if qty > 0 and name in prices:
            order.append(
                {
                    "name": name,
                    "emoji": emojis[name],
                    "qty": qty,
                    "price": prices[name],
                    "total": prices[name] * qty,
                }
            )
    return order


def check_coupon(code, subtotal):
    """Check a coupon. Returns (discount_percent, message, is_valid)."""
    code = (code or "").strip().upper()
    if not code:
        return 0, "", False
    if code not in COUPONS:
        return 0, "That coupon code is not valid.", False
    percent, minimum = COUPONS[code]
    if subtotal < minimum:
        return 0, f"{code} needs an order of at least {minimum}.", False
    return percent, f"{code} applied: {percent}% off!", True


def calculate_bill(order, gst_percent=5.0, manual_discount=0.0, coupon_percent=0.0,
                   add_service_charge=False):
    """Calculate every number on the bill.

    The bigger of the manual discount and the coupon discount is used
    (discounts are not stacked).
    """
    subtotal = sum(line["total"] for line in order)
    discount_percent = max(manual_discount, coupon_percent)
    discount = round(subtotal * discount_percent / 100, 2)
    taxable = subtotal - discount
    gst = round(taxable * gst_percent / 100, 2)
    service = round(taxable * SERVICE_CHARGE_PERCENT / 100, 2) if add_service_charge else 0.0
    exact_total = taxable + gst + service
    grand_total = round(exact_total)
    round_off = round(grand_total - exact_total, 2)
    return {
        "subtotal": subtotal,
        "discount_percent": discount_percent,
        "discount": discount,
        "taxable": taxable,
        "gst_percent": gst_percent,
        "cgst": round(gst / 2, 2),
        "sgst": round(gst / 2, 2),
        "gst": gst,
        "service": service,
        "round_off": round_off,
        "grand_total": grand_total,
    }
