
import json
import csv
from connect import connect_db

#FILTER AND SORT CONTACTS

def filter_sort_contacts():
    print("\n===== FILTER AND SORT CONTACTS =====")

    group_name = input(
        "Enter group (Family/Work/Friend/Other) "
        "or press Enter to skip: "
    ).strip()

    email = input(
        "Enter email keyword or press Enter to skip: "
    ).strip()

    print("\nSort by:")
    print("1. Name")
    print("2. Birthday")
    print("3. Date added")

    sort_choice = input("Choose sorting option: ").strip()

    sort_options = {
        "1": "c.first_name ASC, c.id ASC",
        "2": "c.birthday ASC NULLS LAST, c.first_name ASC",
        "3": "c.created_at DESC, c.id DESC"
    }

    if sort_choice not in sort_options:
        print("Invalid sorting option!")
        return

    order_by = sort_options[sort_choice]

    conn = connect_db()
    cur = conn.cursor()

    try:
        query = f"""
            SELECT
                c.id,
                c.first_name,
                c.email,
                c.birthday,
                g.name AS group_name,
                COALESCE(
                    STRING_AGG(
                        p.phone || ' (' || p.type || ')',
                        ', ' ORDER BY p.id
                    ),
                    'No phone'
                ) AS phones,
                c.created_at
            FROM contacts c
            LEFT JOIN groups g
                ON c.group_id = g.id
            LEFT JOIN phones p
                ON c.id = p.contact_id
            WHERE
                (%s = '' OR g.name ILIKE %s)
                AND
                (%s = '' OR c.email ILIKE %s)
            GROUP BY c.id, g.name
            ORDER BY {order_by}
        """

        cur.execute(
            query,
            (
                group_name,
                group_name,
                email,
                f"%{email}%"
            )
        )

        contacts = cur.fetchall()

        if contacts:
            print("\n===== CONTACTS =====")

            for contact in contacts:
                print("\nID:", contact[0])
                print("Name:", contact[1])
                print("Email:", contact[2])
                print("Birthday:", contact[3])
                print("Group:", contact[4])
                print("Phones:", contact[5])
                print("Date added:", contact[6])

        else:
            print("No contacts found.")

    except Exception as error:
        print("Error:", error)

    finally:
        cur.close()
        conn.close()


#PAGINATED CONTACTS

def show_paginated_contacts():
    print("\n===== CONTACTS PAGINATION =====")

    try:
        page_size = int(input("Enter contacts per page: "))

        if page_size <= 0:
            print("Page size must be positive!")
            return

    except ValueError:
        print("Please enter a valid number!")
        return

    offset = 0

    conn = connect_db()
    cur = conn.cursor()

    try:
        while True:
            cur.execute(
                "SELECT * FROM get_contacts_paginated(%s, %s)",
                (page_size, offset)
            )

            contacts = cur.fetchall()

            if not contacts:
                if offset > 0:
                    print("\nNo more contacts on this page.")
                    offset = max(0, offset - page_size)
                else:
                    print("No contacts found.")

                print("\nCommands: next / prev / quit")
                command = input("Enter command: ").strip().lower()

                if command == "quit":
                    break
                elif command == "prev":
                    if offset >= page_size:
                        offset -= page_size
                    else:
                        print("You are already on the first page.")
                elif command == "next":
                    print("No next page available.")
                else:
                    print("Invalid command!")

                continue

            print("\n===== CONTACTS =====")

            for contact in contacts:
                print(
                    f"ID: {contact[0]} | "
                    f"Name: {contact[1]} | "
                    f"Phone: {contact[2]}"
                )

            print(f"\nPage: {offset // page_size + 1}")
            print("Commands: next / prev / quit")

            command = input("Enter command: ").strip().lower()

            if command == "next":
                offset += page_size

            elif command == "prev":
                if offset >= page_size:
                    offset -= page_size
                else:
                    print("You are already on the first page.")

            elif command == "quit":
                print("Exiting pagination.")
                break

            else:
                print("Invalid command!")

    except Exception as error:
        print("Database error:", error)

    finally:
        cur.close()
        conn.close()



#EXPORT CONTACTS TO JSON


