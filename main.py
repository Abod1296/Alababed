import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="متجر العبابيد", page_icon="🧾", layout="centered")

# ترويسة مخصصة
st.markdown(
    """
    <div style='text-align: center; margin-top: -50px;'>
        <h5 style='color: black;'>مرحباً بك في</h5>
        <h1 style='color: orange; font-family: "Arial Black", "Cairo", sans-serif;'>العبابيد</h1>
        <h4 style='color: grey;'>هدفنا ثقتكم</h4>
        <p style='color: #555;'>للتواصل: +963943001296</p>
        <div style='margin-top: 10px; padding: 5px 10px; background-color: #fca311; display: inline-block; border-radius: 5px; color: white; font-weight: bold;'>أقساطنا راحتكم</div>
    </div>
    """,
    unsafe_allow_html=True
)

# اختيار التصنيف
category = st.selectbox("اختر تصنيف المنتج", ["أجهزة محمولة", "كهربائيات", "مفروشات", "مواد بناء", "أخرى"])

# اسم المنتج وسعره
product_name = st.text_input("اسم المنتج")
cash_price = st.number_input("أدخل سعر الكاش (بالدولار)", min_value=0.0, step=10.0)

if st.button("احسب الأقساط"):
    if product_name and cash_price > 0:
        # الحسابات
        increased_price = int(cash_price * 1.3)
        min_down = int(increased_price * 0.25)
        max_down = int(increased_price * 0.34)
        recommended_down = (min_down + max_down) // 2
        monthly_installment = (increased_price - recommended_down) // 5

        # عرض النتائج بتنسيق جميل
        st.markdown(
            f"""
            <div style='background-color: #fca311; padding: 20px; border-radius: 10px; color: white; font-size: 18px;'>
                <b>اسم المنتج:</b> {product_name}<br>
                <b>التصنيف:</b> {category}<br>
                <b>السعر كاش:</b> {int(cash_price)} دولار<br>
                <b>السعر بعد الزيادة:</b> {increased_price} دولار<br>
                <b>الدفعة الأولى:</b> {recommended_down} دولار<br>
                <b>عدد الأقساط:</b> 5 دفعات<br>
                <b>قيمة كل دفعة:</b> {monthly_installment} دولار
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("يرجى إدخال اسم المنتج وسعر الكاش.")
