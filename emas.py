import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# URL Harga Emas
url = "https://www.logammulia.com/id/harga-emas-hari-ini"

# Headers lengkap agar dianggap sebagai browser asli
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Mencari harga di dalam tabel yang mengandung kata '1 gr'
    harga = "Gagal mengambil data"
    rows = soup.find_all('tr')
    for row in rows:
        text = row.text.lower()
        if '1 gr' in text or '1 gram' in text:
            cols = row.find_all('td')
            if len(cols) >= 2:
                # Ambil kolom kedua (biasanya harga)
                harga = cols[1].text.strip().replace('\n', '')
                break

    waktu_skrg = datetime.now().strftime("%Y-%m-%d")
    jam_skrg = datetime.now().strftime("%H:%M:%S")

    # Simpan ke CSV
    with open('laporan_emas.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([waktu_skrg, jam_skrg, harga])

    print(f"✅ DataForge ID Berhasil!")
    print(f"💰 Harga 1 Gram: {harga}")
    print(f"🕒 Jam: {jam_skrg}")

except Exception as e:
    print(f"❌ Error: {e}")
