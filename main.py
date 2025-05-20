import streamlit as st
import urllib.parse

# إعداد الصفحة
st.set_page_config(page_title="متجر العبابيد", layout="centered")

# العنوان والترويسة
st.markdown("<h3 style='text-align: center; color: black;'>مرحباً بك في</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: orange; font-family: Cairo;'>العبـــابيد</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>هدفنا ثقتكم</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #ff9900;'>", unsafe_allow_html=True)

# ملصق جانبي
st.sidebar.markdown("<h4 style='color: orange;'>أقساطنا راحتكم</h4>", unsafe_allow_html=True)
st.sidebar.markdown("رقم التواصل: +963943001296")

# إدخال المعلومات
st.markdown("### اختر تصنيف المنتج")
category = st.selectbox("اختر تصنيف المنتج", ["أجهزة محمولة", "كهربائيات", "مواد بناء", "أخرى"])

product_name = st.text_input("اسم المنتج")
cash_price = st.number_input("أدخل سعر الكاش (بالدولار)", min_value=0.0, step=0.5, format="%.2f")

# زر الحساب
if st.button("احسب الأقساط"):
    if cash_price > 0 and product_name:
        price_with_increase = round(cash_price * 1.3)
        down_payment = round(price_with_increase / 3)
        monthly_installment = round((price_with_increase - down_payment) / 5)

        report = f"""اسم المنتج: {product_name}
التصنيف: {category}
السعر كاش: {int(cash_price)} دولار
السعر بعد الزيادة: {price_with_increase} دولار
الدفعة الأولى: {down_payment} دولار
عدد الأقساط: 5 دفعات
قيمة كل قسط: {monthly_installment} دولار"""

        st.markdown("### تفاصيل الأقساط الشرعية:")
        st.markdown(
            f"""
            <div style='background-color:#FF9900; padding:15px; border-radius:10px; color:white; font-size:18px; line-height:1.7;'>
            <b>اسم المنتج:</b> {product_name}<br>
            <b>التصنيف:</b> {category}<br>
            <b>السعر كاش:</b> {int(cash_price)} دولار<br>
            <b>السعر بعد الزيادة:</b> {price_with_increase} دولار<br>
            <b>الدفعة الأولى:</b> {down_payment} دولار<br>
            <b>عدد الأقساط:</b> 5 دفعات<br>
            <b>قيمة كل قسط:</b> {monthly_installment} دولار
            </div>
            """,
            unsafe_allow_html=True,
        )

        # زر المشاركة على واتساب
        message = urllib.parse.quote(report)
        whatsapp_link = f"https://wa.me/?text={message}"
        st.markdown(f"<br><a href='{whatsapp_link}' target='_blank'><button style='background-color:#25D366; color:white; padding:10px 20px; border:none; border-radius:5px; font-size:16px;'>شارك عبر واتساب</button></a>", unsafe_allow_html=True)
    else:
        st.warning("يرجى إدخال اسم المنتج وسعر الكاش بشكل صحيح.")

# زر إعادة تعيين الحقول
if st.button("إعادة تعيين الحقول"):
    st.experimental_rerun()
