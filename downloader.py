#!/usr/bin/env python3
"""Download public Instagram / Facebook videos using yt-dlp."""
import argparse
import sys
from urllib.parse import urlparse

try:
    import yt_dlp
except ImportError:
    sys.exit("yt-dlp is not installed. Run: pip install -r requirements.txt")

ALLOWED_HOSTS = (
    "instagram.com",
    "facebook.com",
    "fb.watch",
    "fb.com",
)


def is_supported(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower()
    return any(host == h or host.endswith("." + h) for h in ALLOWED_HOSTS)


def download(url: str, out_dir: str, audio_only: bool, cookies: str | None) -> bool:
    opts = {
        "outtmpl": f"{out_dir}/%(uploader)s - %(title).80s [%(id)s].%(ext)s",
        "noplaylist": True,
        "quiet": False,
        "restrictfilenames": False,
    }
    if audio_only:
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}
        ]
    else:
        opts["format"] = "bv*+ba/b"
        opts["merge_output_format"] = "mp4"
    if cookies:
        opts["cookiefile"] = cookies

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        return True
    except yt_dlp.utils.DownloadError as e:
        print(f"[!] Failed: {url}\n    {e}", file=sys.stderr)
        return False


def main() -> int:
    p = argparse.ArgumentParser(description="Instagram & Facebook video downloader")
    p.add_argument("urls", nargs="+", help="One or more video URLs")
    p.add_argument("-o", "--output", default="downloads", help="Output folder")
    p.add_argument("-a", "--audio", action="store_true", help="Audio only (mp3)")
    p.add_argument("-c", "--cookies", help="cookies.txt file (for content that needs login)")
    args = p.parse_args()

    ok = True
    for url in args.urls:
        if not is_supported(url):
            print(f"[!] Unsupported link: {url}", file=sys.stderr)
            ok = False
            continue
        ok = download(url, args.output, args.audio, args.cookies) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
