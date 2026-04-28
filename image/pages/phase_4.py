import cv2
import streamlit as st
import numpy as np
from PIL import Image
from backend.phase_4 import histogram_equalization, histogram_stretching

st.title("Phase 4 -  histogram ")

uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    if st.button("Equalization"):
        output_image = histogram_equalization(image)
        st.subheader("Output Image")
        st.image(output_image, use_container_width=True)
    if st.button("Stretching"):
        output_image = histogram_stretching(image)
        st.subheader("Output Image")
        st.image(output_image, use_container_width=True)
if st.button("Go to Phase 5"):
    st.switch_page("pages/phase_5.py")