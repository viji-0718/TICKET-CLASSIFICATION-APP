import streamlit as st

# Custom CSS for background image
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1508780709619-79562169bc64");
    background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("🎯 Ticket Classification Result")

    
