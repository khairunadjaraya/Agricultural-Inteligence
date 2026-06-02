import pandas as pd
import sqlite3 as sql

# Membuat koneksi database
def connect_db():
    conn = sql.connect("pertanian.db")
    return conn

# Membuat tabel produksi_padi
def save_to_db(df, name_file):
    conn = connect_db()
    cursor = conn.cursor()
    df.to_sql(
        name_file,
        conn,
        if_exists="replace",
        index=False
    )
    conn.close()
    print(f"Data berhasil disimpan ke tabel {name_file}!")

def read_from_db(name_file):
    conn = connect_db()
    cursor = conn.cursor()
    df = pd.read_sql(f"SELECT * FROM {name_file}", conn)
    conn.close()
    return df   

def query_by_provinsi (provinsi):
    conn = connect_db()
    cursor = conn.cursor()
    query = f"""SELECT * FROM produksi_padi
    WHERE provinsi = '{provinsi}'"""
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def query_by_column(column, value):
    allowed_columns = ["provinsi", "tahun"]

    if column not in allowed_columns:
        raise ValueError("Kolom tidak valid")

    conn = connect_db()

    try:
        query = f"SELECT * FROM produksi_padi WHERE {column} = ?"
        df = pd.read_sql(query, conn, params=(value,))
    finally:
        conn.close()

    return df

def add_data_to_db(provinsi, tahun, produksi_ton, curah_hujan_mm):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO produksi_padi (
        provinsi,
        tahun,
        produksi_ton,
        curah_hujan_mm
    )
    VALUES (?, ?, ?, ?)
    """, (provinsi, tahun, produksi_ton, curah_hujan_mm))
    conn.commit()
    conn.close()
    print(f"Data berhasil ditambahkan ke tabel produksi_padi!")

def select_all_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM produksi_padi
    """)
    result = cursor.fetchall()
    conn.close()
    return result

# Melihat daftar tabel
def show_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT name FROM sqlite_master
    WHERE type='table';
    """)
    tables = cursor.fetchall()
    conn.close()
    return tables
    
def show_columns(table_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    conn.close()
    return columns

def update_produksi(provinsi, produksi_ton):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE produksi_padi
    SET produksi_ton = ?
    WHERE provinsi = ?
    """, (produksi_ton, provinsi))
    conn.commit()
    conn.close()
    print(f"Data produksi untuk provinsi {provinsi} berhasil diperbarui!")

def delete_data(provinsi):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    DELETE FROM produksi_padi
    WHERE provinsi = ?
    """, (provinsi,))
    conn.commit()
    conn.close()
    print(f"Data untuk provinsi {provinsi} berhasil dihapus!")

def sum_produksi_by_provinsi():
    conn = connect_db()
    cursor = conn.cursor()
    query = f"""
    SELECT provinsi, SUM(produksi_kg)
    FROM produksi_padi
    GROUP BY provinsi"""
    df = pd.read_sql(query, conn)
    conn.close()
    return df

