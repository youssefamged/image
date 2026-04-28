import streamlit as st
import cv2
import numpy as np

from backend.phase_6 import change_red_color, eliminate_red_channel, swap_red_to_green

st.title("Operations")


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

    col1, col2 = st.columns(2)

    result = None
    threshold = None

    with col1:
        if "show_red_input" not in st.session_state:
            st.session_state.show_red_input = False

        if st.button("Change red color"):
            st.session_state.show_red_input = True

        if st.session_state.show_red_input:
            intensity = st.number_input(
                "Enter red intensity", min_value=0, max_value=255, value=255
            )

            result = change_red_color(image, intensity)
            st.image(result, caption="Red Changed", use_container_width=True)
        if st.button("eliminate red channel"):
            result = eliminate_red_channel(image)

    with col2:
        if st.button("swap_red_to_green"):
            result = swap_red_to_green(image)

    if result is not None:
        st.subheader("Result")
        show_image(result, "Restored Image")

        if threshold is not None:
            st.write("Threshold =", threshold)

else:
    st.warning("Please upload an image first.")


if st.button("Go to Phase 1"):
    st.switch_page("pages/phase_1.py")