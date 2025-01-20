import os
import time
import platform
from colorama import Fore, Style
from wiki import WikipediaFetcher
from ytbmp3 import download_youtube_mp3
from ytbmp4 import download_youtube_mp4
from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

TOKEN = ('6348811142:AAHsXhnD1yMTELx56tEfKkhCOA9OHPDJkg0')

if not TOKEN:
    raise ValueError("Token tidak ditemukan! Pastikan file 'API.env' berisi variabel 'TELEGRAM_TOKEN'.")

BOT_USERNAME: Final = '@SyaiAi_bot'

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    log_user_info(user, "start command")
    
    await update.message.reply_text(
        "Halo, saya SyaiAi! 👋\n"
        "Saya dapat membantu Anda dengan beberapa hal:\n\n"
        "   | Pencarian Wikipedia\n"
        "   | YouTube ke MP3\n"
        "   | YouTube ke MP4\n\n"
        "Pilih salah satu opsi di bawah untuk mulai!",
        reply_markup=InlineKeyboardMarkup([[ 
            InlineKeyboardButton("1. Pencarian Wikipedia", callback_data='1')
        ], [
            InlineKeyboardButton("2. YouTube ke MP3", callback_data='2')
        ], [
            InlineKeyboardButton("3. YouTube ke MP4", callback_data='3')
        ]])
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    log_user_info(user, "help command")
    
    await update.message.reply_text(
        "Untuk menggunakan bot ini ketik /start, lalu pilih salah satu perintah berikut:\n"
        "   | Pencarian Wikipedia\n"
        "   | YouTube ke MP3\n"
        "   | YouTube ke MP4"
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == '1':
        await query.edit_message_text("Masukkan judul halaman yang ingin dicari di Wikipedia: 📚")
        context.user_data['mode'] = 'wikipedia'
    elif query.data == '2':
        await query.edit_message_text("Masukkan URL YouTube untuk diunduh sebagai MP3: 🎵")
        context.user_data['mode'] = 'mp3'
    elif query.data == '3':
        await query.edit_message_text("Masukkan URL YouTube untuk diunduh sebagai MP4: 🎥")
        context.user_data['mode'] = 'mp4'

import os

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text: str = update.message.text.strip()

    if context.user_data.get('mode') == 'wikipedia':
        await wikipedia_search(update, text)
    elif context.user_data.get('mode') == 'mp3':
        clear_screen()
        title = download_youtube_mp3(text)
        if title:
            file_path = os.path.join("downloads/mp3", f"{title}.mp3")
            if os.path.exists(file_path):
                await update.message.reply_text(f"{title}.mp3 berhasil diunduh.")
                await update.message.reply_audio(audio=open(file_path, 'rb'))
            else:
                await update.message.reply_text("File tidak ditemukan. Gagal mengunduh MP3. Lokasi", f"{file_path}")
        else:
            await update.message.reply_text("Gagal mengunduh MP3.")

    elif context.user_data.get('mode') == 'mp4':
        clear_screen()
        title = download_youtube_mp4(text)
        if title:
            file_path = os.path.join("downloads", "mp4", f"{title}.mp4")
            if os.path.exists(file_path):
                await update.message.reply_text(f"{title}.mp4 berhasil diunduh.")
                await update.message.reply_video(video=open(file_path, 'rb'))
            else:
                await update.message.reply_text("File tidak ditemukan. Gagal mengunduh MP4.")
        else:
            await update.message.reply_text("Gagal mengunduh MP4.")
async def wikipedia_search(update: Update, query: str):
    try:
        fetcher = WikipediaFetcher()
        result = fetcher.get_wikipedia_page(query, 'id')
        
        if isinstance(result, dict):
            await update.message.reply_text(
                f"Judul Halaman : {result['title']}\n"
                f"\nRingkasan :\n {result['summary']}\n"
                f"\nReferensi :\n {result['full_url']}"
            )
        else:
            await update.message.reply_text(result)
    except Exception as e:
        await update.message.reply_text(f"Gagal mencari di Wikipedia: {str(e)}")

def log_user_info(user, action):
    username = user.username
    user_id = user.id
    print(f":User  {username}, ID: {user_id}, Action: {action}")

if __name__ == "__main__":
    print('Starting Bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    app.run_polling()
