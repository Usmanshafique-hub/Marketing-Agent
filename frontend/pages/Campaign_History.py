import streamlit as st
import pandas as pd

st.set_page_config(page_title="Campaign History", page_icon="📁")

st.title("📁 Campaign History")

data = {
    "Business": [
        "OYO",
        "Nike",
        "Tesla",
        "Apple"
    ],
    "Platform": [
        "Facebook",
        "Instagram",
        "LinkedIn",
        "Twitter"
    ],
    "Goal": [
        "Bookings",
        "Sales",
        "Brand Awareness",
        "Engagement"
    ]
}

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)

selected = st.selectbox(
    "Select Campaign",
    df["Business"]
)

st.write(f"Selected Campaign: **{selected}**")