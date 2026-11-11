--Create contact groups
CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

--Add standard groups
INSERT INTO groups (name)
VALUES
    ('Family'),
    ('Work'),
    ('Friend'),
    ('Other')
ON CONFLICT (name) DO NOTHING;

--Extend existing contacts table
ALTER TABLE contacts
ADD COLUMN IF NOT EXISTS email VARCHAR(100),
ADD COLUMN IF NOT EXISTS birthday DATE,
ADD COLUMN IF NOT EXISTS group_id INTEGER
    REFERENCES groups(id),
ADD COLUMN IF NOT EXISTS created_at TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP;

--Create separate phones table
CREATE TABLE IF NOT EXISTS phones (
    id SERIAL PRIMARY KEY,
    contact_id INTEGER
        REFERENCES contacts(id) ON DELETE CASCADE,
    phone VARCHAR(20) NOT NULL,
    type VARCHAR(10)
        CHECK (type IN ('home', 'work', 'mobile'))
);

--Move old phone numbers into phones
INSERT INTO phones (contact_id, phone, type)
SELECT c.id, c.phone, 'mobile'
FROM contacts c
WHERE c.phone IS NOT NULL
  AND c.phone <> ''
  AND NOT EXISTS (
      SELECT 1
      FROM phones p
      WHERE p.contact_id = c.id
        AND p.phone = c.phone
  );

--Make old phone column optional
ALTER TABLE contacts
ALTER COLUMN phone DROP NOT NULL;
