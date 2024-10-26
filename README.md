# 🎥 YouTube Video Downloader

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](#)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&label=Contributions&colorA=red&colorB=black)](#)

This project is a command-line application that allows users to download YouTube videos in various formats. It leverages the powerful `yt-dlp` library to provide a seamless downloading experience.

## 🌟 Features

- Download YouTube videos in multiple formats:
  - Select video quality and format
  - Convert videos to MP4 after downloading
- List available video formats and qualities before downloading
- User-friendly command-line interface for easy interaction
- Support for `.netrc` authentication for downloading private or age-restricted videos
- Debug statements to help troubleshoot issues with the application

## 🛠️ Technologies Used

- Python
- yt-dlp
- FFmpeg (for video conversion)

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/vedants556/yt_downloder.git
   ```

2. Install the required dependencies:
   ```bash
   pip install yt-dlp
   ```

3. Ensure FFmpeg is installed on your system.

4. Create a `.netrc` file in your home directory for authentication (if needed):
   ```plaintext
   machine youtube.com
   login your_username
   password your_password
   ```
   Make sure to set the permissions for the `.netrc` file:
   ```bash
   chmod 600 ~/.netrc
   ```

5. Run the application:
   ```bash
   python main.py
   ```

6. Follow the prompts to download your desired video.

## 📊 How It Works

1. Users input the YouTube video URL through the command line.
2. The application checks for the `.netrc` file and displays relevant debug information.
3. It fetches available formats and displays them.
4. Users select the desired format by number.
5. The chosen video is downloaded and converted to MP4 format.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](#) if you want to contribute.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Vedant  
- GitHub: [@vedants556](https://github.com/vedants556)  
- LinkedIn: [vedant-shelar](https://www.linkedin.com/in/vedant-shelar-41923724b)

## 🙏 Acknowledgements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for the downloading capabilities
- [FFmpeg](https://ffmpeg.org/) for video conversion

---

If you find this project useful, please consider giving it a star ⭐️ to show your support!

---
