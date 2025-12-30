import requests
from datetime import datetime

url = "https://api.exchangerate-api.com/v4/latest/USD"

try:
    response = requests.get(url)
    data = response.json()
    kurs = data['rates']['IDR']
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    hasil = f"Laporan Tanggal {waktu}: 1 USD = Rp {kurs:,.2f}"
    
    # Bagian ini yang bakal bikin file otomatis
    with open("laporan_cuan.txt", "a") as file:
        file.write(hasil + "\n")
    
    print("Berhasil! Data sudah disimpan ke laporan_cuan.txt")

except Exception as e:
    print(f"Error: {e}")
