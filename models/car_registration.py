from database.connection import get_db_connection

class CarRegistration:
    def __init__(self, registration_number, owner_id, model_id):
        if not isinstance(registration_number, str) or not registration_number.strip():
            raise ValueError("Registration number must be a non-empty string.")
        if not isinstance(owner_id, int):
            raise ValueError("Owner ID must be an integer.")
        if not isinstance(model_id, int):
            raise ValueError("Model ID must be an integer.")

        self._registration_number = registration_number
        self._owner_id = owner_id
        self._model_id = model_id

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO car_registrations (registration_number, owner_id, model_id) VALUES (?, ?, ?)",
                (registration_number, owner_id, model_id),
            )

    @property
    def registration_number(self):
        return self._registration_number

    @staticmethod
    def fetch_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM car_registrations")
            return cursor.fetchall()

    def __repr__(self):
        return f"<CarRegistration {self.registration_number}>"