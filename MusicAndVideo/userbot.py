import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Minggu", 60 * 60 * 24 * 7),
    ("Hari", 60 * 60 * 24),
    ("Jam", 60 * 60),
    ("Menit", 60),
    ("Detik", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>🚀 Ping</b> `{delta_ping * 1000:.3f} ms` \n<b>⏳ İşləmə vaxtı</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `0%`")
    await loli.edit("██▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `20%`")
    await loli.edit("████▒▒▒▒▒▒▒▒▒▒▒▒ `30%`")
    await loli.edit("██████▒▒▒▒▒▒▒▒▒▒ `45%`")
    await loli.edit("████████▒▒▒▒▒▒▒▒ `60%`")
    await loli.edit("██████████▒▒▒▒▒▒ `70%`")
    await loli.edit("████████████▒▒▒▒ `80%`")
    await loli.edit("██████████████▒▒ `95%`")
    await loli.edit("████████████████ `100%`")
    await loli.edit("**✅ Userbot yenidən işə salındı...**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["start"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>👋 Salam {m.from_user.mention}!

🛠 Kömək menyusu👇

⚡ **Bütün qrup üzvləri üçün**
• {HNDLR}play [mahnı adı | link youtube | mahnı faylına yanıt] - mahnını səslidə oxudar
• {HNDLR}vplay [video adı | link youtube | video faylına yanıt] - videonu səslidə göstərər 
• {HNDLR}playlist və ya {HNDLR}siyahi siyahını göstərər 
• {HNDLR}ping - bot statusu
• {HNDLR}help - kömək
• {HNDLR}song mahnı yükləyər
• {HNDLR}vsong və ya {HNDLR}video video yükləyər
• {HNDLR}ses mətni səsə çevirər
• {HNDLR}q və ya {HNDLR}stiker mətni Stikerə çevirər

⚡ **Yalnız adminlər👇**
• {HNDLR}resume - davam etdirər
• {HNDLR}pause - dayandırar
• {HNDLR}skip - növbətiyə keçər
• {HNDLR}end - sonlandırar</b>
"""
    await m.reply(HELP)


@Client.on_message(filters.command(["sexsi"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋 Hallo {m.from_user.mention}!

🐍 Music Dan Video Player UserBot

🔰 Telegram UserBot Untuk Memutar Lagu Dan Video Di Obrolan Suara Telegram.

👩‍💻 Dipersembahkan Oleh 
• [Gen Support](https://t.me/GenXProject_support)
• [PyTgCalls](https://github.com/pytgcalls/pytgcalls)
• [Pyrogram](https://github.com/pyrogram/pyrogram)


📝 Persyaratan
• Python 3.8+
• FFMPEG
• Nodejs v16+

🛠 MENU BANTUAN

⚡ PERINTAH UNTUK SEMUA ORANG
• `{HNDLR}play [judul lagu | link youtube | balas file audio]` - untuk memutar lagu
• `{HNDLR}vplay [judul video | link youtube | balas file video]` - untuk memutar video
• `{HNDLR}playlist` untuk melihat daftar putar
• `{HNDLR}ping` - untuk cek status
• `{HNDLR}help` - untuk melihat daftar perintah

⚡ PERINTAH UNTUK SEMUA ADMIN
• `{HNDLR}resume` - untuk melanjutkan pemutaran lagu atau video
• `{HNDLR}pause` - untuk untuk menjeda pemutaran lagu atau video
• `{HNDLR}skip` - untuk melewati lagu atau video
• `{HNDLR}end` - untuk mengakhiri pemutaran

🥜 Deployment Userbot
💜 Heroku

 [𝗗𝗘𝗣𝗟𝗢𝗬 𝗞𝗘 𝗛𝗘𝗥𝗢𝗞𝗨](https://heroku.com/deploy?template=https://github.com/fjgaming212/Userbot-Music)

📚 Variabel Yang Dibutuhkan
• `API_ID` - Dapatkan Dari [my.telegram.org](https://my.telegram.org)
• `API_HASH` - Dapatkan Dari [my.telegram.org](https://my.telegram.org)
• `SESSION` - Sesi String Pyrogram. Dapatkan String Dari [Sini](https://replit.com/@fjgaming212/StringSession#main.py)
• `SUDO_USER` - ID Akun Telegram Yang Digunakan Sebagai Admin
• `HNDLR` - Handler untuk bot mu


❤️‍🔥 KREDIT 
• [Fariz](https://github.com/fjgaming212)
• [Skyzo](https://github.com/ridho17-ind)
• [Tomi](https://github.com/XtomiSN)
• [Dan](https://github.com/delivrance) Untuk [Pyrogram](https://github.com/pyrogram/pyrogram)
• [Laky](https://github.com/Laky-64) Untuk [PyTgCalls](https://github.com/pytgcalls/pytgcalls)</b>
"""
    await m.reply(REPO, disable_web_page_preview=True)
