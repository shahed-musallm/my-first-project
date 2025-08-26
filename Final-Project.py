

Admin_User = "ibtisam"
Admin_Pass = "20222023"


phone_list = []


def is_valid_number(phone_num):
    return phone_num.startswith("059") and len(phone_num) == 9 and phone_num.isdigit()


def admin_login():
    user = input("Enter username: ")
    password = input("Enter password: ")
    return user == Admin_User and password == Admin_Pass


def add_number():
    phone = input("Enter phone number (should start with 059): ")
    if not is_valid_number(phone):
        print(" Invalid phone number !! ")
        return
    person_id = input("Enter ID number: ")
    person_name = input("Enter name: ")
    person_age = input("Enter age: ")
    person_address = input("Enter address: ")

    phone_list.append({
        "phone": phone,
        "person_id": person_id,
        "person_name": person_name,
        "person_age": person_age,
        "person_address": person_address
    })
    print(" Number added successfully ")


def all_number():
    if not phone_list:
        print("No phone numbers have been  stored")
        return
    for item in phone_list:
        print(item)


def find_number():
    search_term = input("Enter phone number to search for: ")
    for item in phone_list:
        if item["phone"] == search_term:
            print(item)
            return
    print("Phone number was not found")


def update_details():
    number_to_update = input("Enter phone number to update: ")
    for person in phone_list:
        if person["phone"] == number_to_update:
            person["person_id"] = input("Enter new ID: ")
            person["person_name"] = input("Enter new name: ")
            person["person_age"] = input("Enter new age: ")
            person["person_address"] = input("Enter new address: ")
            print("Phone details have been updated.")
            return
    print("Phone number not found.")


def remove_number():
    number_to_delete = input("Enter phone number to delete: ")
    for person in phone_list:
        if person["phone"] == number_to_delete:
            phone_list.remove(person)
            print("Phone number has been deleted")
            return
    print("Phone number not found")


def admin_panel():
    while True:
        print("1- Add Phone Number")
        print("2- Show All Phone Numbers")
        print("3- Search for phone number details")
        print("4- Update phone number info")
        print("5- Delete phone number")
        print("6- Exit")

        choice = input("Enter your selection: ")

        if choice == "1":
            add_number()
        elif choice == "2":
            all_numbers()
        elif choice == "3":
            find_number()
        elif choice == "4":
            update_details()
        elif choice == "5":
            remove_number()
        elif choice == "6":
            break
        else:
            print("Invalid selection.")


def main():
    while True:
        print("\n" + "*" * 60)
        print("Welcome, the System is now active")
        print("*" * 60)
        print("1- Admin Panel")
        print("2- Search for phone number details")
        print("3- Exit")

        selection = input("Enter your choice: ")

        if selection == "1":
            if admin_login():
                admin_panel()
            else:
                print("Incorrect username or password.")
        elif selection == "2":
            find_number()
        elif selection == "3":
            print("Exiting from the program")
            break
        else:
            print("Invalid choice")


main()
