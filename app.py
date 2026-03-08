import streamlit as st
from generator import generate_post

st.title("AI Social Media Post Creator")

st.write("Generate captions and hashtags for your social media posts.")

topic = st.text_input("Enter the topic of your post")

platform = st.selectbox(
    "Choose Platform",
    ["Instagram", "Twitter", "LinkedIn"]
)

tone = st.selectbox(
    "Choose Tone",
    ["Casual", "Professional", "Funny"]
)

if st.button("Generate Post"):

    result = generate_post(topic, platform, tone)

    st.subheader("Generated Captions")

    st.text(result)

    st.download_button(
        label="Download Captions",
        data=result,
        file_name="captions.txt",
        mime="text/plain"
    )