"""Joshna Restaurant Bill Generator - a beginner-friendly Streamlit app.

Run it with:  streamlit run app.py
"""

import html
from datetime import datetime

import streamlit as st

from bill_logic import build_order, calculate_bill, check_coupon, get_price_lookup
from menu_data import (APP_NAME, COUPONS, CURRENCY, MENU, RESTAURANT_NAME,
                       SERVICE_CHARGE_PERCENT)
from styles import CSS

st.set_page_config(page_title=APP_NAME, page_icon="🍔", layout="centered")
st.markdown(CSS, unsafe_allow_html=True)


def money(amount):
    """Format a number as money, e.g. ₹1,234.50"""
    return f"{CURRENCY}{amount:,.2f}"


def qty_key(item_name):
    return f"qty_{item_name}"


def clear_order():
    """Reset every quantity to 0 (used by the 'Clear order' button)."""
    for name in get_price_lookup():
        st.session_state[qty_key(name)] = 0
    st.session_state["show_bill"] = False


def bill_as_text(order, bill, customer, table, bill_no, when):
    """Plain-text version of the bill for the download button."""
    lines = [
        APP_NAME.upper(),
        RESTAURANT_NAME,
        "-" * 44,
        f"Bill No : {bill_no}",
        f"Date    : {when}",
        f"Customer: {customer}",
        f"Table   : {table}",
        "-" * 44,
    ]
    for line in order:
        lines.append(f"{line['name'][:20]:<20} {line['qty']:>2} x {line['price']:>5} = {line['total']:>7}")
    lines.append("-" * 44)
    lines.append(f"{'Subtotal':<30}{bill['subtotal']:>14.2f}")
    if bill["discount"]:
        lines.append(f"{'Discount (' + str(bill['discount_percent']) + '%)':<30}{-bill['discount']:>14.2f}")
    lines.append(f"{'CGST':<30}{bill['cgst']:>14.2f}")
    lines.append(f"{'SGST':<30}{bill['sgst']:>14.2f}")
    if bill["service"]:
        lines.append(f"{'Service charge':<30}{bill['service']:>14.2f}")
    lines.append(f"{'Round off':<30}{bill['round_off']:>14.2f}")
    lines.append("=" * 44)
    lines.append(f"{'GRAND TOTAL':<30}{bill['grand_total']:>14.2f}")
    lines.append("=" * 44)
    lines.append("Thank you! Please visit again.")
    return "\n".join(lines)


