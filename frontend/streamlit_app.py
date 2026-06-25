import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from app.agent import generate_marketing_content

st.title("Marketing Agent")

business_name = st.text_input("Business Name")
audience = st.text_input("Audience")
goal = st.text_input("Goal")

platform = st.selectbox("Platform", ["Facebook", "Instagram", "LinkedIn"])

if st.button("Generate"):
    result = generate_marketing_content(
        business_name,
        audience,
        goal,
        platform
    )
    st.write(result)