
import psycopg2
import os
import csv
import config


def connect_db():
    return psycopg2.connect(
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        host=config.DB_HOST,
        port=config.DB_PORT
    )


def show_contacts():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts ORDER BY id")
    contacts = cur.fetchall()

    for contact in contacts:
        print(contact)

    cur.close()
    conn.close()


def search_contacts():
    print("\nSearch by:")
    print("1. First name")
    print("2. Phone number prefix")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter first name: ")

        conn = connect_db()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM contacts WHERE first_name ILIKE %s ORDER BY id",
            (f"%{name}%",)
        )

    elif choice == "2":
        prefix = input("Enter phone number prefix: ")

        conn = connect_db()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM contacts WHERE phone LIKE %s ORDER BY id",
            (f"{prefix}%",)
        )

    else:
        print("Invalid choice!")
        return

    contacts = cur.fetchall()

    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")

    cur.close()
    conn.close()


def update_contact():
    print("\nUpdate by:")
    print("1. Change first name")
    print("2. Change phone number")

    choice = input("Choose an option: ")

    conn = connect_db()
    cur = conn.cursor()

    if choice == "1":
        old_phone = input("Enter the current phone number: ")
        new_name = input("Enter the new first name: ")

        cur.execute(
            "UPDATE contacts SET first_name = %s WHERE phone = %s",
            (new_name, old_phone)
        )

    elif choice == "2":
        old_phone = input("Enter the current phone number: ")
        new_phone = input("Enter the new phone number: ")

        cur.execute(
            "UPDATE contacts SET phone = %s WHERE phone = %s",
            (new_phone, old_phone)
        )

    else:
        print("Invalid choice!")
        cur.close()
        conn.close()
        return

    if cur.rowcount > 0:
        conn.commit()
        print("Contact updated successfully!")
    else:
        conn.rollback()
        print("Contact not found.")

    cur.close()
    conn.close()


def delete_contact():
    print("\nDelete by:")
    print("1. First name")
    print("2. Phone number")

    choice = input("Choose an option: ")

    conn = connect_db()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter first name: ")

        cur.execute(
            "DELETE FROM contacts WHERE first_name = %s",
            (name,)
        )

    elif choice == "2":
        phone = input("Enter phone number: ")

        cur.execute(
            "DELETE FROM contacts WHERE phone = %s",
            (phone,)
        )

    else:
        print("Invalid choice!")
        cur.close()
        conn.close()
        return

    deleted = cur.rowcount
    conn.commit()

    if deleted > 0:
        print(f"Deleted {deleted} contact(s).")
    else:
        print("Contact not found.")

    cur.close()
    conn.close()


def import_csv():
    try:
        csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.csv")
        with open(csv_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            conn = connect_db()
            cur = conn.cursor()

            for row in reader:
                cur.execute(
                    "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
                    (row["first_name"], row["phone"])
                )

            conn.commit()
            cur.close()
            conn.close()

        print("Contacts imported successfully!")

    except FileNotFoundError:
        print("File contacts.csv not found.")
    except (KeyError, psycopg2.Error) as error:
        print("Import failed:", error)


def add_contact():
    name = input("Enter first name: ").strip()
    phone = input("Enter phone number: ").strip()

    if not name or not phone:
        print("Name and phone cannot be empty!")
        return

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added successfully!")


def main():
    while True:
        print("1. Show all contacts")
        print("2. Add a contact")
        print("3. Search contacts")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Import contacts from CSV")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            import_csv()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
