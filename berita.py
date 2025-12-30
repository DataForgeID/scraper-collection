import requests
from bs4 import BeautifulSoup

url = "https://www.detik.com/terpopuler"
headers = {'User-Agent': 'Mozilla/5.0'}

print("Sedang mengambil berita terpopuler...")

try:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Mencari judul berita di halaman terpopuler
    berita = soup.find_all('h3', class_='media__title')

    print("\n" + "="*40)
    print("       BERITA TERPOPULER HARI INI")
    print("="*40)

    for i, judul in enumerate(berita[:10], 1):
        print(f"{i}. {judul.text.strip()}")

    print("="*40)
    print("Script Berhasil! Data siap dipamerkan.")

except Exception as e:
    print(f"Gagal karena: {e}")
