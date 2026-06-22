import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Aplikasi Logika Fuzzy",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Aplikasi Logika Fuzzy")

menu = st.sidebar.selectbox(
    "Pilih Studi Kasus",
    [
        "Penilaian Mahasiswa",
        "Kelayakan Beasiswa",
        "Tingkat Kemacetan"
    ]
)

# ==================================================
# PENILAIAN MAHASISWA
# ==================================================

if menu == "Penilaian Mahasiswa":

    st.header("Penilaian Mahasiswa")

    nilai = st.number_input(
        "Masukkan Nilai",
        min_value=0.0,
        max_value=100.0,
        value=60.0
    )

    def rendah(x):
        if x <= 25:
            return 1
        elif 25 < x < 50:
            return (50 - x) / 25
        return 0

    def sedang(x):
        if x <= 25 or x >= 75:
            return 0
        elif 25 < x < 50:
            return (x - 25) / 25
        elif 50 <= x < 75:
            return (75 - x) / 25
        return 0

    def tinggi(x):
        if x <= 50:
            return 0
        elif 50 < x < 75:
            return (x - 50) / 25
        return 1

    if st.button("Hitung Nilai"):

        r = round(rendah(nilai), 2)
        s = round(sedang(nilai), 2)
        t = round(tinggi(nilai), 2)

        hasil = pd.DataFrame({
            "Nilai":[nilai],
            "Rendah":[r],
            "Sedang":[s],
            "Tinggi":[t]
        })

        st.table(hasil)

        x = np.arange(0,101,1)

        fig, ax = plt.subplots()

        ax.plot(x,[rendah(i) for i in x],label="Rendah")
        ax.plot(x,[sedang(i) for i in x],label="Sedang")
        ax.plot(x,[tinggi(i) for i in x],label="Tinggi")

        ax.axvline(nilai, linestyle="--")
        ax.scatter(nilai,r)
        ax.scatter(nilai,s)
        ax.scatter(nilai,t)

        ax.set_title("Grafik Penilaian Mahasiswa")
        ax.set_xlabel("Nilai")
        ax.set_ylabel("Keanggotaan")
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)

# ==================================================
# KELAYAKAN BEASISWA
# ==================================================

elif menu == "Kelayakan Beasiswa":

    st.header("Kelayakan Beasiswa")

    ipk = st.number_input(
        "Masukkan IPK",
        min_value=0.0,
        max_value=4.0,
        value=3.0,
        step=0.01
    )

    def tidak_layak(x):
        if x <= 2:
            return 1
        elif 2 < x < 3:
            return (3 - x)
        return 0

    def dipertimbangkan(x):
        if x <= 2 or x >= 4:
            return 0
        elif 2 < x < 3:
            return x - 2
        elif 3 <= x < 4:
            return 4 - x
        return 0

    def layak(x):
        if x <= 3:
            return 0
        elif 3 < x < 4:
            return x - 3
        return 1

    if st.button("Hitung Beasiswa"):

        tl = round(tidak_layak(ipk),2)
        dp = round(dipertimbangkan(ipk),2)
        ly = round(layak(ipk),2)

        hasil = pd.DataFrame({
            "IPK":[ipk],
            "Tidak Layak":[tl],
            "Dipertimbangkan":[dp],
            "Layak":[ly]
        })

        st.table(hasil)

        x = np.arange(0,4.01,0.01)

        fig, ax = plt.subplots()

        ax.plot(x,[tidak_layak(i) for i in x],label="Tidak Layak")
        ax.plot(x,[dipertimbangkan(i) for i in x],label="Dipertimbangkan")
        ax.plot(x,[layak(i) for i in x],label="Layak")

        ax.axvline(ipk, linestyle="--")
        ax.scatter(ipk,tl)
        ax.scatter(ipk,dp)
        ax.scatter(ipk,ly)

        ax.set_title("Grafik Kelayakan Beasiswa")
        ax.set_xlabel("IPK")
        ax.set_ylabel("Keanggotaan")
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)

# ==================================================
# TINGKAT KEMACETAN
# ==================================================

else:

    st.header("Tingkat Kemacetan")

    kendaraan = st.number_input(
        "Masukkan Jumlah Kendaraan",
        min_value=0,
        max_value=1000,
        value=700
    )

    def lancar(x):
        if x <= 300:
            return 1
        elif 300 < x < 600:
            return (600 - x)/300
        return 0

    def padat(x):
        if x <= 300 or x >= 900:
            return 0
        elif 300 < x < 600:
            return (x - 300)/300
        elif 600 <= x < 900:
            return (900 - x)/300
        return 0

    def macet(x):
        if x <= 600:
            return 0
        elif 600 < x < 900:
            return (x - 600)/300
        return 1

    if st.button("Hitung Kemacetan"):

        l = round(lancar(kendaraan),2)
        p = round(padat(kendaraan),2)
        m = round(macet(kendaraan),2)

        hasil = pd.DataFrame({
            "Jumlah Kendaraan":[kendaraan],
            "Lancar":[l],
            "Padat":[p],
            "Macet":[m]
        })

        st.table(hasil)

        x = np.arange(0,1001,1)

        fig, ax = plt.subplots()

        ax.plot(x,[lancar(i) for i in x],label="Lancar")
        ax.plot(x,[padat(i) for i in x],label="Padat")
        ax.plot(x,[macet(i) for i in x],label="Macet")

        ax.axvline(kendaraan, linestyle="--")
        ax.scatter(kendaraan,l)
        ax.scatter(kendaraan,p)
        ax.scatter(kendaraan,m)

        ax.set_title("Grafik Tingkat Kemacetan")
        ax.set_xlabel("Jumlah Kendaraan")
        ax.set_ylabel("Keanggotaan")
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)
