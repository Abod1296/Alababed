import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="متجر العبابيد", page_icon="🛒", layout="centered")

# تنسيق CSS مخصص
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
        padding: 30px;
        border-radius: 12px;
        border: 1px solid #ddd;
        box-shadow: 0 3px 12px rgba(0,0,0,0.05);
    }
    .header-small {
        font-size: 20px;
        color: black;
        text-align: center;
        margin-bottom: 0px;
    }
    .header-main {
        font-size: 34px;
        color: orange;
        font-family: 'Tahoma', sans-serif;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 16px;
        color: #444;
        text-align: center;
        margin-bottom: 30px;
    }
    .result-box {
        background-color: #eef9f0;
        padding: 20px;
        border-radius: 10px;
        font-size: 17px;
        color: #2e7d32;
        line-height: 1.8;
    }
    </style>
""", unsafe_allow_html=True)

# الواجهة الأساسية
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="header-small">مرحباً بك في</div>', unsafe_allow_html=True)
st.markdown('<div class="header-main">العبابيد</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">هدفنا ثقتكم</div>', unsafe_allow_html=True)

# مدخلات المستخدم
category = st.selectbox("اختر تصنيف المنتج", ["أجهزة محمولة", "كهربائيات", "مواد بناء", "غير ذلك"])
product_name = st.text_input("اسم المنتج")
cash_price = st.number_input("أدخل سعر الكاش (بالدولار)", min_value=0.0, step=10.0)

# حساب الأقساط عند الضغط على الزر
if st.button("احسب الأقساط"):
    if product_name and cash_price > 0:
        total_price = round(cash_price * 1.3, 2)
        down_payment = round(total_price / 3, 2)
        monthly_payment = round((total_price - down_payment) / 4, 2)

        st.markdown(f"""
<div class="result-box">
<strong>المنتج:</strong> {product_name}<br>
<strong>التصنيف:</strong> {category}<br>
<strong>السعر الإجمالي بعد التقسيط:</strong> ${total_price}<br>
<strong>الدفعة الأولى (ثلث المبلغ):</strong> ${down_payment}<br>
<strong>عدد الأقساط:</strong> 4 أقساط شهرية بقيمة ${monthly_payment} لكل قسط
</div>
""", unsafe_allow_html=True)
    else:
        st.warning("يرجى إدخال جميع البيانات المطلوبة.")

st.markdown("</div>", unsafe_allow_html=True)
