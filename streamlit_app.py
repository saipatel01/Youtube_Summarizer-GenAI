import streamlit as st
from modules.transcript import get_transcript
from modules.summarizer import generate_summary
from modules.article import generate_article


st.set_page_config(page_title="YouTube Summarizer", page_icon="🎥")

st.title("🎥 YouTube Summarizer (GenAI)")
st.write("Convert YouTube videos into summaries and blog articles using Gemini AI")


# Input
url = st.text_input("Enter YouTube URL")

if st.button("Generate"):

    if not url:
        st.error("Please enter a YouTube URL")
    else:
        try:
            with st.spinner("Fetching transcript..."):
                transcript = get_transcript(url)

            st.success("Transcript fetched!")

            with st.spinner("Generating summary..."):
                summary = generate_summary(transcript)

            st.subheader("📌 Summary")
            st.write(summary)

            with st.spinner("Generating article..."):
                article = generate_article(summary)

            st.subheader("📰 Article")
            st.write(article)

            # Download buttons
            st.download_button(
                label="Download Summary",
                data=summary,
                file_name="summary.txt"
            )

            st.download_button(
                label="Download Article",
                data=article,
                file_name="article.md"
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")