import cv2
import streamlit as st
import numpy as np
from PIL import Image
from backend.phase_2 import edge_detect

st.title("Phase 2 -  Edge Detection ")

uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    if st.button("Apply Operation"):
        output_image = edge_detect(image)

        st.subheader("Output Image")
        st.image(output_image, use_container_width=True)
if st.button("Go to Phase 3"):
    st.switch_page("pages/phase_3.py")