import re
import yt_dlp


def extract_video_id(url: str) -> str:
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)

    if not match:
        raise ValueError("Invalid YouTube URL")

    return match.group(1)


def get_transcript(url: str) -> str:
    import yt_dlp
    import requests
    import re

    try:
        ydl_opts = {
            'quiet': True,
            'skip_download': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        # Try both types of captions
        subtitles = info.get("subtitles", {})
        auto_captions = info.get("automatic_captions", {})

        all_captions = subtitles if subtitles else auto_captions

        if not all_captions:
            raise Exception("No captions available")

        # Prefer English, else first available language
        if "en" in all_captions:
            lang = "en"
        else:
            lang = list(all_captions.keys())[0]

        subtitle_url = all_captions[lang][0]["url"]

        # Fetch subtitle XML
        response = requests.get(subtitle_url)
        xml_data = response.text

        # Remove XML tags
        clean_text = re.sub('<[^<]+?>', '', xml_data)

        return clean_text.strip()

    except Exception as e:
        raise Exception(f"Transcript error: {str(e)}")