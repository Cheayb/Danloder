<p align="center">
  <img src="icon.svg" alt="Social Video Downloader icon" width="120">
</p>

# Social Video Downloader

Small Python CLI to download videos from Instagram and Facebook, built on [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Install

```bash
pip install -r requirements.txt
```

Install [ffmpeg](https://ffmpeg.org/) too (needed to merge video/audio and for mp3 extraction).

## Usage

```bash
python downloader.py "https://www.instagram.com/reel/XXXX/"
python downloader.py URL1 URL2 -o my_videos
python downloader.py URL --audio
python downloader.py URL --cookies cookies.txt
```

## Notes

- For personal use only. Respect copyright and the platforms' terms of service.
- If a download fails, run `pip install -U yt-dlp`.

## License

MIT
