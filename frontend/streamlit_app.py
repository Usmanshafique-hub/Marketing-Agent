import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from app.agent import generate_marketing_content

st.title("AI Marketing Agent")

business_name = st.text_input("Business Name")
audience = st.text_input("Audience")
goal = st.text_input("Goal")

tool = st.selectbox(
    "Select Tool",
    [
        "Facebook Ad",
        "Instagram Post",
        "Google Ad",
        "Email Marketing",
        "SEO Keywords",
        "Marketing Strategy"
    ]
)

platform = st.selectbox(
    "Platform",
    [
        "Facebook",
        "Instagram",
        "LinkedIn"
        "Google"
        "Email"
    ]
)

if st.button("Generate"):

    if business_name and audience and goal:

        result = generate_marketing_content(
            business_name,
            audience,
            goal,
            platform,
            tool
        )

        st.write(result)

    else:
        st.warning("Please fill all fields.")