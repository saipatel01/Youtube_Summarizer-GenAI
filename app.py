from modules.transcript import get_transcript
from modules.summarizer import generate_summary
from modules.article import generate_article


def main():
    print("=== YouTube Summarizer (Gemini) ===\n")

    url = input("Enter YouTube URL: ").strip()

    if not url:
        print("❌ Please enter a valid URL")
        return

    try:
        # Step 1: Get transcript
        print("\n📥 Fetching transcript...")
        transcript = get_transcript(url)
        print("✅ Transcript fetched!\n")

        # Step 2: Generate summary
        print("🤖 Generating summary...\n")
        summary = generate_summary(transcript)

        print("📌 SUMMARY:\n")
        print(summary)

        # Save summary
        with open("outputs/summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)

        print("\n💾 Summary saved in outputs/summary.txt")

        # Step 3: Generate article
        print("\n📝 Generating article...\n")
        article = generate_article(summary)

        print("📰 ARTICLE:\n")
        print(article)

        # Save article
        with open("outputs/article.md", "w", encoding="utf-8") as f:
            f.write(article)

        print("\n💾 Article saved in outputs/article.md")
        
        # Save as HTML
        html_content = f"<html><body><pre>{article}</pre></body></html>"

        with open("outputs/article.html", "w", encoding="utf-8") as f:
         f.write(html_content)

        print("💾 Article also saved as outputs/article.html")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()