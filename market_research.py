import requests
from bs4 import BeautifulSoup
import csv
import re
from datetime import datetime

# Kumpulan User-Agent agar scraper terlihat seperti manusia, bukan robot
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

def get_live_exchange_rate():
    try:
        url_api = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url_api, timeout=10)
        return response.json()['rates']['IDR']
    except:
        return 16000

def scrape_market_pro():
    kurs_sekarang = get_live_exchange_rate()
    rating_map = {"One": "⭐", "Two": "⭐⭐", "Three": "⭐⭐⭐", "Four": "⭐⭐⭐⭐", "Five": "⭐⭐⭐⭐⭐"}
    
    # Penamaan file otomatis berdasarkan tanggal: riset_30_Dec_2025.csv
    nama_file = datetime.now().strftime("riset_%d_%b_%Y.csv")
    url_target = "http://books.toscrape.com/catalogue/category/books/science_22/index.html"
    
    try:
        print(f"💎 DataForge ID PRO | Kurs: Rp {kurs_sekarang:,.0f}")
        response = requests.get(url_target, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('article', class_='product_pod')
        
        with open(nama_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Nama Barang', 'Harga (IDR)', 'Rating', 'Update Terakhir'])
            
            for item in products:
                nama = item.h3.a['title']
                
                # Scrape Rating
                tag_rating = item.find('p', class_='star-rating')
                rating_class = tag_rating['class'][1]
                rating_visual = rating_map.get(rating_class, "No Rating")
                
                # Scrape & Convert Harga
                harga_raw = item.find('p', class_='price_color').text
                harga_clean = re.sub(r'[^\d.]', '', harga_raw)
                
                if harga_clean:
                    harga_idr = int(float(harga_clean) * kurs_sekarang)
                    format_rupiah = f"Rp {harga_idr:,}".replace(',', '.')
                    
                    waktu_skrg = datetime.now().strftime("%H:%M:%S")
                    writer.writerow([nama, format_rupiah, rating_visual, waktu_skrg])
                    print(f"🚀 [SAVED] {nama[:20]}... | {format_rupiah} | {rating_visual}")

        print(f"\n✅ DATABASE UPDATE: {nama_file}")
        print("💡 Tips: Kirim file ini ke klien sebagai laporan harian.")

    except Exception as e:
        print(f"❌ Critical Error: {e}")

if __name__ == "__main__":
    scrape_market_pro()
