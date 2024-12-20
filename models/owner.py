from database.connection import get_db_connection

class Owner:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")

        self._name = name

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO owners (name) VALUES (?)", (name,))
            self._id = cursor.lastrowid

    @property
    def name(self):
        return self._name

    @staticmethod
    def fetch_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM owners")
            return cursor.fetchall()
    
    @staticmethod
    def fetch_with_related_data():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    o.id AS owner_id, 
                    o.name AS owner_name, 
                    cr.registration_number, 
                    cm.model AS car_model, 
                    m.brand AS manufacturer
                FROM owners o
                LEFT JOIN car_registrations cr ON o.id = cr.owner_id
                LEFT JOIN car_models cm ON cr.model_id = cm.id
                LEFT JOIN manufacturers m ON cm.brand_id = m.id
            """)
            results = cursor.fetchall()
        return results

    @staticmethod
    def delete_owner(owner_id):
        """
        Deletes an owner and all related data from the database, including 
        their car registrations and car models.

        Args:
            owner_id (int): The ID of the owner to delete.

        Returns:
            str: Confirmation message.
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()

            # Fetch all car models associated with the owner's registrations
            cursor.execute("""
                SELECT DISTINCT cm.id
                FROM car_models cm
                INNER JOIN car_registrations cr ON cm.id = cr.model_id
                WHERE cr.owner_id = ?
            """, (owner_id,))
            car_model_ids = [row[0] for row in cursor.fetchall()]

            # Delete related car registrations
            cursor.execute("DELETE FROM car_registrations WHERE owner_id = ?", (owner_id,))
            
            # Delete car models associated with the owner's registrations
            for model_id in car_model_ids:
                cursor.execute("DELETE FROM car_models WHERE id = ?", (model_id,))
            
            # Delete the owner
            cursor.execute("DELETE FROM owners WHERE id = ?", (owner_id,))
            conn.commit()

            return f"Owner with ID {owner_id}, their registrations, and associated car models deleted successfully."

    def __repr__(self):
        return f"<Owner {self.name}>"
