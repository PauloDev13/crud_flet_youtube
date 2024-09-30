import sqlite3


class ConnectionManager:
    def __init__(self):
        self.connection = sqlite3.connect(database='connection/data.db', check_same_thread=False)

    def add_contact(self, name, age, email, phone):
        query = 'INSERT INTO contacts (NAME, AGE, EMAIL, PHONE) VALUES (?, ?, ?, ?)'

        self.connection.execute(query, (name, age, email, phone))
        self.connection.commit()

    def get_all_contacts(self) -> list:
        cursor = self.connection.cursor()
        query = 'SELECT * FROM contacts'
        cursor.execute(query)
        return cursor.fetchall()

    def update_contact(self, contact_id, name, age, email, phone):
        query = 'UPDATE contacts SET NAME=?, AGE=?, EMAIL=?, PHONE=? WHERE ID=?'
        self.connection.execute(query, (name, age, email, phone, contact_id))
        self.connection.commit()

    def delete_contact(self, name):
        query = 'DELETE FROM contacts WHERE NAME=?'
        self.connection.execute(query, (name,))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()
