**🧠 YouTube Converter & Wikipedia CLI**
Oleh Kelompok 7

Program berbasis terminal untuk:
   - 🔍 Mencari ringkasan artikel Wikipedia (bahasa Indonesia)
   - 🎵 Mengunduh video YouTube sebagai MP3
   - 📺 Mengunduh video YouTube sebagai MP4

**🖥️ Fitur**
  1. Pencarian Wikipedia
      Masukkan judul artikel untuk menampilkan ringkasan, URL, dan daftar bagian artikel Wikipedia.
  2. YouTube ke MP3
      Unduh konten audio dari link video YouTube.
  3. YouTube ke MP4
      Unduh konten video dari link video YouTube.

**🔧 Instalasi**
  1. Clone repository:
     
```graphql
  git clone https://github.com/SyaiYesMom/YouTube-Converter-Wikipedia.git
  cd YouTube-Converter-Wikipedia
```

  2. Install dependencies:
      Pastikan kamu sudah memiliki Python 3 dan pip.
      Lalu jalankan:

```graphql
  pip install -r requirements.txt
```

**▶️ Cara Menjalankan**
Jalankan program utama:

      python main.py

**🗂️ Struktur File**

```graphql
├── main.py            # Menu utama program
├── wiki.py            # Modul pencarian Wikipedia
├── ytbmp3.py          # Modul pengunduh YouTube ke MP3
├── ytbmp4.py          # Modul pengunduh YouTube ke MP4
├── requirements.txt   # Daftar dependensi
└── README.md          # Dokumentasi
```

**🛠️ Contoh Output**

```markdown
===============================================
|                 Kelompok 7                  |
|        Konverter YouTube & WikiPedia        |
===============================================
 1. Pencarian Wikipedia
 2. YouTube ke MP3
 3. YouTube ke MP4
 4. Selesai
```

**✅ Dependencies**
Beberapa package yang kemungkinan digunakan (isi ```requirements.txt``` kamu bisa seperti ini):
