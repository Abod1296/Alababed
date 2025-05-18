import streamlit as st

st.set_page_config(page_title="متجر العبابيد للتقسيط", layout="centered")

st.title("مرحبًا بك في متجر العبابيد للتقسيط الشرعي")
st.markdown("رضا الله فوق كل شيء، والتعامل الحلال هو الأساس.")

# تصنيفات
category = st.selectbox("اختر تصنيف المنتج", ["أجهزة محمولة", "كهربائيات", "مواد بناء", "غير ذلك"])
product_name = st.text_input("اسم المنتج")
cash_price = st.number_input("أدخل سعر الكاش (بالدولار)", min_value=0.0, step=10.0)

if st.button("احسب الأقساط"):
    if product_name and cash_price > 0:
        total_price = round(cash_price * 1.3, 2)
        down_payment = round(total_price / 3, 2)
        monthly_payment = round((total_price - down_payment) / 4, 2)

        st.success("تفاصيل الأقساط الشرعية:")
        st.write(f"**المنتج:** {product_name}")
        st.write(f"**التصنيف:** {category}")
        st.write(f"**السعر الكاش:** ${cash_price}")
        st.write(f"**السعر بعد الزيادة (30%):** ${total_price}")
        st.write(f"**الدفعة الأولى (ثلث المبلغ):** ${down_payment}")
        st.write(f"**القسط الشهري:** ${monthly_payment} × 4 أشهر")
    else:
        st.warning("يرجى تعبئة جميع الحقول.")
