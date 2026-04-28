import streamlit as st
import cv2
import numpy as np

from backend.phase_5 import (
    restore_gauss_averaging,
    restore_gauss_filter,
    restore_sp_average,
    restore_sp_median,
    restore_sp_outlier,
)

st.title("Restoration")


def show_image(img, caption="Image"):
    if img is None:
        return

    if len(img.shape) == 2:
        st.image(img, caption=caption, channels="GRAY", use_container_width=True)

    elif img.shape[2] == 3:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        st.image(img_rgb, caption=caption, use_container_width=True)

    elif img.shape[2] == 4:
        img_rgba = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
        st.image(img_rgba, caption=caption, use_container_width=True)


uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)

    # Read image as it is
    image = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)

    show_image(image, "Original Image")

    col1, col2, col3 = st.columns(3)

    result = None
    threshold = None

    with col1:
        if st.button("gauss averaging"):
            result = restore_gauss_averaging(image)

        if st.button("gauss filter"):
            result = restore_gauss_filter(image)

    with col2:
        if st.button("sp average"):
            result = restore_sp_average(image)

        if st.button("sp median"):
            result = restore_sp_median(image)

    with col3:
        if st.button("sp outlier"):
            result = restore_sp_outlier(image)

    if result is not None:
        st.subheader("Result")
        show_image(result, "Restored Image")

        if threshold is not None:
            st.write("Threshold =", threshold)

else:
    st.warning("Please upload an image first.")


if st.button("Go to Phase 6"):
    st.switch_page("pages/phase_6.py")