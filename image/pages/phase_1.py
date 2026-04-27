import cv2
import streamlit as st
import numpy as np
from PIL import Image
from backend.phase_1 import segmentation

st.title("Phase 1 - segmentation ")

uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)  # convert to grey scale

    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    if st.button("Apply Operation"):
        threshold, output_image = segmentation(image)
        st.markdown(f"## Threshold = {threshold}")  # أقل شوية
        st.subheader("Output Image")
        st.image(output_image, use_container_width=True)

if st.button("Go to Phase 2"):
    st.switch_page("pages/phase_2.py")
