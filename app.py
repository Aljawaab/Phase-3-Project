from database.tables import create_tables
from models.owner import Owner
from models.manufacturer import Manufacturer
from models.car_model import CarModel
from models.car_registration import CarRegistration


def main():
    create_tables()

    while True:
        print("\nCar Registration System")
        print("1. Add Owner")
        print("2. Add Manufacturer")
        print("3. Add Car Model")
        print("4. Register Car")
        print("5. View All Owners and Related Data")
        print("6. Delete Owner")  # New menu option
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

    
        if choice == "1":
            name = input("Enter owner name: ").strip()
            if not name:
                print("Error: Owner name cannot be empty.")
            else:
                Owner(name)
                print("Owner created successfully!")
        elif choice == "2":
            brand = input("Enter manufacturer brand: ").strip()
            if not brand:
                print("Error: Manufacturer brand cannot be empty.")
            else:
                Manufacturer(brand)
                print("Manufacturer created successfully!")
        elif choice == "3":
            model = input("Enter car model: ").strip()
            brand_id = input("Enter brand ID: ").strip()
            if not model or not brand_id.isdigit():
                print("Error: Invalid inputs.")
            else:
                CarModel(model, int(brand_id))
                print("Car model created successfully!")
        elif choice == "4":
            registration_number = input("Enter registration number: ").strip()
            owner_id = input("Enter owner ID: ").strip()
            model_id = input("Enter model ID: ").strip()
            if not registration_number or not owner_id.isdigit() or not model_id.isdigit():
                print("Error: Invalid inputs.")
            else:
                CarRegistration(registration_number, int(owner_id), int(model_id))
                print("Car registered successfully!")
        elif choice == "5":
            owners_data = Owner.fetch_with_related_data()
            if not owners_data:
                print("No data found.")
            else:
                for record in owners_data:
                    print(f"Owner: {record['owner_name']}, "
                          f"Registration: {record['registration_number']}, "
                          f"Car Model: {record['car_model']}, "
                          f"Manufacturer: {record['manufacturer']}")
        elif choice == "6":
            owner_id = input("Enter the ID of the owner to delete: ")
            confirmation = input(f"Are you sure you want to delete Owner ID {owner_id} and related data? (yes/no): ").strip().lower()
            if confirmation == "yes":
                result = Owner.delete_owner(owner_id)
                print(result)
            else:
                print("Deletion canceled.")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
