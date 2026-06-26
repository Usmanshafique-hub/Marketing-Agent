import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="📊")

st.title("📊 Marketing Agent Dashboard")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Campaigns", "12", "+2")

with col2:
    st.metric("Generated Content", "68", "+10")

with col3:
    st.metric("Success Rate", "95%", "+3%")

st.markdown("---")

st.subheader("Recent Activity")

activities = [
    "Facebook campaign generated",
    "Instagram post created",
    "Email campaign completed",
    "LinkedIn strategy generated",
]

for item in activities:
    st.success(item)

st.markdown("---")

st.info("Welcome to your Marketing Agent dashboard.")