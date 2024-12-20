from database.connection import get_db_connection

def create_tables():
    """Create all necessary tables if they don't exist."""
with get_db_connection() as conn:
        cursor = conn.cursor()

        sql_create_owners_table = """CREATE TABLE IF NOT EXISTS owners (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL
                                );"""

        sql_create_manufacturers_table = """CREATE TABLE IF NOT EXISTS manufacturers (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        brand TEXT NOT NULL
                                    );"""

        sql_create_car_models_table = """CREATE TABLE IF NOT EXISTS car_models (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        model TEXT NOT NULL,
                                        brand_id INTEGER NOT NULL,
                                        FOREIGN KEY (brand_id) REFERENCES manufacturers(id) ON DELETE CASCADE
                                    );"""

        sql_create_car_registrations_table = """CREATE TABLE IF NOT EXISTS car_registrations (
                                            registration_number TEXT PRIMARY KEY,
                                            owner_id INTEGER,
                                            model_id INTEGER,
                                            FOREIGN KEY (owner_id) REFERENCES owners(id),
                                            FOREIGN KEY (model_id) REFERENCES car_models(id)
                                        );"""

cursor.execute(sql_create_owners_table)
cursor.execute(sql_create_manufacturers_table)
cursor.execute(sql_create_car_models_table)
cursor.execute(sql_create_car_registrations_table)

