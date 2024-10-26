import os
import yt_dlp

def check_netrc():
    netrc_path = os.path.expanduser("~/.netrc")
    
    # Check if .netrc file exists
    if os.path.exists(netrc_path):
        print(f".netrc file found at: {netrc_path}")
        with open(netrc_path, 'r') as file:
            content = file.read()
            print("Contents of .netrc:")
            print(content)
            
            # Check for proper formatting
            if "machine youtube.com" in content:
                print("Found credentials for youtube.com in .netrc.")
            else:
                print("No credentials for youtube.com found in .netrc.")
    else:
        print("No .netrc file found. Please create one for authentication.")

def download_video(url, format_choice):
    print(f"Attempting to download video from URL: {url} with format: {format_choice}")
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
            print("Download completed successfully.")
        except Exception as e:
            print(f"Error downloading video: {e}")

def list_formats(url):
    print(f"Fetching formats for URL: {url}")
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)  # Get video info without downloading
        formats = info.get('formats', [])

        print("Available formats:")
        for idx, fmt in enumerate(formats):
            print(f"{idx + 1}: {fmt['format']} (Quality: {fmt.get('height', 'audio')}p)")

        return formats

def main():
    check_netrc()  # Check and debug .netrc file

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
