"""Menu and coupon data for the Joshna Restaurant Bill Generator.

Everything lives in plain Python dictionaries (no database needed).
Prices are in Indian Rupees (₹).
"""

APP_NAME = "Joshna Restaurant Bill Generator"
RESTAURANT_NAME = "Joshna's Kitchen"
CURRENCY = "₹"

# Category -> {item name: (emoji, price)}
MENU = {
    "🥟 Starters": {
        "Paneer Tikka": ("🧀", 220),
        "Veg Spring Rolls": ("🥟", 160),
        "Chicken 65": ("🍗", 260),
        "Gobi Manchurian": ("🥦", 180),
    },
    "🍛 Main Course": {
        "Butter Chicken": ("🍗", 320),
        "Paneer Butter Masala": ("🍛", 280),
        "Dal Tadka": ("🥣", 180),
        "Veg Fried Rice": ("🍚", 190),
    },
    "🍚 Biryani": {
        "Veg Biryani": ("🥘", 210),
        "Chicken Biryani": ("🍗", 290),
        "Egg Biryani": ("🥚", 240),
    },
    "🫓 Breads": {
        "Butter Naan": ("🫓", 50),
        "Garlic Naan": ("🧄", 60),
        "Tandoori Roti": ("🫓", 30),
    },
    "🍨 Desserts": {
        "Gulab Jamun": ("🍡", 90),
        "Chocolate Brownie": ("🍫", 140),
        "Vanilla Ice Cream": ("🍨", 100),
    },
    "🥤 Drinks": {
        "Masala Chai": ("☕", 40),
        "Fresh Lime Soda": ("🍋", 70),
        "Mango Lassi": ("🥭", 90),
        "Cold Coffee": ("🧋", 110),
    },
}

# Coupon code -> (discount percent, minimum subtotal needed)
COUPONS = {
    "JOSHNA10": (10, 0),
    "FOODIE20": (20, 800),
}

SERVICE_CHARGE_PERCENT = 5
