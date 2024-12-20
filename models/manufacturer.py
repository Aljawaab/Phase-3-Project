from database.connection import get_db_connection

class Manufacturer:
    def __init__(self, brand):
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Brand must be a non-empty string.")

        self._brand = brand

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO manufacturers (brand) VALUES (?)", (brand,))
            self._id = cursor.lastrowid

    @property
    def brand(self):
        return self._brand

    @staticmethod
    def fetch_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM manufacturers")
            return cursor.fetchall()

    def __repr__(self):
        return f"<Manufacturer {self.brand}>"