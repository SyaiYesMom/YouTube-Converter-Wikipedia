import os
from yt_dlp import YoutubeDL

def download_youtube_mp4(url, output_path="downloads/mp4"):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
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
                if filesize < 1024 * 1024:
                    filesize_str = f"{round(filesize / 1024, 2)} KB"
                elif filesize < 1024 * 1024 * 1024:
                    filesize_str = f"{round(filesize / (1024 * 1024), 2)} MB"
                else:
                    filesize_str = f"{round(filesize / (1024 * 1024 * 1024), 2)} GB"
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

        print("Video berhasil diunduh dalam format MP4.")
        return title
    except Exception as e:
        print("Terjadi kesalahan:", e)
        return None

if __name__ == "__main__":
    url = input("Masukkan URL YouTube: ")
    download_youtube_mp4(url)
