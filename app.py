import streamlit as st
import numpy as np
import cv2
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import os


# ================================================================
# 1. KONFIGURASI HALAMAN
# ================================================================

st.set_page_config(
    page_title="Adara Skincare",
    page_icon="logo_adara.png",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ================================================================
# 2. SESSION STATE
# ================================================================

if "halaman_utama" not in st.session_state:
    st.session_state.halaman_utama = False


# ================================================================
# 3. CUSTOM CSS
# ================================================================

st.markdown(
    """
    <style>

    /* ============================================================
       BACKGROUND
       ============================================================ */

    .stApp {
        background: linear-gradient(
            135deg,
            #FFF5F7 0%,
            #F8E8DC 100%
        );
    }


    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }


    /* ============================================================
       TOMBOL
       ============================================================ */

    .stButton > button {
        background: linear-gradient(
            90deg,
            #C98282 0%,
            #B85C5C 100%
        );

        color: white !important;

        border: none;

        border-radius: 25px;

        min-height: 50px;

        font-size: 16px;

        font-weight: 700;

        width: 100%;

        box-shadow:
            0 5px 18px
            rgba(184, 92, 92, 0.25);

        transition: 0.3s;
    }


    .stButton > button:hover {
        background: linear-gradient(
            90deg,
            #B96F6F 0%,
            #A95252 100%
        );

        color: white !important;

        transform: translateY(-2px);

        box-shadow:
            0 7px 22px
            rgba(184, 92, 92, 0.35);
    }


    /* ============================================================
       JUDUL WELCOME
       ============================================================ */

    .welcome-title {
        color: #A95252;
        text-align: center;
        font-weight: 700;
    }


    .welcome-subtitle {
        color: #26364A;
        text-align: center;
        font-weight: 600;
    }


    /* ============================================================
       KARTU HASIL
       ============================================================ */

    .hasil-box {
        background-color:
            rgba(255, 255, 255, 0.90);

        border-radius: 15px;

        padding: 20px;

        margin-top: 15px;

        margin-bottom: 15px;

        box-shadow:
            0 5px 20px
            rgba(184, 92, 92, 0.10);
    }


    /* ============================================================
       FOOTER
       ============================================================ */

    .footer {
        text-align: center;

        color: #777777;

        font-size: 13px;

        margin-top: 30px;

        padding-top: 15px;

        border-top:
            1px solid
            rgba(180, 100, 100, 0.15);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ================================================================
# 4. HALAMAN SELAMAT DATANG
# ================================================================

if not st.session_state.halaman_utama:

    st.write("")


    # ============================================================
    # LOGO ADARA
    # ============================================================

    if os.path.exists("logo_adara.png"):

        kolom_kiri, kolom_logo, kolom_kanan = st.columns(
            [1, 1, 1]
        )

        with kolom_logo:

            st.image(
                "logo_adara.png",
                width=180
            )

    else:

        st.warning(
            "File logo_adara.png tidak ditemukan."
        )


    st.write("")


    # ============================================================
    # JUDUL SELAMAT DATANG
    # ============================================================

    st.title(
        "Selamat Datang di Adara Skincare"
    )


    # ============================================================
    # SUBJUDUL
    # ============================================================

    st.subheader(
        "Sistem Klasifikasi Wajah & "
        "Rekomendasi Produk Skincare"
    )


    # ============================================================
    # DESKRIPSI
    # ============================================================

    st.write(
        "Aplikasi ini menggunakan teknologi "
        "**Deep Learning** untuk mendeteksi kondisi "
        "kulit wajah dan memberikan rekomendasi "
        "produk skincare yang sesuai."
    )


    # ============================================================
    # SLOGAN
    # ============================================================

    st.markdown(
        "*“Kenali Kulitmu, Temukan Perawatan Terbaikmu”*"
    )


    st.write("")


    # ============================================================
    # TOMBOL MULAI APLIKASI
    # ============================================================

    kolom1, kolom2, kolom3 = st.columns(
        [1, 2, 1]
    )


    with kolom2:

        if st.button(
            "MULAI APLIKASI  →",
            use_container_width=True
        ):

            st.session_state.halaman_utama = True

            st.rerun()


    st.write("")


    # ============================================================
    # FITUR APLIKASI
    # ============================================================

    st.markdown("---")

    st.subheader(
        "Fitur Aplikasi"
    )


    # ------------------------------------------------------------
    # FITUR 1
    # ------------------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        st.markdown(
            "### Unggah Foto Wajah"
        )

        st.write(
            "Gunakan foto wajah dalam format "
            "JPG, JPEG, atau PNG."
        )


    # ------------------------------------------------------------
    # FITUR 2
    # ------------------------------------------------------------

    with col2:

        st.markdown(
            "### Deteksi Kondisi Kulit"
        )

        st.write(
            "Klasifikasi kondisi kulit menggunakan "
            "teknologi Deep Learning."
        )


    # ------------------------------------------------------------
    # FITUR 3
    # ------------------------------------------------------------

    col3, col4 = st.columns(2)


    with col3:

        st.markdown(
            "### Rekomendasi Produk"
        )

        st.write(
            "Mendapatkan rekomendasi produk "
            "skincare yang sesuai."
        )


    # ------------------------------------------------------------
    # FITUR 4
    # ------------------------------------------------------------

    with col4:

        st.markdown(
            "### Mudah Digunakan"
        )

        st.write(
            "Antarmuka sederhana dan mudah digunakan."
        )


    st.write("")
    st.write("")


    # ============================================================
    # FOOTER
    # ============================================================

    st.markdown(
        """
        <div class="footer">
            Adara Skincare |
            Sistem Klasifikasi Wajah & Rekomendasi Produk
        </div>
        """,
        unsafe_allow_html=True
    )


    # ============================================================
    # STOP HALAMAN WELCOME
    # ============================================================

    st.stop()


# ================================================================
# 5. HALAMAN UTAMA APLIKASI
# ================================================================

st.title(
    "Sistem Klasifikasi Wajah & "
    "Rekomendasi Produk Skincare Adara"
)


st.subheader(
    "Sistem Deteksi Kondisi Kulit Wajah & "
    "Rekomendasi Produk Berbasis Deep Learning"
)


# ================================================================
# 6. TOMBOL KEMBALI
# ================================================================

if st.button(
    "← Kembali ke Halaman Awal"
):

    st.session_state.halaman_utama = False

    st.rerun()


# ================================================================
# 7. ATURAN REKOMENDASI PRODUK
# ================================================================

ATURAN_REKOMENDASI = {

    "Jerawat": {

        "produk":
            "Adara P.M.S Series Stay Clear Enzyme Wash",

        "aturan":
            "Jerawat",

        "deskripsi":
            (
                "Pembersih wajah khusus untuk merawat "
                "kulit berjerawat dan membersihkan "
                "pori-pori secara mendalam."
            ),

        "gambar":
            "pms.png"
    },


    "Bekas Jerawat": {

        "produk":
            "Adara Bee White Spotless Cream",

        "aturan":
            "Bekas Jerawat",

        "deskripsi":
            (
                "Krim perawatan untuk membantu "
                "menyamarkan noda hitam dan "
                "bekas jerawat pada wajah."
            ),

        "gambar":
            "spotless_cream.png"
    },


    "Komedo": {

        "produk":
            "Adara P.M.S Package",

        "aturan":
            "Komedo",

        "deskripsi":
            (
                "Rangkaian paket perawatan untuk "
                "mengatasi komedo dan membantu "
                "mengontrol minyak berlebih."
            ),

        "gambar":
            "pms_package.png"
    },


    "Normal": {

        "produk":
            "Adara Bee White Foam Cleanser",

        "aturan":
            "Kulit Normal",

        "deskripsi":
            (
                "Pembersih wajah bertekstur busa lembut "
                "untuk menjaga kebersihan dan kesegaran "
                "kulit normal."
            ),

        "gambar":
            "foam_cleanser.png"
    }
}


# ================================================================
# 8. LOAD MODEL DAN DETEKTOR WAJAH
# ================================================================

@st.cache_resource
def load_components():

    # ------------------------------------------------------------
    # Load model
    # ------------------------------------------------------------

    model_path = "model_final.h5"


    if not os.path.exists(model_path):

        raise FileNotFoundError(
            "File model_final.h5 tidak ditemukan."
        )


    model = tf.keras.models.load_model(
        model_path,
        compile=False
    )


    # ------------------------------------------------------------
    # Load Haar Cascade
    # ------------------------------------------------------------

    cascade_path = (
        "haarcascade_frontalface_default.xml"
    )


    if not os.path.exists(cascade_path):

        raise FileNotFoundError(
            "File "
            "haarcascade_frontalface_default.xml "
            "tidak ditemukan."
        )


    face_cascade = cv2.CascadeClassifier(
        cascade_path
    )


    if face_cascade.empty():

        raise RuntimeError(
            "Haar Cascade gagal dimuat."
        )


    return model, face_cascade


# ================================================================
# 9. LOAD KOMPONEN
# ================================================================

try:

    model, face_cascade = load_components()


except Exception as e:

    st.error(
        "Gagal memuat komponen aplikasi."
    )

    st.warning(
        "Pastikan file model_final.h5 dan "
        "haarcascade_frontalface_default.xml "
        "berada di folder yang sama dengan app.py."
    )

    st.code(
        str(e)
    )

    st.stop()


# ================================================================
# 10. KONFIGURASI MODEL
# ================================================================

IMG_SIZE = (
    224,
    224
)

THRESHOLD_MASALAH = 0.003


# ================================================================
# 11. UPLOAD FOTO
# ================================================================

st.markdown("---")

st.subheader(
    "Unggah Foto Wajah"
)


uploaded_file = st.file_uploader(
    "Pilih foto wajah Anda",
    type=[
        "jpg",
        "jpeg",
        "png"
    ]
)


# ================================================================
# 12. PROSES FOTO
# ================================================================

if uploaded_file is not None:

    try:

        # --------------------------------------------------------
        # Membaca file
        # --------------------------------------------------------

        file_bytes = np.asarray(
            bytearray(
                uploaded_file.read()
            ),
            dtype=np.uint8
        )


        img_cv = cv2.imdecode(
            file_bytes,
            cv2.IMREAD_COLOR
        )


        # --------------------------------------------------------
        # Validasi gambar
        # --------------------------------------------------------

        if img_cv is None:

            st.error(
                "Foto tidak dapat dibaca."
            )

            st.info(
                "Silakan gunakan foto JPG, JPEG, "
                "atau PNG yang valid."
            )

            st.stop()


        # --------------------------------------------------------
        # Konversi warna
        # --------------------------------------------------------

        img_cv_rgb = cv2.cvtColor(
            img_cv,
            cv2.COLOR_BGR2RGB
        )


        gray = cv2.cvtColor(
            img_cv,
            cv2.COLOR_BGR2GRAY
        )


        # ========================================================
        # 13. DETEKSI WAJAH
        # ========================================================

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(100, 100)
        )


        # ========================================================
        # 14. CROPPING WAJAH
        # ========================================================

        if len(faces) > 0:

            # Mengambil wajah terbesar
            x, y, w, h = max(
                faces,
                key=lambda b: b[2] * b[3]
            )


            # Padding
            pad_w = int(
                w * 0.1
            )

            pad_h = int(
                h * 0.1
            )


            ymin = max(
                0,
                y - pad_h
            )


            ymax = min(
                img_cv.shape[0],
                y + h + pad_h
            )


            xmin = max(
                0,
                x - pad_w
            )


            xmax = min(
                img_cv.shape[1],
                x + w + pad_w
            )


            # Crop wajah
            cropped_face = img_cv_rgb[
                ymin:ymax,
                xmin:xmax
            ]


            img_input = Image.fromarray(
                cropped_face
            )


            status_crop = (
                "Berhasil memotong area wajah "
                "secara otomatis."
            )


        else:

            # Jika wajah tidak ditemukan
            img_input = Image.fromarray(
                img_cv_rgb
            )


            status_crop = (
                "Wajah tidak terdeteksi secara presisi. "
                "Sistem menggunakan citra utuh."
            )


        # ========================================================
        # 15. TAMPILKAN FOTO
        # ========================================================

        st.subheader(
            "Hasil Prapemrosesan"
        )


        col1, col2 = st.columns(2)


        with col1:

            st.image(
                img_cv_rgb,
                caption="Foto Original",
                use_container_width=True
            )


        with col2:

            st.image(
                img_input,
                caption="Hasil Cropping Wajah",
                use_container_width=True
            )


        st.info(
            f"Status Sistem: {status_crop}"
        )


        st.write("")


        # ========================================================
        # 16. TOMBOL ANALISIS
        # ========================================================

        if st.button(
            "MENGANALISIS KONDISI KULIT SEKARANG",
            use_container_width=True
        ):

            with st.spinner(
                "Sedang menganalisis kondisi kulit..."
            ):

                # ------------------------------------------------
                # Resize
                # ------------------------------------------------

                img_resize = img_input.resize(
                    IMG_SIZE
                )


                # ------------------------------------------------
                # Konversi menjadi array
                # ------------------------------------------------

                img_array = img_to_array(
                    img_resize
                ) / 255.0


                # ------------------------------------------------
                # Tambahkan dimensi batch
                # ------------------------------------------------

                img_batch = np.expand_dims(
                    img_array,
                    axis=0
                )


                # ------------------------------------------------
                # Prediksi model
                # ------------------------------------------------

                prediction = model.predict(
                    img_batch,
                    verbose=0
                )[0]


            # ====================================================
            # 17. VALIDASI OUTPUT MODEL
            # ====================================================

            if len(prediction) < 4:

                st.error(
                    "Output model tidak sesuai. "
                    "Model harus menghasilkan "
                    "4 kelas klasifikasi."
                )

                st.stop()


            # ====================================================
            # 18. PROBABILITAS
            # ====================================================

            prob_bekas = (
                float(prediction[0]) * 100
            )


            prob_jerawat = (
                float(prediction[1]) * 100
            )


            prob_komedo = (
                float(prediction[2]) * 100
            )


            prob_normal = (
                float(prediction[3]) * 100
            )


            # ====================================================
            # 19. PROBABILITAS MASALAH
            # ====================================================

            probs_masalah = {

                "Bekas Jerawat":
                    prob_bekas,

                "Jerawat":
                    prob_jerawat,

                "Komedo":
                    prob_komedo
            }


            # ====================================================
            # 20. MENCARI PROBABILITAS TERTINGGI
            # ====================================================

            nama_tertinggi = max(
                probs_masalah,
                key=probs_masalah.get
            )


            prob_tertinggi = (
                probs_masalah[
                    nama_tertinggi
                ]
            )


            # ====================================================
            # 21. MENENTUKAN HASIL
            # ====================================================

            if (
                prob_tertinggi / 100
            ) > THRESHOLD_MASALAH:

                hasil = nama_tertinggi

                conf = prob_tertinggi

                penjelasan = (
                    f"Sistem mendeteksi indikasi dominan "
                    f"{nama_tertinggi} dengan tingkat "
                    f"probabilitas {conf:.2f}%."
                )


            else:

                hasil = "Normal"

                conf = prob_normal

                penjelasan = (
                    "Indikasi masalah kulit berada pada "
                    "batas aman (≤ 0.30%). Kondisi kulit "
                    "tergolong Sehat/Normal."
                )


            # ====================================================
            # 22. HASIL ANALISIS
            # ====================================================

            st.markdown("---")

            st.subheader(
                "Hasil Analisis"
            )


            if hasil == "Normal":

                st.success(
                    f"Kondisi Terdeteksi: {hasil}"
                )

            else:

                st.warning(
                    f"Kondisi Terdeteksi: {hasil}"
                )


            st.write(
                penjelasan
            )


            # ====================================================
            # 23. DISTRIBUSI PROBABILITAS
            # ====================================================

            st.subheader(
                "Distribusi Probabilitas Klasifikasi"
            )


            col_a, col_b = st.columns(2)


            with col_a:

                st.metric(
                    "Bekas Jerawat",
                    f"{prob_bekas:.2f}%"
                )


            with col_b:

                st.metric(
                    "Jerawat",
                    f"{prob_jerawat:.2f}%"
                )


            col_c, col_d = st.columns(2)


            with col_c:

                st.metric(
                    "Komedo",
                    f"{prob_komedo:.2f}%"
                )


            with col_d:

                st.metric(
                    "Normal",
                    f"{prob_normal:.2f}%"
                )


            # ====================================================
            # 24. REKOMENDASI PRODUK
            # ====================================================

            st.markdown("---")

            st.subheader(
                "Rekomendasi Produk"
            )


            rekomendasi_info = (
                ATURAN_REKOMENDASI.get(
                    hasil,
                    None
                )
            )


            if rekomendasi_info is not None:

                # ------------------------------------------------
                # Layout gambar + informasi
                # ------------------------------------------------

                kolom_gambar, kolom_info = st.columns(
                    [1, 2]
                )


                # ------------------------------------------------
                # GAMBAR PRODUK
                # ------------------------------------------------

                with kolom_gambar:

                    nama_gambar = (
                        rekomendasi_info[
                            "gambar"
                        ]
                    )


                    if os.path.exists(
                        nama_gambar
                    ):

                        st.image(
                            nama_gambar,
                            use_container_width=True
                        )

                    else:

                        st.warning(
                            "Gambar produk tidak ditemukan."
                        )


                # ------------------------------------------------
                # INFORMASI PRODUK
                # ------------------------------------------------

                with kolom_info:

                    st.success(
                        rekomendasi_info[
                            "produk"
                        ]
                    )


                    st.write(
                        "**Untuk Kondisi Wajah:** "
                        + rekomendasi_info[
                            "aturan"
                        ]
                    )


                    st.write(
                        "**Deskripsi:** "
                        + rekomendasi_info[
                            "deskripsi"
                        ]
                    )


            else:

                st.info(
                    "Rekomendasi produk "
                    "tidak tersedia."
                )


    # ============================================================
    # 25. ERROR SAAT MEMPROSES FOTO
    # ============================================================

    except Exception as e:

        st.error(
            "Terjadi kesalahan saat memproses foto."
        )

        st.code(
            str(e)
        )


# ================================================================
# 26. FOOTER
# ================================================================

st.markdown("---")

st.caption(
    "Adara Skincare | "
    "Sistem Klasifikasi Wajah & Rekomendasi Produk "
    "Berbasis Deep Learning"
)

st.caption(
    "© 2026 Adara Skincare. All rights reserved."
)