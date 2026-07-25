import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Bakery Calculator", layout="wide")

# Hide Streamlit's default padding/menu so the page looks clean
st.markdown(
    """
    <style>
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        header[data-testid="stHeader"] {
            display: none;
        }
        #MainMenu, footer {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load your existing HTML calculator
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Render it. Increase height if the bottom of your calculator gets cut off.
components.html(html, height=1200, scrolling=True)
