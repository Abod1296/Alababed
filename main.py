import streamlit as st

st.set_page_config(page_title="متجر العبابيد للتقسيط", layout="centered")

st.markdown(
    """
    <style>
    .main-title { font-size: 26px; color: black; text-align: center; }
    .brand { font-size: 38px; color: orange; font-family: 'Cairo', sans-serif; font-weight: bold; text-align: center; }
    .tagline { font-size: 18px; color: #555; text-align: center; margin-bottom: 20px; }
    .result-box { background-color: #FFA500; padding: 15px; border-radius: 8px; color: white; direction: rtl; }
    .footer { text-align: center; margin-top: 20px; font-weight: bold; color: #FF6600; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="main-title">مرحباً بك في</p>', unsafe_allow_html=True)
st.markdown('<p class="brand">العبــابيد</p>', unsafe_allow_html=True)
st.markdown('<p class="tagline">هدفنا ثقتكم</p>', unsafe_allow_html=True)

# إعداد الجلسة
if "category" not in st.session_state: st.session_state["category"] = ""
if "product_name" not in st.session_state: st.session_state["product_name"] = ""
if "cash_price" not in st.session_state: st.session_state["cash_price"] = 0.0

# إدخال المستخدم
st.session_state["category"] = st.selectbox("اختر تصنيف المنتج", ["أجهزة محمولة", "كهربائيات", "مواد بناء", "أخرى"], index=0, key="category")
st.session_state["product_name"] = st.text_input("اسم المنتج", key="product_name")
st.session_state["cash_price"] = st.number_input("أدخل سعر الكاش (بالدولار)", min_value=0.0, step=0.5, format="%.2f", key="cash_price")

# حساب الأقساط
if st.button("احسب الأقساط"):
    cash_price = st.session_state["cash_price"]
    if cash_price > 0 and st.session_state["product_name"].strip() != "":
        increase = 0.30
        new_price = int(cash_price * (1 + increase))
        down_payment = int(new_price / 3.5)  # تقريباً بين الثلث والربع
        monthly_installment = int((new_price - down_payment) / 5)

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown(f"""
        <b>اسم المنتج:</b> {st.session_state["product_name"]}<br>
        <b>التصنيف:</b> {st.session_state["category"]}<br>
        <b>السعر كاش:</b> ${cash_price:.2f}<br>
        <b>السعر بعد الزيادة (30%):</b> ${new_price}<br>
        <b>الدفعة الأولى:</b> ${down_payment}<br>
        <b>عدد الأقساط:</b> 5 دفعات × ${monthly_installment}
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# زر إعادة تعيين الحقول
if st.button("إعادة تعيين الحقول"):
    st.session_state["category"] = ""
    st.session_state["product_name"] = ""
    st.session_state["cash_price"] = 0.0
    st.experimental_set_query_params(reset="1")

# ملصق تسويقي
st.markdown('<div class="footer">أقساطنا راحتكم</div>', unsafe_allow_html=True)
