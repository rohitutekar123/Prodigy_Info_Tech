import json

class ContactManager:
    def __init__(self):
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                contacts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            contacts = {}
        return contacts

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file)

    def add_contact(self):
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email address: ")

        self.contacts[name] = {"Phone": phone, "Email": email}
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for name, info in self.contacts.items():
                print(f"{name}: Phone - {info['Phone']}, Email - {info['Email']}")

    def edit_contact(self):
        name_to_edit = input("Enter the name of the contact to edit: ")
        if name_to_edit in self.contacts:
            new_phone = input(f"Enter the new phone number for {name_to_edit}: ")
            new_email = input(f"Enter the new email address for {name_to_edit}: ")

            self.contacts[name_to_edit]["Phone"] = new_phone
            self.contacts[name_to_edit]["Email"] = new_email

            print(f"Contact '{name_to_edit}' updated successfully.")
        else:
            print(f"Contact '{name_to_edit}' not found.")

    def delete_contact(self):
        name_to_delete = input("Enter the name of the contact to delete: ")
        if name_to_delete in self.contacts:
            del self.contacts[name_to_delete]
            print(f"Contact '{name_to_delete}' deleted successfully.")
        else:
            print(f"Contact '{name_to_delete}' not found.")

    def run(self):
        while True:
            print("\nContact Management System:")
            print("1. Add a new contact")
            print("2. View all contacts")
            print("3. Edit an existing contact")
            print("4. Delete a contact")
            print("5. Quit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.edit_contact()
            elif choice == "4":
                self.delete_contact()
            elif choice == "5":
                self.save_contacts()
                print("Exiting the Contact Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

# Run the contact management system
contact_manager = ContactManager()
contact_manager.run()
