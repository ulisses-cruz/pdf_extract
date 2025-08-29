import sqlite3
import datetime

from src.settings import Settings
from src.application.dtos.save_data import SaveData




class ExtractedDataRepo:
    def __init__(self):
        self.conn = sqlite3.connect(Settings.DATABASE_URL)

    def save_data(self, dto: SaveData) -> datetime.datetime:
        cursor = self.conn.cursor()
        now = datetime.datetime.now()
        cursor.execute("""
        INSERT INTO extracted_data (case_id, pdf_url, create_at, data)
        VALUES (?, ?, ?, ?)
        """, 
        (dto.case_id, dto.pdf_url.encoded_string(), now, dto.data))
        self.conn.commit()
        return now


    def create_table(self): 
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS extracted_data (
            case_id TEXT,
            pdf_url TEXT,
            create_at DATETIME,
            data TEXT
        )
        """)
        self.conn.commit()

