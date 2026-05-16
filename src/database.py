import pandas as pd
import sqlite3 as sql

data = {
    "provinsi": ["Jawa Barat", "Jawa Tengah", "Jawa Timur"],
    "tahun": [2024, 2024, 2024],
    "produksi_ton": [9500000, 8700000, 12000000],
    "curah_hujan_mm": [1500, 1200, 1800]
}

df = pd.DataFrame(data)

print(df)

# Membuat koneksi database
conn = sql.connect("pertanian.db")

# Membuat object cursor
cursor = conn.cursor()

# Membuat tabel produksi_padi
df.to_sql(
    "produksi_padi",
    conn,
    if_exists="replace",
    index=False
)

query = """SELECT provinsi, produksi_ton 
FROM produksi_padi
WHERE produksi_ton > 9000000
ORDER BY produksi_ton DESC"""

df_hasil = pd.read_sql(query, conn)
print(df_hasil)

# Menambahkan data
cursor.execute("""
INSERT INTO produksi_padi (
    provinsi,
    tahun,
    produksi_ton,
    curah_hujan_mm
)
VALUES (?, ?, ?, ?)
""", ("Jawa Tengah", 2022, 8000000, 1200))


# Melihat daftar tabel
cursor.execute("""
SELECT name FROM sqlite_master
WHERE type='table';
""")

tables = cursor.fetchall()

#print(tables)

cursor.execute("""
UPDATE produksi_padi
SET produksi_ton = 9000000
WHERE provinsi = 'Jawa Tengah'
""")

cursor.execute("""
               DELETE FROM produksi_padi
               WHERE provinsi = 'Jawa Tengah'
               """)

cursor.execute("""
SELECT * FROM produksi_padi
""")

result = cursor.fetchall()
#print(result)

cursor.execute("""SELECT provinsi, produksi_ton
FROM produksi_padi
""")

output = cursor.fetchall()
#print(output)

cursor.execute("""
SELECT provinsi, SUM(produksi_ton)
FROM produksi_padi
GROUP BY provinsi
""")

hasil = cursor.fetchall()

#print(hasil)

# Menyimpan perubahan
conn.commit()

# Menutup koneksi
conn.close()

print("Database dan tabel berhasil dibuat!")