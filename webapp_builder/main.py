import streamlit as st
from utilities import CodeGenerator, ImageProcessor


def main():
    st.set_page_config(
        page_title="Image To Code Generation",
        page_icon="🖼️",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    # Add some custom styling
    main_bg = "rgba(255, 229, 180, 0.8)"
    main_fg = "#006400"  # Dark Green

    st.markdown(
        f"""
        <style>
            .reportview-container {{
                background-color: {main_bg};
                color: {main_fg};
                border: 2px solid {main_fg};
                border-radius: 5px;
                padding: 20px;
            }}
            .sidebar .sidebar-content {{
                background-color: {main_bg};
            }}
            h1, h2, h3 {{
                color: {main_fg};
            }}
            div.stButton > button {{
                background-color: {main_fg};
                color: {main_bg};
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("App Builder -- Code Generator")
    st.header("Upload an image and get codes")

    st.markdown("<br>", unsafe_allow_html=True)
    upload_file = st.file_uploader("Choose an image:", type=["jpg", "png"])

    if upload_file is not None:
        file_bytes = upload_file.getvalue()
        with open(upload_file.name, "wb") as file:
            file.write(file_bytes)

        st.image(
            upload_file,
            caption="The uploaded image",
            use_column_width=True,
            width=250,
            output_format="JPEG",
            channels="RGB",
        )

        code_generator = CodeGenerator()
        image_processor = ImageProcessor()

        with st.spinner(
            "Generating Code... Please wait, it might take a little time..."
        ):
            code_text = image_processor.get_image_description(
                upload_file.name, code_generator.api_key
            )
            code = code_generator.generate_code(code_text=code_text)

            with st.expander("Implementations", False):
                st.markdown(code, unsafe_allow_html=True, help=None)


if __name__ == "__main__":
    main()
