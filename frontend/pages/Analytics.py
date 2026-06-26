import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analytics", page_icon="📈")

st.title("📈 Analytics")

analytics = pd.DataFrame(
    {
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ],
        "Campaigns": [
            3,
            5,
            4,
            8,
            10,
            12
        ]
    }
)

st.line_chart(
    analytics.set_index("Month")
)

st.bar_chart(
    analytics.set_index("Month")
)

st.metric(
    "Average Monthly Campaigns",
    "7"
)