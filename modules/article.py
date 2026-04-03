import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_article(summary: str) -> str:

    prompt = PromptTemplate.from_template("""
    Convert the following summary into a well-structured blog article.

    Include:
    - Title
    - Introduction
    - Headings
    - Conclusion

    Summary:
    {summary}
    """)

    chain = prompt | llm

    response = chain.invoke({"summary": summary})

    return response.content