def export_json():
    print("\n===== EXPORT CONTACTS TO JSON =====")

    filename = input(
        "Enter JSON filename (default: contacts.json): "
    ).strip()

    if not filename:
        filename = "contacts.json"

    conn = connect_db()
    cur = conn.cursor()

    try:
        # Get contacts and their groups
        cur.execute("""
            SELECT
                c.id,
                c.first_name,
                c.email,
                c.birthday,
                g.name,
                c.created_at
            FROM contacts c
            LEFT JOIN groups g
                ON c.group_id = g.id
            ORDER BY c.id
        """)

        contacts = cur.fetchall()

        # Get all phone numbers
        cur.execute("""
            SELECT contact_id, phone, type
            FROM phones
            ORDER BY id
        """)

        all_phones = cur.fetchall()

        # Organize phone numbers by contact ID
        phones_by_contact = {}

        for contact_id, phone, phone_type in all_phones:
            if contact_id not in phones_by_contact:
                phones_by_contact[contact_id] = []

            phones_by_contact[contact_id].append({
                "phone": phone,
                "type": phone_type
            })

        # Prepare JSON structure
        data = {"contacts": []}

        for contact in contacts:
            contact_id = contact[0]

            contact_data = {
                "first_name": contact[1],
                "email": contact[2],
                "birthday": (
                    contact[3].isoformat()
                    if contact[3] else None
                ),
                "group": contact[4],
                "created_at": (
                    contact[5].isoformat()
                    if contact[5] else None
                ),
                "phones": phones_by_contact.get(
                    contact_id, []
                )
            }

            data["contacts"].append(contact_data)

        # Write JSON file
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("\nExport successful!")
        print("File:", filename)
        print("Exported contacts:", len(contacts))

    except Exception as error:
        print("Export error:", error)

    finally:
        cur.close()
        conn.close()



#IMPORT CONTACTS FROM JSON


def import_json():
    print("\n===== IMPORT CONTACTS FROM JSON =====")

    filename = input(
        "Enter JSON filename (default: contacts.json): "
    ).strip()

    if not filename:
        filename = "contacts.json"

    # Read JSON file
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            print("Invalid JSON format!")
            return

        contacts_data = data.get("contacts")

        if not isinstance(contacts_data, list):
            print("Invalid JSON format!")
            return

    except FileNotFoundError:
        print("JSON file not found!")
        return

    except json.JSONDecodeError:
        print("Invalid JSON syntax!")
        return

    imported = 0
    updated = 0
    skipped = 0

    valid_types = ("home", "work", "mobile")

    conn = connect_db()
    cur = conn.cursor()

    try:
        for contact in contacts_data:

            if not isinstance(contact, dict):
                raise ValueError("Invalid contact object.")

            # Validate contact name
            name = contact.get("first_name")

            if not isinstance(name, str) or not name.strip():
                raise ValueError("Invalid contact name.")

            name = name.strip()

            if len(name) > 100:
                raise ValueError("Contact name is too long.")

            # Validate phone list
            phones = contact.get("phones", [])

            if not isinstance(phones, list):
                raise ValueError("Phones must be a list.")

            for phone_data in phones:
                if not isinstance(phone_data, dict):
                    raise ValueError("Invalid phone object.")

                phone = phone_data.get("phone")
                phone_type = phone_data.get("type")

                if not isinstance(phone, str) or not phone.strip():
                    raise ValueError("Invalid phone number.")

                if len(phone.strip()) > 20:
                    raise ValueError("Phone number is too long.")

                if phone_type not in valid_types:
                    raise ValueError("Invalid phone type.")

            # Validate email
            email = contact.get("email")

            if email is not None:
                if not isinstance(email, str) or len(email) > 100:
                    raise ValueError("Invalid email address.")

            # Validate birthday
            birthday = contact.get("birthday")

            if birthday is not None:
                if not isinstance(birthday, str):
                    raise ValueError("Invalid birthday format.")

            # Validate created_at
            created_at = contact.get("created_at")

            if created_at is not None:
                if not isinstance(created_at, str):
                    raise ValueError("Invalid created_at format.")

            # Check whether contact already exists
            cur.execute("""
                SELECT id
                FROM contacts
                WHERE LOWER(TRIM(first_name)) =
                      LOWER(TRIM(%s))
                LIMIT 1
            """, (name,))

            existing = cur.fetchone()

            if existing:
                print(f"\nContact '{name}' already exists.")

                while True:
                    choice = input(
                        "Choose: skip / overwrite: "
                    ).strip().lower()

                    if choice in ("skip", "overwrite"):
                        break

                    print("Please enter skip or overwrite.")

                if choice == "skip":
                    skipped += 1
                    continue

            # Get or create contact group
            group_name = contact.get("group")
            group_id = None

            if group_name is not None:
                if not isinstance(group_name, str):
                    raise ValueError("Invalid group name.")

                group_name = group_name.strip()

                if group_name:
                    cur.execute("""
                        INSERT INTO groups (name)
                        VALUES (%s)
                        ON CONFLICT (name)
                        DO UPDATE SET name = EXCLUDED.name
                        RETURNING id
                    """, (group_name,))

                    group_id = cur.fetchone()[0]

            if existing:
                # Update existing contact
                contact_id = existing[0]

                cur.execute("""
                    UPDATE contacts
                    SET first_name = %s,
                        email = %s,
                        birthday = %s::DATE,
                        group_id = %s,
                        created_at = COALESCE(
                            %s::TIMESTAMP,
                            created_at
                        ),
                        phone = NULL
                    WHERE id = %s
                """, (
                    name,
                    email,
                    birthday,
                    group_id,
                    created_at,
                    contact_id
                ))

                # Delete old phone numbers
                cur.execute("""
                    DELETE FROM phones
                    WHERE contact_id = %s
                """, (contact_id,))

                updated += 1

            else:
                # Insert a new contact
                cur.execute("""
                    INSERT INTO contacts (
                        first_name,
                        email,
                        birthday,
                        group_id,
                        created_at
                    )
                    VALUES (
                        %s, %s, %s::DATE, %s,
                        COALESCE(
                            %s::TIMESTAMP,
                            CURRENT_TIMESTAMP
                        )
                    )
                    RETURNING id
                """, (
                    name,
                    email,
                    birthday,
                    group_id,
                    created_at
                ))

                contact_id = cur.fetchone()[0]
                imported += 1

            # Insert all phone numbers
            for phone_data in phones:
                cur.execute("""
                    INSERT INTO phones (
                        contact_id,
                        phone,
                        type
                    )
                    VALUES (%s, %s, %s)
                """, (
                    contact_id,
                    phone_data["phone"].strip(),
                    phone_data["type"]
                ))

        # Save all changes
        conn.commit()

        print("\n===== IMPORT SUMMARY =====")
        print("New contacts:", imported)
        print("Updated contacts:", updated)
        print("Skipped contacts:", skipped)
        print("Import completed successfully!")

    except Exception as error:
        conn.rollback()

        print("\nImport error:", error)
        print("All import changes have been rolled back.")

    finally:
        cur.close()
        conn.close()




