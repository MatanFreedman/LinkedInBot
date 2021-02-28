import sqlite3
from pathlib import Path


class DBConnection:
    data_path = "data/"
    conn = sqlite3.connect(data_path + 'linkedin_data.db')
    cur = conn.cursor()

    def __init__(self):
        self.initialize()

    def initialize(self):
        """Check if DB exists, create table if it doesnt
        """
        self.cur.execute("""CREATE TABLE IF NOT EXISTS positions(
            id INTEGER PRIMARY KEY NOT NULL,
            position TEXT,
            company TEXT,
            location TEXT,
            details TEXT,
            date INT
            );
        """)
        self.conn.commit()

    def close(self):
        """Close DB connection"""
        self.conn.close()

    def is_duplicate(self, data):
        """Check if data is duplicate

        Parameters
        ---------
        data : tuple : (position, company, location, details) - all strings

        Returns : Boolean if duplicate
        """
        # check DB for duplicate:
        self.cur.execute("""
            SELECT *
            FROM positions
            WHERE position = ?
            AND company = ?
            AND location = ?
            AND details = ?
            ;
            """, data)

        if self.cur.fetchone() is None:
            return False 
        else:
            return True


    def insert_position(self, data):
        """Inserts into DB.

        Parameters
        ---------
        data : tuple : (position, company, location, details) - all strings
        """
        self.cur.execute("""
            INSERT INTO positions(position, company, location, details, date) VALUES (?, ?, ?, ?, date('now'))
            """, data)
        self.conn.commit()
