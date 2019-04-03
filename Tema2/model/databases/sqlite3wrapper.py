import sqlite3

class Database:
    InsertConflictError = 409

    def __init__(self, path):
        conn = sqlite3.connect(path)
        conn.close()
        self.path = path

    def select(self, table, pattern=None, params=None):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()

        if params:
            c.execute("SELECT * FROM {} {}".format(table, pattern), params)
        else:
            c.execute("SELECT * FROM {} {}".format(table, pattern))
        result = c.fetchall()

        conn.close()
        return result

    def create_table(self, table, columns):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()

        query = "CREATE TABLE {} {}".format(table, columns)
        try:
            c.execute(query)
        except Exception:
            pass
        conn.commit()
        conn.close()

    def insert(self, table, data, columns=[]):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()

        if columns:
            columns_string = "("
            for column in columns:
                columns_string += column + ", "
            columns_string = columns_string[:-2] + ") "
        else:
            columns_string = ""

        query = "INSERT INTO {} {} VALUES (".format(table, columns_string)
        for value in data:
            query += "?, "
        query = query[:-2] + ")"

        try:
            c.execute(query, data)
            conn.commit()
        except sqlite3.IntegrityError:
            return {'status_code':409}
        finally:
            conn.close()

        return {'status_code':201, 'id':c.lastrowid}

    def update(self, table, id_name, id_value, data, columns=[]):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()

        if columns:
            columns_string = ""
            for i, column in enumerate(columns):
                if data[i] is not None:
                    columns_string += column + " = ?, " 
            columns_string = columns_string[:-2] + " "
        else:
            return {'status_code':400}

        query = "UPDATE {} SET {} WHERE {} = ?".format(table, columns_string, id_name)
        data = [value for value in data if value is not None]
        if len(data) == 0:
            return {'status_code':400}
        data.append(id_value)

        try:
            c.execute(query, data)
            conn.commit()
        finally:
            conn.close()

        return {'status_code':200}

    def delete_by_id(self, table, id_name, id_value):
        conn = sqlite3.connect(self.path)

        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        
        c = conn.cursor()
        c.execute("SELECT * FROM {} WHERE {}=?".format(table, id_name), (id_value,))
        
        if c.fetchone():
            c = conn.cursor()
            c.execute("DELETE FROM {} WHERE {}=?".format(table, id_name), (id_value,))
            conn.commit()
            conn.close()
            return {'status_code':200}
        else:
            return {'status_code':404}

    def delete_all(self, table):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute("DELETE FROM {}".format(table))
        conn.commit()
        conn.close()
        return {'status_code':200}

    def all_tables(self):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cursor.fetchall())
        conn.close()