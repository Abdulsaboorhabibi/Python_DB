from db import Database


class Item:
    def __init__(self):
        self.db = Database()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                name TEXT,
                quantity INTEGER,
                price REAL
            )
        '''
        self.db.execute(query)

    def create_item(self, name, quantity, price):
        query = 'INSERT INTO items (name, quantity, price) VALUES (?, ?, ?)'
        self.db.execute(query, (name, quantity, price))

    def get_items(self):
        query = 'SELECT * FROM items'
        self.db.execute(query)
        return self.db.fetchall()

    def update_item(self, item_id, name, quantity, price):
        query = 'UPDATE items SET name = ?, quantity = ?, price = ? WHERE id = ?'
        self.db.execute(query, (name, quantity, price, item_id))

    def delete_item(self, item_id):
        query = 'DELETE FROM items WHERE id = ?'
        self.db.execute(query, (item_id,))

    def close(self):
        self.db.close()
