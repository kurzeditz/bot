import requests
import time
from datetime import datetime

WEBHOOK_URL = "https://discord.com/api/webhooks/1458765762444394496/W17Ailw7x0Wy0O5ydM47CZkjBpvZqNeJnjbyKXOsNYWEQYB3lOov0NGDxM3gmnOTVZPV"
ROLE_ID = "1458728903660273747"

pesan = input("Isi pesan notifikasi: ")

data = {
    "content": f"<@&{ROLE_ID}>",
    "embeds": [
        {
            "title": "📢 Informasi",
            "description": pesan,
            "color": 0x00ffcc
        }
    ]
}

while True:
    try:
        r = requests.post(WEBHOOK_URL, json=data)
        if r.status_code in [200, 204]:
            print(f"[{datetime.now()}] ✅ Terkirim")
        else:
            print(f"[{datetime.now()}] ❌ Gagal | {r.status_code}")
    except Exception as e:
        print("❌ Error:", e)

    # delay 5 detik
    time.sleep(5)
