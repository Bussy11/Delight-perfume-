import urllib.parse
import streamlit as st

# ============================================================
# DELIGH PERFUME & BEAUTY STORE
# Save this file as app.py and run:
#     pip install streamlit
#     streamlit run app.py
# ============================================================

st.set_page_config(
    page_title="Deligh Perfume & Beauty Store",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------- BUSINESS SETTINGS ---------------------------
SHOP_NAME = "Deligh Perfume & Beauty Store"
SHOP_ADDRESS = "Taiwo Road, Ganmo, Amoyo, Ilorin"
SHOP_WHATSAPP_NUMBER = "2348000000000"  # Replace with your WhatsApp number.
CURRENCY = "₦"

# Replace these sample prices, descriptions and images with your real inventory.
PERFUMES = [
    {
        "id": 1, "name": "Chanel No. 5", "brand": "Chanel",
        "category": "Women", "size": "100ml", "price": 125000,
        "description": "An elegant floral fragrance with a timeless, luxurious character.",
        "image": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=700",
        "badge": "Classic",
    },
    {
        "id": 2, "name": "Dior Sauvage", "brand": "Dior",
        "category": "Men", "size": "100ml", "price": 115000,
        "description": "A fresh, bold fragrance suitable for everyday confidence.",
        "image": "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=700",
        "badge": "Bestseller",
    },
    {
        "id": 3, "name": "Tom Ford Black Orchid", "brand": "Tom Ford",
        "category": "Unisex", "size": "50ml", "price": 95000,
        "description": "A rich, distinctive scent for memorable evenings.",
        "image": "https://images.unsplash.com/photo-1523293182086-7651a899d37f?w=700",
        "badge": "Luxury",
    },
    {
        "id": 4, "name": "Baccarat Rouge 540", "brand": "Maison Francis Kurkdjian",
        "category": "Unisex", "size": "70ml", "price": 210000,
        "description": "A refined, radiant fragrance with a sophisticated presence.",
        "image": "https://images.unsplash.com/photo-1588405748880-12d1d2a59f75?w=700",
        "badge": "Premium",
    },
    {
        "id": 5, "name": "Creed Aventus", "brand": "Creed",
        "category": "Men", "size": "100ml", "price": 230000,
        "description": "A confident, bold fragrance for people who enjoy standing out.",
        "image": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=700",
        "badge": "Premium",
    },
    {
        "id": 6, "name": "Yves Saint Laurent Libre", "brand": "YSL",
        "category": "Women", "size": "90ml", "price": 105000,
        "description": "A modern fragrance blending freshness and warm floral notes.",
        "image": "https://images.unsplash.com/photo-1563178406-4cdc2923acbc?w=700",
        "badge": "Popular",
    },
]

# --------------------------- DESIGN / CSS ---------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

    :root { --wine: #641b35; --gold: #c69b52; --cream: #fbf7f2; }
    .stApp { background: #fbf8f4; }
    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
    h1, h2, h3 { color: #351321; }
    .brand-title {
        font-family: 'Playfair Display', serif;
        color: #641b35; font-size: clamp(30px, 4vw, 48px);
        font-weight: 700; text-align: center; margin-bottom: 2px;
    }
    .brand-subtitle { text-align:center; color:#79636a; font-size:15px; }
    .hero {
        background: linear-gradient(115deg, rgba(42,13,27,.94), rgba(100,27,53,.82)),
                    url('https://images.unsplash.com/photo-1594035910387-fea47794261f?w=1600');
        background-size: cover; background-position: center;
        padding: 48px 35px; border-radius: 18px; color: white;
        margin: 18px 0 25px 0;
    }
    .hero h1 { color:white; font-family:'Playfair Display',serif; font-size:42px; }
    .hero p { color:#f7e9ed; font-size:17px; max-width:650px; }
    .eyebrow { color:#e6c58c; text-transform:uppercase; letter-spacing:3px; font-size:12px; font-weight:700; }
    .product-card {
        background:white; border:1px solid #eee3e5; border-radius:15px;
        padding:13px; margin-bottom:16px; box-shadow:0 5px 18px rgba(53,19,33,.06);
    }
    .product-name { color:#351321; font-size:17px; font-weight:700; margin:7px 0 2px; }
    .product-meta { color:#806d73; font-size:13px; }
    .product-price { color:#641b35; font-size:18px; font-weight:700; margin:8px 0; }
    .badge {
        display:inline-block; background:#f4e9dc; color:#744a24;
        padding:4px 9px; border-radius:20px; font-size:11px; font-weight:700;
    }
    .info-box {
        background:white; border:1px solid #eee3e5; border-radius:14px;
        padding:18px; min-height:100px;
    }
    .section-label { color:#641b35; font-family:'Playfair Display',serif; font-size:27px; font-weight:700; }
    .whatsapp-float {
        position:fixed; right:22px; bottom:22px; z-index:999999;
        background:#25D366; color:white!important; padding:12px 18px;
        border-radius:30px; font-weight:700; text-decoration:none!important;
        box-shadow:0 5px 18px rgba(0,0,0,.22);
    }
    .footer { text-align:center; color:#806d73; padding:25px 0 10px; font-size:13px; }
    div.stButton > button[kind="primary"] {
        background:#641b35; border:0; color:white; border-radius:9px;
    }
    div.stButton > button[kind="primary"]:hover { background:#8b3150; color:white; }
</style>
""", unsafe_allow_html=True)

# --------------------------- SESSION STATE ---------------------------
if "cart" not in st.session_state:
    st.session_state.cart = {}
if "order_message" not in st.session_state:
    st.session_state.order_message = ""

def money(amount):
    return f"{CURRENCY}{amount:,.0f}"

def whatsapp_link(message):
    encoded = urllib.parse.quote(message)
    return f"https://wa.me/{SHOP_WHATSAPP_NUMBER}?text={encoded}"

# Floating WhatsApp contact button
st.markdown(
    f'<a class="whatsapp-float" href="{whatsapp_link("Hello Deligh Perfume & Beauty Store. I would like to make an enquiry.")}" target="_blank">💬 Chat with us</a>',
    unsafe_allow_html=True,
)

# --------------------------- HEADER ---------------------------
st.markdown('<div class="brand-title">🌸 DELIGH</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="brand-subtitle">PERFUME & BEAUTY STORE · Your scent, your signature.</div>',
    unsafe_allow_html=True,
)
st.caption(f"📍 {SHOP_ADDRESS}")
st.divider()

# --------------------------- HERO ---------------------------
st.markdown("""
<div class="hero">
    <div class="eyebrow">Discover your signature scent</div>
    <h1>Make every moment unforgettable.</h1>
    <p>Explore carefully selected fragrances for every personality and occasion.
       Find a scent that tells your story.</p>
</div>
""", unsafe_allow_html=True)

# --------------------------- STORE BENEFITS ---------------------------
b1, b2, b3 = st.columns(3)
with b1:
    st.markdown('<div class="info-box">🚚 <b>Convenient ordering</b><br><small>Place your order directly through WhatsApp.</small></div>', unsafe_allow_html=True)
with b2:
    st.markdown('<div class="info-box">🌺 <b>Fragrance choices</b><br><small>Explore options for men, women and everyone.</small></div>', unsafe_allow_html=True)
with b3:
    st.markdown('<div class="info-box">🤝 <b>Personal assistance</b><br><small>Contact our team for product enquiries.</small></div>', unsafe_allow_html=True)

st.write("")
st.markdown('<div class="section-label">Explore our collection</div>', unsafe_allow_html=True)
st.write("Search the catalogue, select a category and add your favourites to your cart.")

# --------------------------- SEARCH AND FILTERS ---------------------------
filter_col1, filter_col2 = st.columns([2, 1])
with filter_col1:
    search_text = st.text_input("🔎 Search by perfume name or brand", placeholder="e.g. Dior, Chanel...")
with filter_col2:
    category = st.selectbox("Category", ["All", "Men", "Women", "Unisex"])

filtered_perfumes = [
    p for p in PERFUMES
    if (category == "All" or p["category"] == category)
    and (search_text.lower() in p["name"].lower() or search_text.lower() in p["brand"].lower())
]

# --------------------------- PRODUCT GRID ---------------------------
if not filtered_perfumes:
    st.info("No perfume matches your search. Try another name or category.")
else:
    product_cols = st.columns(3)
    for index, perfume in enumerate(filtered_perfumes):
        with product_cols[index % 3]:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            st.image(perfume["image"], use_container_width=True)
            st.markdown(f'<span class="badge">{perfume["badge"]}</span>', unsafe_allow_html=True)
            st.markdown(f'<div class="product-name">{perfume["name"]}</div>', unsafe_allow_html=True)
            st.markdown(
                f'<div class="product-meta">{perfume["brand"]} · {perfume["size"]} · {perfume["category"]}</div>',
                unsafe_allow_html=True,
            )
            st.markdown(f'<div class="product-price">{money(perfume["price"])}</div>', unsafe_allow_html=True)
            st.caption(perfume["description"])
            if st.button("＋ Add to cart", key=f"add_{perfume['id']}", type="primary", use_container_width=True):
                st.session_state.cart[perfume["id"]] = st.session_state.cart.get(perfume["id"], 0) + 1
                st.toast(f"{perfume['name']} added to your cart.", icon="🛍️")
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --------------------------- CART AND CHECKOUT ---------------------------
st.markdown('<div class="section-label">Your shopping cart</div>', unsafe_allow_html=True)
cart_col, checkout_col = st.columns([1.05, 1], gap="large")
total_amount = 0

with cart_col:
    st.subheader("🛍️ Order summary")
    if not st.session_state.cart:
        st.info("Your cart is empty. Add a fragrance from the collection above.")
    else:
        for item_id in list(st.session_state.cart.keys()):
            item = next((p for p in PERFUMES if p["id"] == item_id), None)
            if item is None:
                continue
            quantity = st.session_state.cart[item_id]
            item_total = item["price"] * quantity
            total_amount += item_total

            with st.container(border=True):
                row1, row2, row3 = st.columns([3, 1, 1])
                row1.markdown(f"**{item['name']}**")
                row1.caption(f"{item['size']} · {money(item['price'])} each")
                new_quantity = row2.number_input(
                    "Qty", min_value=1, max_value=20, value=quantity,
                    key=f"qty_{item_id}", label_visibility="collapsed"
                )
                st.session_state.cart[item_id] = int(new_quantity)
                total_amount += (int(new_quantity) - quantity) * item["price"]
                if row3.button("Remove", key=f"remove_{item_id}"):
                    del st.session_state.cart[item_id]
                    st.rerun()
                st.write(f"Item total: **{money(item['price'] * int(new_quantity))}**")
        st.markdown(f"### Total: {money(total_amount)}")
        if st.button("🗑️ Clear cart", use_container_width=True):
            st.session_state.cart = {}
            st.rerun()

with checkout_col:
    st.subheader("🚚 Delivery information")
    st.write("Complete the form below. Your order will be prepared as a WhatsApp message for confirmation.")
    with st.form("checkout_form", clear_on_submit=False):
        customer_name = st.text_input("Full name *")
        customer_phone = st.text_input("Phone number *", placeholder="e.g. 08012345678")
        customer_state = st.text_input("State")
        customer_lga = st.text_input("LGA / City")
        customer_address = st.text_area("Full delivery address *")
        customer_note = st.text_area("Additional note (optional)", placeholder="Preferred delivery time, fragrance questions, etc.")
        submit_order = st.form_submit_button("Place order on WhatsApp", type="primary", use_container_width=True)

    if submit_order:
        if not customer_name.strip() or not customer_phone.strip() or not customer_address.strip():
            st.error("Please complete your full name, phone number and delivery address.")
        elif not st.session_state.cart:
            st.warning("Your cart is empty. Add at least one perfume before placing an order.")
        else:
            order_lines = []
            fresh_total = 0
            for item_id, qty in st.session_state.cart.items():
                item = next(p for p in PERFUMES if p["id"] == item_id)
                line_total = item["price"] * qty
                fresh_total += line_total
                order_lines.append(f"• {item['name']} ({item['size']}) x {qty} = {money(line_total)}")

            message = f"""*NEW ORDER — {SHOP_NAME}*

*Customer:* {customer_name}
*Phone:* {customer_phone}
*State:* {customer_state or 'Not supplied'}
*LGA/City:* {customer_lga or 'Not supplied'}
*Delivery address:* {customer_address}

*ORDER DETAILS*
{chr(10).join(order_lines)}

*TOTAL: {money(fresh_total)}*
*Additional note:* {customer_note or 'None'}

Please confirm availability, delivery fee and payment instructions. Thank you."""
            st.session_state.order_message = message
            st.success("Your order summary is ready. Continue to WhatsApp to send it to the store.")
            st.link_button(
                "💬 Send order to Deligh on WhatsApp",
                whatsapp_link(message),
                type="primary",
                use_container_width=True,
            )

# --------------------------- ABOUT / CONTACT ---------------------------
st.divider()
about_col, contact_col = st.columns(2)
with about_col:
    st.markdown("### 🌸 About Deligh")
    st.write(
        "Deligh Perfume & Beauty Store helps customers discover fragrances "
        "for everyday use, special occasions and thoughtful gifts. Browse the "
        "catalogue and contact us to confirm product availability."
    )
with contact_col:
    st.markdown("### 📞 Contact and enquiries")
    st.write(f"**Location:** {SHOP_ADDRESS}")
    st.write("**WhatsApp:** Update the number in the app settings at the top of this file.")
    st.write("**Opening hours:** Contact us to confirm today's availability.")

st.markdown(
    f'<div class="footer">© {SHOP_NAME} · All rights reserved.<br>Designed for a smooth and simple shopping experience.</div>',
    unsafe_allow_html=True,
)
