import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="متجر العبابيد للتقسيط", layout="centered")

# تنسيق CSS
st.markdown("""
    <style>
    .main-title { font-size: 26px; color: black; text-align: center; }
    .brand { font-size: 38px; color: orange; font-family: 'Cairo', sans-serif; font-weight: bold; text-align: center; }
    .tagline { font-size: 18px; color: #555; text-align: center; margin-bottom: 20px; }
    .result-box { background-color: #FFA500; padding: 15px; border-radius: 8px; color: white; direction: rtl; }
    .footer { text-align: center; margin-top: 20px; font-weight: bold; color: #FF6600; }
    </style>
""", unsafe_allow_html=True)

# العنوان
st.markdown('<p class="main-title">مرحباً بك في</p>', unsafe_allow_html=True)
st.markdown('<p class="brand">الرفاعي كتك</p>', unsafe_allow_html=True)
st.markdown('<p class="tagline">هدفنا ثقتكم</p>', unsafe_allow_html=True)

# مدخلات المستخدم
category = st.selectbox("اختر تصنيف المنتج", ["أجهزة محمولة", "كهربائيات", "مواد بناء", "أخرى"])
product_name = st.text_input("اسم المنتج")
cash_price = st.number_input("أدخل سعر الكاش (بالدولار)", min_value=0.0, step=0.5, format="%.2f")

# زر الحساب
if st.button("احسب الأقساط"):
    if product_name.strip() != "" and cash_price > 0:
        increase = 0.30
        new_price = int(cash_price * (1 + increase))
        down_payment = int(new_price / 3.5)
        monthly_installment = int((new_price - down_payment) / 5)

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown(f"""
        <b>اسم المنتج:</b> {product_name}<br>
        <b>التصنيف:</b> {category}<br>
        <b>السعر كاش:</b> ${cash_price:.2f}<br>
        <b>السعر بعد الزيادة (30%):</b> ${new_price}<br>
        <b>الدفعة الأولى:</b> ${down_payment}<br>
        <b>عدد الأقساط:</b> 5 دفعات × ${monthly_installment}
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("يرجى ملء جميع الحقول أولاً.")

# إعادة تعيين الحقول (بإعادة تحميل الصفحة)
if st.button("إعادة تعيين الحقول"):
    st.experimental_rerun()

# ملصق
st.markdown('<div class="footer">أقساطنا راحتكم</div>', unsafe_allow_html=True)