# ------------------------------------------------------------------ Header
st.markdown(
    f"""
<div class="hero">
  <span class="float-emoji e1">🍔</span><span class="float-emoji e2">🍕</span>
  <span class="float-emoji e3">🍟</span><span class="float-emoji e4">🥤</span>
  <h1>🍽️ {APP_NAME}</h1>
  <p>Pick your food, set the quantity, and get a beautiful bill in a click.</p>
</div>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------- Sidebar
with st.sidebar:
    st.header("🧾 Bill Settings")
    customer = st.text_input("Customer name", value="Guest")
    table = st.text_input("Table number", value="1")
    gst_percent = st.select_slider("GST %", options=[0, 5, 12, 18], value=5)
    manual_discount = st.slider("Discount %", 0, 30, 0)
    coupon_code = st.text_input("Coupon code", placeholder="Try JOSHNA10")
    add_service = st.checkbox(f"Add {SERVICE_CHARGE_PERCENT}% service charge")
    st.caption("Coupons: " + ", ".join(COUPONS))
    st.caption("If you use both, the bigger discount is applied.")

# --------------------------------------------------- Live cart (top strip)
# Widget values are already in session_state when the script runs, so we can
# show a live summary above the menu.
current_quantities = {name: st.session_state.get(qty_key(name), 0) for name in get_price_lookup()}
live_order = build_order(current_quantities)
live_items = sum(line["qty"] for line in live_order)
live_subtotal = sum(line["total"] for line in live_order)

st.markdown(
    f"""
<div class="cart-strip">
  <div class="cart-pill"><small>🛒 Items</small><b>{live_items}</b></div>
  <div class="cart-pill green"><small>🍽️ Dishes</small><b>{len(live_order)}</b></div>
  <div class="cart-pill purple"><small>💰 Subtotal</small><b>{money(live_subtotal)}</b></div>
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------------------- Menu
st.subheader("📖 Menu")
tabs = st.tabs(list(MENU.keys()))
for tab, (category, items) in zip(tabs, MENU.items()):
    with tab:
        for name, (emoji, price) in items.items():
            info_col, qty_col = st.columns([3, 2])
            with info_col:
                st.markdown(
                    f"""<div class="menu-row"><span class="menu-emoji">{emoji}</span>
                    <div><div class="menu-name">{name}</div>
                    <div class="menu-price">{money(price)}</div></div></div>""",
                    unsafe_allow_html=True,
                )
            with qty_col:
                st.number_input(
                    f"Quantity for {name}",
                    min_value=0, max_value=20, step=1,
                    key=qty_key(name), label_visibility="collapsed",
                )

# ----------------------------------------------------------------- Buttons
st.write("")
col_bill, col_clear = st.columns([3, 1])
with col_bill:
    if st.button("🧾 Generate Bill", use_container_width=True, type="primary"):
        st.session_state["show_bill"] = True
        st.session_state["bill_time"] = datetime.now()
        st.session_state["celebrate"] = True
with col_clear:
    st.button("🗑️ Clear", on_click=clear_order, use_container_width=True)

# -------------------------------------------------------------------- Bill
if st.session_state.get("show_bill"):
    order = build_order({name: st.session_state.get(qty_key(name), 0) for name in get_price_lookup()})

    if not order:
        st.warning("Your order is empty. Add at least one item from the menu above. 🍽️")
    else:
        subtotal = sum(line["total"] for line in order)
        coupon_percent, coupon_msg, coupon_ok = check_coupon(coupon_code, subtotal)
        if coupon_msg:
            (st.success if coupon_ok else st.error)(coupon_msg)

        bill = calculate_bill(order, gst_percent, manual_discount, coupon_percent, add_service)
        when_dt = st.session_state.get("bill_time", datetime.now())
        when = when_dt.strftime("%d %b %Y, %I:%M %p")
        bill_no = "JK" + when_dt.strftime("%y%m%d%H%M%S")
        safe_customer = html.escape(customer.strip() or "Guest")
        safe_table = html.escape(table.strip() or "-")

        rows = "".join(
            f"<tr><td>{l['emoji']} {l['name']}</td><td class='num'>{l['qty']}</td>"
            f"<td class='num'>{money(l['price'])}</td><td class='num'>{money(l['total'])}</td></tr>"
            for l in order
        )
        extra = f"<div class='row'><span>Subtotal</span><span>{money(bill['subtotal'])}</span></div>"
        if bill["discount"]:
            extra += (f"<div class='row discount'><span>Discount ({bill['discount_percent']:g}%)</span>"
                      f"<span>-{money(bill['discount'])}</span></div>")
        extra += (f"<div class='row'><span>CGST ({gst_percent / 2:g}%)</span><span>{money(bill['cgst'])}</span></div>"
                  f"<div class='row'><span>SGST ({gst_percent / 2:g}%)</span><span>{money(bill['sgst'])}</span></div>")
        if bill["service"]:
            extra += (f"<div class='row'><span>Service charge ({SERVICE_CHARGE_PERCENT}%)</span>"
                      f"<span>{money(bill['service'])}</span></div>")
        extra += f"<div class='row'><span>Round off</span><span>{money(bill['round_off'])}</span></div>"

        st.markdown(
            f"""<div class="bill">
<h2>🍽️ {RESTAURANT_NAME}</h2>
<div class="sub">Bill No: {bill_no} &nbsp;|&nbsp; {when}<br>Customer: {safe_customer} &nbsp;|&nbsp; Table: {safe_table}</div>
<table><tr><th>Item</th><th class="num">Qty</th><th class="num">Price</th><th class="num">Total</th></tr>{rows}</table>
{extra}
<div class="grand"><span>💰 Grand Total</span><span>{money(bill['grand_total'])}</span></div>
<div class="thanks">Thank you for dining with us! Please visit again 😊</div>
</div>""",
            unsafe_allow_html=True,
        )

        st.download_button(
            "⬇️ Download bill (.txt)",
            data=bill_as_text(order, bill, customer.strip() or "Guest", table.strip() or "-", bill_no, when),
            file_name=f"{bill_no}.txt",
            mime="text/plain",
            use_container_width=True,
        )

        if st.session_state.pop("celebrate", False):
            st.balloons()

st.caption(f"Made with ❤️ using Python + Streamlit · {APP_NAME}")
