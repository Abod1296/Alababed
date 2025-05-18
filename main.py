import streamlit as st
from urllib.parse import quote

st.set_page_config(page_title="متجر العبابيد", layout="centered")

# ترويسة منسقة
st.markdown("""
    <h4 style='text-align: center; color: black;'>مرحباً بك في</h4>
    <h1 style='text-align: center; color: orange; font-family: "Cairo", sans-serif;'>العبابيد</h1>
    <p style='text-align: center; color: gray;'>هدفنا ثقتكم</p>
""", unsafe_allow_html=True)

# إدخال البيانات
category = st.selectbox("اختر تصنيف المنتج", ["أجهزة محمولة", "كهربائيات", "مواد بناء", "أخرى"])
product_name = st.text_input("اسم المنتج")
cash_price = st.number_input("أدخل سعر الكاش (بالدولار)", min_value=0.0, step=10.0)

if st.button("احسب الأقساط"):
    if product_name and cash_price > 0:
        increased_price = int(cash_price * 1.30)
        down_payment = round(increased_price / 3)  # تقريب الرقم الصحيح
        monthly_payment = round((increased_price - down_payment) / 5)

        # عرض التقرير بشكل منسق وجميل
        report = f"""
        اسم المنتج: {product_name}
        التصنيف: {category}
        السعر بعد الزيادة: {increased_price} دولار
        الدفعة الأولى (ثلث تقريباً): {down_payment} دولار
        عدد الأقساط: 5 دفعات × {monthly_payment} دولار
        """

        st.markdown("""
            <div style='background-color: orange; padding: 15px; border-radius: 10px; color: white; font-size: 16px;'>
            <strong>تفاصيل الأقساط:</strong><br><br>
            {}
            <p style='text-align: center; margin-top: 10px; font-weight: bold;'>أقساطنا راحتكم</p>
            </div>
        """.format(report.replace("\n", "<br>")), unsafe_allow_html=True)

        # رابط المشاركة
        share_link = f"https://wa.me/?text={quote('تفاصيل المنتج:\n' + report)}"
        st.markdown(f"<a href='{share_link}' target='_blank'><button>مشاركة عبر واتساب</button></a>", unsafe_allow_html=True)
    else:
        st.warning("يرجى إدخال اسم المنتج وسعر الكاش.")
