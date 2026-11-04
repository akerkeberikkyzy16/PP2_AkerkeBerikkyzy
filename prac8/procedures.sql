
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM contacts
        WHERE first_name = p_name
    ) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE first_name = p_name;

        RAISE NOTICE 'Contact updated successfully!';
    ELSE
        INSERT INTO contacts(first_name, phone)
        VALUES(p_name, p_phone);

        RAISE NOTICE 'Contact inserted successfully!';
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_users(
    p_names TEXT[],
    p_phones TEXT[],
    INOUT p_invalid_data TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INTEGER;
    current_name TEXT;
    current_phone TEXT;
BEGIN
    p_invalid_data := '';

    IF array_length(p_names, 1) IS DISTINCT FROM
       array_length(p_phones, 1) THEN
        RAISE EXCEPTION 'Names and phones must have the same length!';
    END IF;

    IF p_names IS NULL OR p_phones IS NULL THEN
        RAISE EXCEPTION 'Input arrays cannot be NULL!';
    END IF;

    FOR i IN 1..COALESCE(array_length(p_names, 1), 0)
    LOOP
        current_name := btrim(p_names[i]);
        current_phone := btrim(p_phones[i]);

        IF current_name = '' OR
           current_phone !~ '^\+?[0-9]{10,15}$' THEN

            p_invalid_data := p_invalid_data ||
                'Invalid data: ' || current_name ||
                ', ' || current_phone || E'\n';

        ELSE
            INSERT INTO contacts(first_name, phone)
            VALUES(current_name, current_phone);
        END IF;
    END LOOP;

    RAISE NOTICE 'Bulk insert completed!';
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(
    p_value VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    deleted_count INTEGER;
BEGIN
    IF p_type = 'name' THEN
        DELETE FROM contacts
        WHERE first_name = p_value;

    ELSIF p_type = 'phone' THEN
        DELETE FROM contacts
        WHERE phone = p_value;

    ELSE
        RAISE EXCEPTION
            'Invalid type! Use name or phone.';
    END IF;

    GET DIAGNOSTICS deleted_count = ROW_COUNT;

    RAISE NOTICE 'Deleted % contact(s).', deleted_count;
END;
$$;
