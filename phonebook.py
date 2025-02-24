#PROJECT 3: PHONEBOOK

phonebook = [
    {"Name": "James", "Phone number": "08056743621", "Favorite": False},
    {"Name": "John", "Phone number": "08056543421", "Favorite": True},
    {"Name": "Joshua", "Phone number": "08065743621", "Favorite": False},
    {"Name": "Jeremiah", "Phone number": "08032413621", "Favorite": False}
]

def add_contact(contact: dict):
    phonebook.append(contact)

def view_contacts():
    for contact in phonebook:
        print(f"{contact["Name"]}: {contact["Phone number"]}")

def update_contact(phone_number):
    for contact in phonebook:
        if phone_number == contact["Phone number"]:
            choice = input("What would you like to change? ")
            for information in contact.keys():
                if choice == information:
                    change = input(f"What would you like to change {information} to? ")
                    contact[information] = change

def delete_contact(phone_number):
    for contact in phonebook:
        if phone_number == contact["Phone number"]:
            phonebook.remove(contact)

def search_contact(name):
    for contact in phonebook:
        if name == contact["Name"]:
            print(f"{contact['Name']}: {contact["Phone number"]}")

def mark_favorite(phone_number):
    for contact in phonebook:
        if phone_number == contact["Phone number"]:
            contact["Favorite"] = True

def unmark_favorite(phone_number):
    for contact in phonebook:
        if phone_number == contact["Phone number"]:
            contact["Favorite"] = False

while True:
    actions = ["add contact", "view contacts", "search contact", "update contact", "delete contact", "mark as favorite", "unmark as favorite", "exit"]
    inquiry = input("What would you like to do? ").lower()
    if inquiry not in actions:
        print("Cannot perform such an action")
        continue
    
    elif inquiry in actions:
        if inquiry == "add contacts":
            contact = {}
            name = input("\nWhat is the name of the contact? ")
            contact["Name"] = name.title()
            phone_number = input("\nWhat is the phone number of the contact? ")
            contact["Phone number"] = phone_number
            favorite = input("\nDo you wish to mark this contact as a favorite? ")
            if favorite == "Yes" or favorite == "yes":
                contact["Favorite"] = True
            else:
                contact["Favorite"] = False
            add_contact(contact)
            continue
        
        elif inquiry == "view contacts":
            view_contacts()
            continue
        
        elif inquiry == "update contact":
            phone_number = input("Provide the phone number of the contact you want to update: ")
            update_contact(phone_number)
            continue

        elif inquiry == "search contact":
            name = input("Whose contact do you want to search? ")
            search_contact(name)
            continue

        elif inquiry == "delete contact":
            phone_number = input("Provide the phone number of the contact you want to delete: ")
            delete_contact(phone_number)
            continue

        elif inquiry == "mark as favorite":
            phone_number = input("Provide the phone number of the contact you want to mark as favorite: ")
            mark_favorite(phone_number)
            continue

        elif inquiry == "unmark as favorite":
            phone_number = input("Provide the phone number of the contact you want to unmark as favorite: ")
            unmark_favorite(phone_number)
            continue

        elif inquiry == "exit":
            break



            

