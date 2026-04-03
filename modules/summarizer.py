import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


# Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_summary(transcript_text: str) -> str:

    prompt = PromptTemplate.from_template("""
    Summarize the following YouTube transcript into:
    - 5 clear bullet points
    - Simple and easy to understand

    Transcript:
    {text}
    """)

    # New LangChain style (Runnable)
    chain = prompt | llm

    response = chain.invoke({"text": transcript_text[:4000]})

    return response.content