import streamlit as st
import cv2
import numpy as np

from backend.phase_7 import *

st.title("Phase 7")

file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if file is not None:
    bytes_data = np.frombuffer(file.read(), np.uint8)

    img_color = cv2.imdecode(bytes_data, cv2.IMREAD_COLOR)
    img_gray = cv2.imdecode(bytes_data, cv2.IMREAD_GRAYSCALE)

    st.image(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB), caption="Original")

    value = st.number_input("Value", min_value=1, max_value=255, value=50)

    if st.button("Addition"):
        result = addition(img_color, value)
        st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))

    if st.button("Subtraction"):
        result = subtraction(img_color, value)
        st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))

    if st.button("Division"):
        result = division(img_color, value)
        st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))

    if st.button("Complement"):
        result = complement(img_color)
        st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))

    if st.button("Average Filter"):
        result = average_filter(img_gray)
        st.image(result)

    if st.button("Laplacian Filter"):
        result = laplacian_filter(img_gray)
        st.image(result)

    if st.button("Max Filter"):
        result = max_filter(img_gray)
        st.image(result)

    if st.button("Min Filter"):
        result = min_filter(img_gray)
        st.image(result)

    if st.button("Median Filter"):
        result = median_filter(img_gray)
        st.image(result)

    if st.button("Mode Filter"):
        result = mode_filter(img_gray)
        st.image(result)