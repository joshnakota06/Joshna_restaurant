# 🍽️ Joshna Restaurant Bill Generator

A colorful, animated, beginner-friendly restaurant billing app built with **Python + Streamlit**. No database is used.

## Features
- Menu split into tabs (Starters, Main Course, Biryani, Breads, Desserts, Drinks)
- Pick quantities, see a live cart summary (items, dishes, subtotal)
- Item-wise cost, discount (slider or coupon), GST (CGST + SGST), optional service charge, round-off
- Animated final bill with grand total, balloons, and a downloadable `.txt` bill
- Works on desktop and mobile (open the sidebar arrow on mobile for bill settings)

Coupons: `JOSHNA10` (10% off) and `FOODIE20` (20% off on orders of ₹800+).

## Project structure
```
Joshna_Restaurant_Bill_Generator/
├── app.py              # Streamlit user interface
├── bill_logic.py       # Calculations (no Streamlit, easy to test)
├── menu_data.py        # Menu, prices and coupons
├── styles.py           # Colors and animations (CSS)
├── requirements.txt
├── .streamlit/config.toml
└── tests/test_bill_logic.py
```

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Run the tests
```bash
pip install pytest
pytest
```

## Deploy on Streamlit Community Cloud
1. Create a new GitHub repository and push this folder to it:
   ```bash
   git init
   git add .
   git commit -m "Joshna Restaurant Bill Generator"
   git branch -M main
   git remote add origin https://github.com/<your-username>/joshna-restaurant-bill-generator.git
   git push -u origin main
   ```
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **Create app**, choose your repository, branch `main`, and main file `app.py`.
4. Click **Deploy**, then open the link on your phone and laptop to test.
