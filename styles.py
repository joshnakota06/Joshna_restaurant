"""All the custom CSS (colors + animations) lives here to keep app.py tidy."""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;700;800&family=Nunito:wght@400;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #fff7e6 0%, #ffe9f0 45%, #e8f4ff 100%);
}

/* ---------- Animated hero banner ---------- */
.hero {
    position: relative;
    overflow: hidden;
    text-align: center;
    padding: 28px 16px;
    border-radius: 24px;
    color: #fff;
    background: linear-gradient(120deg, #ff6b6b, #ff9a3c, #ff5fa2, #7c5cff);
    background-size: 300% 300%;
    animation: gradientShift 10s ease infinite;
    box-shadow: 0 12px 30px rgba(255, 107, 107, 0.35);
}
.hero h1 {
    font-family: 'Baloo 2', cursive;
    font-weight: 800;
    font-size: clamp(1.6rem, 5vw, 2.6rem);
    margin: 0;
    color: #fff;
}
.hero p { margin: 6px 0 0; font-size: 1.05rem; opacity: .95; }
.float-emoji {
    position: absolute;
    font-size: 2rem;
    animation: floaty 4s ease-in-out infinite;
    opacity: .85;
}
.float-emoji.e1 { left: 6%;  top: 18%; animation-delay: 0s; }
.float-emoji.e2 { right: 7%; top: 14%; animation-delay: 1s; }
.float-emoji.e3 { left: 16%; bottom: 10%; animation-delay: 2s; }
.float-emoji.e4 { right: 17%; bottom: 8%; animation-delay: 3s; }

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
@keyframes floaty {
    0%, 100% { transform: translateY(0) rotate(-6deg); }
    50% { transform: translateY(-12px) rotate(6deg); }
}

/* ---------- Cart strip ---------- */
.cart-strip {
    display: flex; gap: 12px; flex-wrap: wrap;
    margin: 18px 0 8px;
}
.cart-pill {
    flex: 1 1 140px;
    padding: 12px 16px;
    border-radius: 16px;
    background: #fff;
    border-left: 6px solid #ff6b6b;
    box-shadow: 0 6px 16px rgba(0,0,0,.07);
    transition: transform .2s ease;
}
.cart-pill:hover { transform: translateY(-3px); }
.cart-pill.green { border-color: #2ecc71; }
.cart-pill.purple { border-color: #7c5cff; }
.cart-pill small { color: #7a7a8c; font-weight: 700; }
.cart-pill b { display: block; font-family: 'Baloo 2', cursive; font-size: 1.5rem; color: #2d2a4a; }

/* ---------- Menu rows ---------- */
.menu-row {
    display: flex; align-items: center; gap: 10px;
    padding: 8px 12px;
    border-radius: 14px;
    background: #ffffffcc;
    transition: transform .2s ease, box-shadow .2s ease, background .2s ease;
}
.menu-row:hover {
    transform: translateX(4px);
    background: #fff;
    box-shadow: 0 6px 16px rgba(255, 107, 107, .18);
}
.menu-emoji { font-size: 1.8rem; }
.menu-name { font-weight: 700; color: #2d2a4a; line-height: 1.1; }
.menu-price { color: #ff6b6b; font-weight: 800; }

/* ---------- Buttons ---------- */
div.stButton > button, div.stDownloadButton > button {
    border: none;
    border-radius: 14px;
    padding: 0.7rem 1rem;
    font-weight: 800;
    color: #fff;
    background: linear-gradient(90deg, #ff6b6b, #ff9a3c);
    box-shadow: 0 8px 18px rgba(255, 107, 107, .35);
    transition: transform .15s ease, box-shadow .15s ease;
}
div.stButton > button:hover, div.stDownloadButton > button:hover {
    transform: translateY(-2px) scale(1.02);
    color: #fff;
    box-shadow: 0 12px 24px rgba(255, 107, 107, .45);
}
div.stButton > button:active { transform: scale(.97); }

/* ---------- Final bill ---------- */
.bill {
    max-width: 560px;
    margin: 18px auto;
    padding: 24px 22px;
    border-radius: 20px;
    background: #fffdf7;
    border: 3px dashed #ff9a3c;
    box-shadow: 0 16px 36px rgba(124, 92, 255, .18);
    animation: slideIn .7s cubic-bezier(.2,.9,.3,1.2);
    color: #2d2a4a;
}
@keyframes slideIn {
    from { opacity: 0; transform: translateY(40px) scale(.96); }
    to   { opacity: 1; transform: translateY(0) scale(1); }
}
.bill h2 {
    font-family: 'Baloo 2', cursive; text-align: center; margin: 0;
    color: #ff5fa2;
}
.bill .sub { text-align: center; color: #7a7a8c; margin-bottom: 12px; font-size: .9rem; }
.bill table { width: 100%; border-collapse: collapse; margin: 10px 0; }
.bill th {
    text-align: left; padding: 8px 6px; color: #fff;
    background: linear-gradient(90deg, #7c5cff, #ff5fa2);
    font-size: .85rem;
}
.bill th:first-child { border-radius: 10px 0 0 10px; }
.bill th:last-child { border-radius: 0 10px 10px 0; }
.bill td { padding: 8px 6px; border-bottom: 1px dotted #e3d9c8; font-size: .95rem; }
.bill .num { text-align: right; white-space: nowrap; }
.bill .row { display: flex; justify-content: space-between; padding: 4px 6px; }
.bill .discount { color: #1ea65b; font-weight: 700; }
.bill .grand {
    display: flex; justify-content: space-between; align-items: center;
    margin-top: 12px; padding: 14px 16px; border-radius: 16px;
    color: #fff; font-family: 'Baloo 2', cursive; font-size: 1.5rem; font-weight: 800;
    background: linear-gradient(90deg, #2ecc71, #1abc9c);
    animation: pulse 2s ease-in-out infinite;
}
@keyframes pulse {
    0%, 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(46, 204, 113, .5); }
    50% { transform: scale(1.02); box-shadow: 0 0 0 12px rgba(46, 204, 113, 0); }
}
.bill .thanks { text-align: center; margin-top: 14px; font-weight: 700; color: #7c5cff; }

/* ---------- Mobile ---------- */
@media (max-width: 640px) {
    .float-emoji { font-size: 1.4rem; }
    .bill { padding: 18px 12px; }
}

/* Respect people who prefer less motion */
@media (prefers-reduced-motion: reduce) {
    * { animation: none !important; transition: none !important; }
}
</style>
"""
