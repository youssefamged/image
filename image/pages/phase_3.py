import streamlit as st
import cv2
import numpy as np
from PIL import Image

from backend.phase_3 import (
    dilation,
    erosion,
    opening,
    internal_boundary,
    external_boundary,
    morphological_gradient,
)

st.title("Mathematical Morphology")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    st.image(image, caption="Original Image", use_container_width=True)

    col1, col2, col3 = st.columns(3)

    result = None

    with col1:
        if st.button("Dilation"):
            result, threshold = dilation(image)

        if st.button("Erosion"):
            result, threshold = erosion(image)

    with col2:
        if st.button("Opening"):
            result, threshold = opening(image)

        if st.button("Internal Boundary"):
            result, threshold = internal_boundary(image)

    with col3:
        if st.button("External Boundary"):
            result, threshold = external_boundary(image)

        if st.button("Morphological Gradient"):
            result, threshold = morphological_gradient(image)

    if result is not None:
        st.markdown(f"## Threshold = {threshold}")
        st.subheader("Result")
        st.image(result, use_container_width=True, clamp=True)

else:
    st.warning("Please upload an image first.")

if st.button("Go to Phase 4"):
    st.switch_page("pages/phase_4.py")