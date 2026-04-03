# 🎥 YouTube Summarizer using Generative AI

## 📌 Overview

This project is a **Generative AI-based application** that converts YouTube videos into concise summaries and structured blog-style articles.

It extracts transcripts from YouTube videos, processes them using **Gemini (Google LLM)** via **LangChain**, and generates meaningful content in **Markdown and HTML formats**.

---

## 🏢 Internship

This project was developed as part of my internship at **Innomatics Research Labs**.

---

## 🚀 Features

* 🔗 Input: YouTube video URL
* 📥 Extracts transcript from video
* 🤖 Generates summary using Gemini AI
* 📝 Converts summary into structured blog article
* 📄 Outputs in Markdown and HTML formats
* 🌐 Streamlit-based UI for easy interaction
* ⬇️ Download summary and article

---

## 🧠 Tech Stack

* Python
* LangChain (latest syntax)
* Google Gemini API (gemini-2.5-flash)
* Streamlit (UI)
* yt-dlp (robust transcript extraction)
* youtube-transcript-api
* python-dotenv

---

## 🏗️ Project Pipeline

YouTube URL
↓
Transcript Extraction
↓
AI Summarization (Gemini)
↓
Article Generation
↓
Markdown / HTML Output

---

## 📁 Folder Structure

```
youtube_summarizer/
│
├── app.py
├── streamlit_app.py
├── .env
├── requirements.txt
├── README.md
├── .gitignore
│
├── modules/
│   ├── transcript.py
│   ├── summarizer.py
│   ├── article.py
│
├── outputs/
│   ├── summary.txt
│   ├── article.md
│   ├── article.html
│
└── venv/
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/your-username/youtube-summarizer-genai.git
cd youtube-summarizer-genai
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add API Key

Create a `.env` file:

```
GOOGLE_API_KEY=your_gemini_api_key
```

---

## ▶️ Run CLI Version

```
python app.py
```

---

## ▶️ Run UI Version

```
streamlit run streamlit_app.py
```

---

## 📂 Output Files

* `summary.txt` → AI-generated summary
* `article.md` → Blog article (Markdown)
* `article.html` → Blog article (HTML)

---

## 💡 Use Cases

* Content repurposing (video → blog)
* Quick learning from long videos
* Notes generation for students
* Documentation creation

---

## ⚠️ Challenges Faced

* YouTube transcript extraction is inconsistent
* Solved using **yt-dlp fallback mechanism**

---

## 🎯 Future Improvements

* Multi-language support
* Keyword extraction (SEO)
* Title generation
* Multi-video summarization

---

## 👨‍💻 Author

**Saikumar**
B.Tech CSE (AI & ML)
Aspiring GenAI Engineer 🚀

---
