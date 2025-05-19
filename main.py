import streamlit as st

# تنسيق العنوان الرئيسي
st.markdown("""
    <h3 style='text-align: center; color: black;'>مرحباً بك في</h3>
    <h1 style='text-align: center; color: orange; font-family: "Courier New", monospace;'>العبابيد</h1>
    <h4 style='text-align: center; color: gray;'>هدفنا ثقتكم</h4>
""", unsafe_allow_html=True)

# ملصق جانبي
st.markdown("<div style='text-align: center; color: orange; font-weight: bold;'>أقساطنا راحتكم</div>", unsafe_allow_html=True)

# نموذج الإدخال
تصنيفات = ["أجهزة محمولة", "أجهزة كهربائية", "مواد بناء", "مفروشات", "أخرى"]
نوع_المنتج = st.selectbox("اختر تصنيف المنتج", تصنيفات)
اسم_المنتج = st.text_input("اسم المنتج")
سعر_الكاش = st.number_input("أدخل سعر الكاش (بالدولار)", min_value=0.0, format="%.2f")

# زر لحساب الأقساط
if st.button("احسب كسامك") and اسم_المنتج and سعر_الكاش > 0:
    السعر_بعد_الزيادة = round(سعر_الكاش * 1.3)
    
    الدفعة_الأولى_ثلث = السعر_بعد_الزيادة // 3
    الدفعة_الأولى_ربع = السعر_بعد_الزيادة // 4
    
    الدفعة_الأولى = max(الدفعة_الأولى_ربع, الدفعة_الأولى_ثلث)
    المتبقي = السعر_بعد_الزيادة - الدفعة_الأولى
    عدد_الأشهر = 5
    القسط_الشهري = round(المتبقي / عدد_الأشهر)

    st.markdown("### تفاصيل الأقساط الشرعية:")
    st.markdown(f"""
    <div style='background-color: orange; padding: 15px; border-radius: 10px; color: white; font-size: 18px;'>
    <strong>المنتج:</strong> {اسم_المنتج}<br>
    <strong>التصنيف:</strong> {نوع_المنتج}<br>
    <strong>السعر كاش:</strong> {سعر_الكاش}$<br>
    <strong>السعر بعد الزيادة:</strong> {السعر_بعد_الزيادة}$<br>
    <strong>الدفعة الأولى:</strong> {الدفعة_الأولى}$<br>
    <strong>عدد الدفعات:</strong> {عدد_الأشهر} أشهر<br>
    <strong>قيمة القسط الشهري:</strong> {القسط_الشهري}$<br>
    </div>
    """, unsafe_allow_html=True)

# زر إعادة التعيين
if st.button("إعادة تعيين الحقول"):
    st.session_state.clear()
    st.rerun()
