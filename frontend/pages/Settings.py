import streamlit as st

st.set_page_config(page_title="Settings", page_icon="⚙️")

st.title("⚙️ Settings")

st.subheader("Profile")

name = st.text_input("Name", "Usman")

email = st.text_input(
    "Email",
    "example@email.com"
)

theme = st.selectbox(
    "Theme",
    [
        "Light",
        "Dark"
    ]
)

notifications = st.checkbox(
    "Enable Notifications",
    value=True
)

api_key = st.text_input(
    "OpenAI API Key",
    type="password"
)

if st.button("Save Settings"):
    st.success("Settings saved successfully!")