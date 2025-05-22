import streamlit as st

st.title("tralala trilili")
st.write(
    "Love X-D."
)
st.image("views/IMG_8001.jpeg", width=200)
st.write("\n")
st.subheader("cacuca")
st.write(
    "coba liat coba"
)

#with col1 :
st.harder ("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)

if (angka % 2) ==0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
