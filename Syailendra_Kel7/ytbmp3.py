import os
from yt_dlp import YoutubeDL

def download_youtube_mp3(url, output_path="downloads/mp3"):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            title = info_dict.get('title', 'Tidak Diketahui')
            channel = info_dict.get('uploader', 'Tidak Diketahui')
            duration = info_dict.get('duration', 'Tidak Diketahui')
            filesize = info_dict.get('filesize', 'Tidak Diketahui')

            if filesize != 'Tidak Diketahui':
                filesize_mb = round(filesize / (1024 * 1024), 2)
                filesize_str = f"{filesize_mb} Mb"
            else:
                filesize_str = 'Tidak Diketahui'

            if duration != 'Tidak Diketahui':
                minutes = duration // 60
                seconds = duration % 60
                duration_str = f"{minutes}:{seconds:02d}"
            else:
                duration_str = 'Tidak Diketahui'

            print("====================================================================")
            print(f"Tittle  : {title}")
            print(f"Channel : {channel}")
            print(f"Durasi  : {duration_str}")
            print(f"Ukuran  : {filesize_str}")
            print(f"Url     : {url}")
            print("====================================================================")

            ydl.download([url])

        print("Audio berhasil diunduh dalam format MP3.")
        return title
    except Exception as e:
        print("Terjadi kesalahan:", e)
        return None

if __name__ == "__main__":
    url = input("Masukkan URL YouTube: ")
    download_youtube_mp3(url)
