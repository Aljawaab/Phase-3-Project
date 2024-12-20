#### Car Registration System Built with Python and SQLite, DEC 20 2024
#### By **Abdul Aljawaab**

## Description 
The **Car Registration System** is a Command-Line Interface (CLI) application that allows users to manage car ownership information. Users can add owners, manufacturers, car models, register cars, delete owners and  view all owners and related data. The system uses an SQLite database for persistent data storage.

## How to Use
### Requirements
* Python 3.6 or higher installed on your system
* Pipenv for dependency management

### Setup Instructions
1. **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. **Install Dependencies**:
    ```bash
    pipenv install
    ```

3. **Activate the Virtual Environment**:
    ```bash
    pipenv shell
    ```

4. **Run the Application**:
    ```bash
    python app.py
    ```

## Features
- **Add Owner**: Add a new owner to the system.
- **Add Manufacturer**: Add a new car manufacturer.
- **Add Car Model**: Add a new car model and link it to a manufacturer.
- **Register Car**: Register a car by linking it to an owner and a car model.
- **View All Registrations**: Display all car registrations along with related owner and model data.
- **Delete Owner**: Deletes all car registrations along with related owner and model data.
- **Exit**: Close the application.

## Technologies Used
- **Python**: Main programming language.
- **SQLite**: Database for data persistence.
- **Pipenv**: For virtual environment and dependency management.

## Navigation Instructions
When you run the application, you will see a main menu:

```
Car Registration System
1. Add Owner
2. Add Manufacturer
3. Add Car Model
4. Register Car
5. View All Registrations
6. Exit
```

### **1. Add Owner**
- Enter the owner's name when prompted.
- Example:
  ```
  Enter owner name: John Doe
  ```
- But if it happens you need to add a new car to the same user, you can skip this process of creating new owner and intead go to step proceed to option 2. And when prompted in any of the coming options to give owner id you provide id for ownr you intend to add them a car.

### **2. Add Manufacturer**
- Enter the manufacturer's brand name when prompted.
- Example:
  ```
  Enter manufacturer brand: Toyota
  ```

### **3. Add Car Model**
- Enter the car model and the associated brand ID.
- Example:
  ```
  Enter car model: Corolla
  Enter brand ID: 1
  ```

### **4. Register Car**
- Enter the registration number, owner ID, and model ID.
- Example:
  ```
  Enter registration number: ABC123
  Enter owner ID: 1
  Enter model ID: 1
  ```

### **5. View All Registrations**
- Displays all car registrations along with related data.
- Example output:
  ```
  {'registration_number': 'ABC123', 'owner_name': 'John Doe', 'model_name': 'Corolla'}
  ```

### **6. Exit**
- Closes the application.

## Files in the Project
- **app.py**: The main script to run the application.
- **database/connection.py**: Manages database connections.
- **database/tables.py**: Contains database schema creation logic.
- **models/owner.py**: Handles owner-related database operations.
- **models/manufacturer.py**: Handles manufacturer-related database operations.
- **models/car_model.py**: Handles car model-related database operations.
- **models/car_registration.py**: Handles car registration-related database operations.
- **cars_ownership.db**: SQLite database file.

## Future Enhancements
- Add a search feature to find specific owners, cars, or manufacturers.
- Implement a GUI for easier navigation.
- Add error logging for debugging.

---

## License 
MIT License

Copyright &copy; 2024 Abdul Aljawaab

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
