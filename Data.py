import pandas as pd

# Nomor 1: Membaca data dari file Excel
df = pd.read_excel(r'C:\Users\Dadan Ramdani\Documents\KULIAH\SMESTER 5\Pemograman Dasar\Tugas DataFrame\Data.xlsx')

# Menampilkan kolom yang dipilih
K = df[['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'satuan', 'tahun']]
print(K)
print()

# Nomor 2: Menghitung total produksi sampah di seluruh Kabupaten/Kota untuk tahun tertentu
tahun = int(input("Masukkan Tahun (2016-2023): "))
total_produksi = 0
for i, row in K.iterrows():
    if row['tahun'] == tahun:
        total_produksi += row['jumlah_produksi_sampah']

print(f"Total produksi sampah di seluruh Kabupaten/Kota di Jawa Barat untuk tahun {tahun} adalah: {total_produksi:.2f} ton.")
print()

# Nomor 3: Jumlahkan semua data sampah berdasarkan tahun
Semua_Tahun = {}

for i, row in K.iterrows():
    tahun = row['tahun']
    jumlah_sampah = row['jumlah_produksi_sampah']
    
    if tahun in Semua_Tahun:
        Semua_Tahun[tahun] += jumlah_sampah
    else:
        Semua_Tahun[tahun] = jumlah_sampah

print("Total produksi sampah per tahun:")
for tahun, total in Semua_Tahun.items():
    print(f"Total produksi sampah untuk tahun {tahun} adalah {total:.2f} ton.")
print()

# Nomor 4: Menjumlahkan semua data sampah berdasarkan kota/kabupaten per tahun
semua_kota = {}

for i, row in K.iterrows():
    kota = row['nama_kabupaten_kota']
    tahun = row['tahun']
    jumlah_sampah = row['jumlah_produksi_sampah']
    
    if tahun not in semua_kota:
        semua_kota[tahun] = {}

    if kota in semua_kota[tahun]:
        semua_kota[tahun][kota] += jumlah_sampah
    else:
        semua_kota[tahun][kota] = jumlah_sampah

print("Total produksi sampah per kota/kabupaten per tahun:")
for tahun, sampah in semua_kota.items():
    print(f"Tahun {tahun}:")
    for kota, total in sampah.items():
        print(f"  {kota}: {total:.2f} ton")

data_hasil = []
for tahun, kota_data in semua_kota.items():
    for kota, total in kota_data.items():
        data_hasil.append([tahun, kota, total])

# Export ek csv dan exel
hasil_df = pd.DataFrame(data_hasil, columns=['Kota/Kabupaten', 'Total Sampah (ton)', 'Tahun'])
hasil_df.to_csv(r'C:\Users\Dadan Ramdani\Documents\KULIAH\SMESTER 5\Pemograman Dasar\Tugas DataFrame\Hasil_Code.csv', index=False)
hasil_df.to_excel(r'C:\Users\Dadan Ramdani\Documents\KULIAH\SMESTER 5\Pemograman Dasar\Tugas DataFrame\Hasil_Code2.xlsx', index=False)
print("\nHasil telah diekspor ke file CSV: Hasil_Code.csv")
print("\nHasil telah diekspor ke file Excel: Hasil_Code2.xlsx")