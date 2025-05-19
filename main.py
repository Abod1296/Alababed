import streamlit as st

# إعداد صفحة التطبيق
st.set_page_config(page_title="متجر العبابيد", page_icon="💰", layout="centered")

# عنوان الصفحة
st.markdown(
    """
    <div style='text-align: center; margin-top: -50px;'>
        <h4 style='color: black; font-family: sans-serif;'>مرحباً بك في</h4>
        <h1 style='color: orange; font-family: "Cairo", sans-serif;'>العبابيد</h1>
        <p style='color: #555;'>هدفنا ثقتكم</p>
    </div>
    """, unsafe_allow_html=True
)

# إدخال معلومات المنتج
st.write("")  # مسافة
col1, col2 = st.columns(2)
with col1:
    category = st.selectbox("اختر تصنيف المنتج", ["أجهزة محمولة", "كهربائيات", "مواد بناء", "أخرى"])
with col2:
    product_name = st.text_input("اسم المنتج")

cash_price = st.number_input("أدخل سعر الكاش (بالدولار)", min_value=0.0, step=1.0)

# زر إعادة تعيين
if st.button("إعادة تعيين الحقول"):
    st.session_state.clear()
    st.experimental_rerun()

# زر حساب الأقساط
if st.button("احسب الأقساط") and product_name and cash_price > 0:
    increased_price = int(cash_price * 1.3)
    down_payment = int(increased_price / 3.5)  # تقريباً بين الثلث والربع
    remaining = increased_price - down_payment
    monthly = round(remaining / 5)

    with st.container():
        st.markdown(
            f"""
            <div style='background-color: orange; padding: 15px; border-radius: 10px; color: white; font-family: "Cairo", sans-serif;'>
                <h4 style='margin-bottom: 10px;'>تفاصيل الأقساط:</h4>
                <p><strong>اسم المنتج:</strong> {product_name}</p>
                <p><strong>التصنيف:</strong> {category}</p>
                <p><strong>السعر كاش:</strong> {cash_price:.0f} $</p>
                <p><strong>السعر بعد الزيادة:</strong> {increased_price} $</p>
                <p><strong>الدفعة الأولى:</strong> {down_payment} $</p>
                <p><strong>عدد الدفعات:</strong> 5 أشهر</p>
                <p><strong>قيمة كل دفعة:</strong> {monthly} $</p>
                <p style='margin-top: 10px; font-weight: bold;'>اقساطنا راحتكم</p>
            </div>
            """, unsafe_allow_html=True
        )
else:
    st.markdown("<br>", unsafe_allow_html=True)
