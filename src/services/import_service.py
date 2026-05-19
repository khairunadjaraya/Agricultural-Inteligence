from .cleaning_service import clean_data
from script.database import save_to_db, read_from_db
import pandas as pd
import sqlite3 as sql

def import_data(nama_tabel):
    data = clean_data()
    save_to_db(data, nama_tabel)
    return data