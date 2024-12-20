from database.connection import get_db_connection

class CarModel:
    def __init__(self, model, brand_id):
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Model must be a non-empty string.")
        if not isinstance(brand_id, int):
            raise ValueError("Brand ID must be an integer.")

        self._model = model
        self._brand_id = brand_id

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO car_models (model, brand_id) VALUES (?, ?)",
                (model, brand_id),
            )
            self._id = cursor.lastrowid

    @property
    def model(self):
        return self._model

    @property
    def brand_id(self):
        return self._brand_id

    @staticmethod
    def fetch_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM car_models")
            return cursor.fetchall()

    def __repr__(self):
        return f"<CarModel {self.model}>"
