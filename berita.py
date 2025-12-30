import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Target: Berita Terpopuler Kompas
url = "https://www.kompas.com/"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    response = requests.get(url, headers=headers, timeout=15)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Mencari judul berita di bagian terpopuler
    kumpulan_berita = []
    # Mengambil 5 judul berita pertama
    for berita in soup.select('.article__title', limit=5):
        judul = berita.text.strip()
        kumpulan_berita.append(judul)

    waktu_skrg = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Simpan ke CSV
    file_path = 'laporan_berita.csv'
    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        for b in kumpulan_berita:
            writer.writerow([waktu_skrg, b])

    print(f"✅ DataForge ID: Berhasil ambil {len(kumpulan_berita)} berita terbaru!")
    for i, j in enumerate(kumpulan_berita, 1):
        print(f"{i}. {j}")

except Exception as e:
    print(f"❌ Error: {e}")
