import streamlit as st
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="متجر العبابيد للتقسيط", page_icon="💼", layout="centered")

# تنسيق CSS مخصص
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ddd;
        box-shadow: 0 0 10px rgba(0,0,0,0.05);
    }
    .title {
        font-size: 28px;
        font-weight: bold;
        color: #2E4053;
        text-align: center;
    }
    .subtitle {
        font-size: 16px;
        color: #566573;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# واجهة المستخدم
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">مرحباً بك في متجر العبابيد للتقسيط الشرعي</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">رضا الله فوق كل شيء، والتعامل الحلال هو الأساس.</div>', unsafe_allow_html=True)

# مدخلات المستخدم
category = st.selectbox("اختر تصنيف المنتج", ["أجهزة محمولة", "كهربائيات", "مواد بناء", "غير ذلك"])
product_name = st.text_input("اسم المنتج")
cash_price = st.number_input("أدخل سعر الكاش (بالدولار)", min_value=0.0, step=10.0)

# زر حساب
if st.button("احسب الأقساط"):
    if product_name and cash_price > 0:
        total_price = round(cash_price * 1.3, 2)
        down_payment = round(total_price / 3, 2)
        monthly_payment = round((total_price - down_payment) / 4, 2)

        with st.expander("تفاصيل الأقساط الشرعية:"):
            st.success(f"""
            **اسم المنتج:** {product_name}  
            **التصنيف:** {category}  
            **السعر كاش:** ${cash_price}  
            **السعر بعد الزيادة (30%):** ${total_price}  
            **الدفعة الأولى (ثلث):** ${down_payment}  
            **الأقساط:** 4 دفعات × ${monthly_payment}
            """)
    else:
        st.warning("يرجى تعبئة جميع الحقول.")

st.markdown("</div>", unsafe_allow_html=True)
