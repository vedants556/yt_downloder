import yt_dlp

def download_video(url, format_choice):
    ydl_opts = {
        'format': format_choice,
        'outtmpl': '%(title)s.%(ext)s',  # Save as title.extension
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convert to mp4 after download
        }],
        'quiet': False,  # Set to True to suppress output
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"Error downloading video: {e}")

def list_formats(url):
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)  # Get video info without downloading
        formats = info.get('formats', [])

        print("Available formats:")
        for idx, fmt in enumerate(formats):
            print(f"{idx + 1}: {fmt['format']} (Quality: {fmt.get('height', 'audio')}p)")

        return formats

def main():
    url = input("Enter the YouTube video URL: ")
    formats = list_formats(url)

    choice = int(input("Select a format number to download: ")) - 1
    if 0 <= choice < len(formats):
        format_choice = formats[choice]['format_id']
        download_video(url, format_choice)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
