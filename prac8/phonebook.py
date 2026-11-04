
from connect import connect_db


def search_contacts():
    pattern = input("Enter name or phone pattern: ")

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts_by_pattern(%s)",
        (pattern,)
    )

    contacts = cur.fetchall()

    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")

    cur.close()
    conn.close()


def upsert_contact():
    name = input("Enter first name: ").strip()
    phone = input("Enter phone number: ").strip()

    if not name or not phone:
        print("Name and phone cannot be empty!")
        return

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "CALL upsert_contact(%s, %s)",
        (name, phone)
    )

    conn.commit()

    print("Contact saved successfully!")

    cur.close()
    conn.close()


def insert_many_users():
    names_input = input(
        "Enter names separated by commas: "
    )

    phones_input = input(
        "Enter phones separated by commas: "
    )

    names = [name.strip() for name in names_input.split(",")]
    phones = [phone.strip() for phone in phones_input.split(",")]

    if len(names) != len(phones):
        print("The number of names and phones must be equal!")
        return

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        """
        CALL insert_many_users(
            %s::TEXT[],
            %s::TEXT[],
            %s::TEXT
        )
        """,
        (names, phones, None)
    )

    result = cur.fetchone()
    conn.commit()

    if result and result[0]:
        print("Incorrect data:")
        print(result[0])
    else:
        print("All contacts were inserted successfully!")

    cur.close()
    conn.close()


def show_paginated_contacts():
    try:
        limit = int(input("Enter number of contacts per page: "))
        offset = int(input("Enter offset: "))

        if limit <= 0 or offset < 0:
            print("Limit must be positive and offset cannot be negative!")
            return

    except ValueError:
        print("Please enter valid numbers!")
        return

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s, %s)",
        (limit, offset)
    )

    contacts = cur.fetchall()

    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")

    cur.close()
    conn.close()


def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")

    choice = input("Choose an option: ")

    if choice == "1":
        value = input("Enter first name: ")
        delete_type = "name"

    elif choice == "2":
        value = input("Enter phone number: ")
        delete_type = "phone"

    else:
        print("Invalid choice!")
        return

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "CALL delete_contact(%s, %s)",
        (value, delete_type)
    )

    conn.commit()

    print("Delete operation completed!")

    cur.close()
    conn.close()


def main():
    while True:
        print("\n===== PHONEBOOK =====")
        print("1. Search contacts")
        print("2. Add or update contact")
        print("3. Insert many users")
        print("4. Show contacts with pagination")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            search_contacts()

        elif choice == "2":
            upsert_contact()

        elif choice == "3":
            insert_many_users()

        elif choice == "4":
            show_paginated_contacts()

        elif choice == "5":
            delete_contact()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
