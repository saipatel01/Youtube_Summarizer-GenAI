# 🎥 YouTube Summarizer using Generative AI

## 📌 Overview

This project is a Generative AI-based system that converts YouTube videos into concise summaries and structured blog articles.

## 🚀 Features

* Extracts transcript from YouTube videos
* Generates summary using Gemini (Google LLM)
* Converts summary into blog-style article
* Outputs content in Markdown format

## 🧠 Tech Stack

* Python
* LangChain
* Gemini API (Google Generative AI)
* yt-dlp (for transcript extraction)

## 🏗️ Project Pipeline

YouTube URL → Transcript → Summary → Article → Markdown Output

## ▶️ How to Run

1. Clone repository
2. Create virtual environment
3. Install dependencies:

pip install -r requirements.txt

4. Add your API key in `.env`:

GOOGLE_API_KEY=your_key_here

5. Run:

python app.py

## 📂 Output

* summary.txt → Generated summary
* article.md → Generated article

## 💡 Use Case

Content repurposing: Convert videos into blogs, notes, or documentation.

## 👨‍💻 Author

Saikumar (GenAI Engineer Aspirant)