#IMPORT CONTACTS FROM CSV

def import_csv():
    print("\n===== IMPORT CONTACTS FROM CSV =====")

    filename = input(
        "Enter CSV filename (default: contacts.csv): "
    ).strip()

    if not filename:
        filename = "contacts.csv"

    valid_types = ("home", "work", "mobile")

    # Read and validate CSV file.
    try:
        with open(filename, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            required_columns = {
                "first_name", "email", "birthday",
                "group", "phone", "type"
            }

            if reader.fieldnames is None:
                print("CSV file is empty!")
                return

            missing = required_columns - set(reader.fieldnames)

            if missing:
                print("Missing CSV columns:", ", ".join(sorted(missing)))
                print(
                    "Required columns: first_name,email,birthday,"
                    "group,phone,type"
                )
                return

            # One contact may occupy several rows if they have
            # multiple phone numbers.
            contacts_by_name = {}

            for row_number, row in enumerate(reader, start=2):
                name = (row.get("first_name") or "").strip()

                if not name:
                    raise ValueError(
                        f"Row {row_number}: first_name cannot be empty."
                    )

                if len(name) > 100:
                    raise ValueError(
                        f"Row {row_number}: contact name is too long."
                    )

                email = (row.get("email") or "").strip() or None
                birthday = (row.get("birthday") or "").strip() or None
                group_name = (row.get("group") or "").strip() or None
                phone = (row.get("phone") or "").strip()
                phone_type = (row.get("type") or "").strip().lower()

                if email and len(email) > 100:
                    raise ValueError(
                        f"Row {row_number}: email is too long."
                    )

                if phone:
                    if len(phone) > 20:
                        raise ValueError(
                            f"Row {row_number}: phone number is too long."
                        )
                    if phone_type not in valid_types:
                        raise ValueError(
                            f"Row {row_number}: type must be home, work or mobile."
                        )
                elif phone_type:
                    raise ValueError(
                        f"Row {row_number}: phone type was provided "
                        "without a phone number."
                    )

                key = name.casefold()

                if key not in contacts_by_name:
                    contacts_by_name[key] = {
                        "first_name": name,
                        "email": email,
                        "birthday": birthday,
                        "group": group_name,
                        "phones": []
                    }
                else:
                    existing_data = contacts_by_name[key]
                    if (
                        existing_data["email"] != email
                        or existing_data["birthday"] != birthday
                        or existing_data["group"] != group_name
                    ):
                        raise ValueError(
                            f"Row {row_number}: metadata for contact "
                            f"'{name}' differs between CSV rows."
                        )

                if phone:
                    contacts_by_name[key]["phones"].append({
                        "phone": phone,
                        "type": phone_type
                    })

        if not contacts_by_name:
            print("No contacts found in CSV file.")
            return

    except FileNotFoundError:
        print("CSV file not found!")
        return
    except (csv.Error, UnicodeError, ValueError) as error:
        print("CSV read error:", error)
        return

    imported = 0
    updated = 0
    skipped = 0

    conn = connect_db()
    cur = conn.cursor()

    try:
        for contact in contacts_by_name.values():
            name = contact["first_name"]

            cur.execute("""
                SELECT id
                FROM contacts
                WHERE LOWER(TRIM(first_name)) = LOWER(TRIM(%s))
                ORDER BY id
                LIMIT 1
            """, (name,))

            existing = cur.fetchone()

            if existing:
                print(f"\nContact '{name}' already exists.")

                while True:
                    choice = input(
                        "Choose: skip / overwrite: "
                    ).strip().lower()

                    if choice in ("skip", "overwrite"):
                        break

                    print("Please enter skip or overwrite.")

                if choice == "skip":
                    skipped += 1
                    continue

            # Find or create the contact's group.
            group_id = None
            group_name = contact["group"]

            if group_name:
                cur.execute("""
                    INSERT INTO groups (name)
                    VALUES (%s)
                    ON CONFLICT (name)
                    DO UPDATE SET name = EXCLUDED.name
                    RETURNING id
                """, (group_name,))
                group_id = cur.fetchone()[0]

            if existing:
                contact_id = existing[0]

                cur.execute("""
                    UPDATE contacts
                    SET first_name = %s,
                        email = %s,
                        birthday = %s::DATE,
                        group_id = %s,
                        phone = NULL
                    WHERE id = %s
                """, (
                    name,
                    contact["email"],
                    contact["birthday"],
                    group_id,
                    contact_id
                ))

                cur.execute("""
                    DELETE FROM phones
                    WHERE contact_id = %s
                """, (contact_id,))

                updated += 1

            else:
                cur.execute("""
                    INSERT INTO contacts (
                        first_name, email, birthday, group_id
                    )
                    VALUES (%s, %s, %s::DATE, %s)
                    RETURNING id
                """, (
                    name,
                    contact["email"],
                    contact["birthday"],
                    group_id
                ))

                contact_id = cur.fetchone()[0]
                imported += 1

            for phone_data in contact["phones"]:
                cur.execute("""
                    INSERT INTO phones (contact_id, phone, type)
                    VALUES (%s, %s, %s)
                """, (
                    contact_id,
                    phone_data["phone"],
                    phone_data["type"]
                ))

        conn.commit()

        print("\n===== CSV IMPORT SUMMARY =====")
        print("New contacts:", imported)
        print("Updated contacts:", updated)
        print("Skipped contacts:", skipped)
        print("CSV import completed successfully!")

    except Exception as error:
        conn.rollback()
        print("\nCSV import error:", error)
        print("All CSV import changes have been rolled back.")

    finally:
        cur.close()
        conn.close()



#MAIN MENU


def main():
    while True:
        print("\n========== PHONEBOOK TSIS 1 ==========")
        print("1. Filter and sort contacts")
        print("2. Show contacts with pagination")
        print("3. Export contacts to JSON")
        print("4. Import contacts from JSON")
        print("5. Import contacts from CSV")
        print("0. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            filter_sort_contacts()

        elif choice == "2":
            show_paginated_contacts()

        elif choice == "3":
            export_json()

        elif choice == "4":
            import_json()

        elif choice == "5":
            import_csv()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
