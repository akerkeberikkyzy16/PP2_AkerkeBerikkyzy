--add a phone number to an existing contact

CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    contact_id_value INTEGER;
BEGIN
    SELECT id
    INTO contact_id_value
    FROM contacts
    WHERE first_name = p_contact_name
    LIMIT 1;

    IF contact_id_value IS NULL THEN
        RAISE EXCEPTION 'Contact not found!';
    END IF;

    IF p_type NOT IN ('home', 'work', 'mobile') THEN
        RAISE EXCEPTION 'Invalid phone type!';
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES(contact_id_value, p_phone, p_type);

    RAISE NOTICE 'Phone added successfully!';
END;
$$;


--move a contact to a group

CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    contact_id_value INTEGER;
    group_id_value INTEGER;
BEGIN
    SELECT id
    INTO contact_id_value
    FROM contacts
    WHERE first_name = p_contact_name
    LIMIT 1;

    IF contact_id_value IS NULL THEN
        RAISE EXCEPTION 'Contact not found!';
    END IF;

    INSERT INTO groups(name)
    VALUES(p_group_name)
    ON CONFLICT (name) DO NOTHING;

    SELECT id
    INTO group_id_value
    FROM groups
    WHERE name = p_group_name;

    UPDATE contacts
    SET group_id = group_id_value
    WHERE id = contact_id_value;

    RAISE NOTICE 'Contact moved to group successfully!';
END;
$$;


--search contacts by name, email or any phone

CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(
    id INTEGER,
    first_name VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT
        c.id,
        c.first_name,
        c.email,
        c.birthday,
        g.name
    FROM contacts c
    LEFT JOIN groups g
        ON c.group_id = g.id
    LEFT JOIN phones p
        ON c.id = p.contact_id
    WHERE
        c.first_name ILIKE '%' || p_query || '%'
        OR c.email ILIKE '%' || p_query || '%'
        OR p.phone ILIKE '%' || p_query || '%'
    ORDER BY c.id;
END;
$$ LANGUAGE plpgsql;
