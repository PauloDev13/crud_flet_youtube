import sqlite3


class ConnectionManager:
    def __init__(self):
        self.connection = sqlite3.connect(
            database='connection/data.db',
            check_same_thread=True
        )

    def add_contact(self, name, age, email, phone):
        try:
            # cursor = self.connection.cursor()
            query = 'INSERT INTO contacts (NAME, AGE, EMAIL, PHONE) VALUES (?, ?, ?, ?)'
            self.connection.execute(query, (name, age, email, phone))
            self.connection.commit()
            print(f'contato {name} adicionado com sucesso')

        except sqlite3.Error as e:
            print('Erro ao inserir contato.', e)

        except Exception as e:
            # Captura outros erros e exibe a mensagem
            print(f'Erro inesperado: {e}')

    def get_all_contacts(self) -> list:
        try:
            cursor = self.connection.cursor()
            query = 'SELECT * FROM contacts'
            cursor.execute(query)
            return cursor.fetchall()

        except sqlite3.Error as e:
            print(f"Erro ao buscar contatos: {e}")
            return []

    def update_contact(self, contact_id, name, age, email, phone):
        query = 'UPDATE contacts SET NAME=?, AGE=?, EMAIL=?, PHONE=? WHERE ID=?'
        self.connection.execute(query, (name, age, email, phone, contact_id))
        self.connection.commit()

    def delete_contact(self, name):
        query = 'DELETE FROM contacts WHERE NAME=?'
        self.connection.execute(query, (name,))
        self.connection.commit()

    def close_connection(self):
        if self.connection:
            self.connection.close()
