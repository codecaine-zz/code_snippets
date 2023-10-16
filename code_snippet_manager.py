import sqlite3


class CodeSnippetManager:
    """
    Class to manage code snippets. Snippets are stored in an SQLite database.
    """

    def __init__(self, filename):
        """
        Constructor to initialize the CodeSnippetManager.

        :param filename: Name of the SQLite database file to store and load snippets.
        """
        self.filename = filename
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Method to create the snippets table if it does not exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS snippets (
                id INTEGER PRIMARY KEY,
                language TEXT,
                title TEXT,
                code TEXT,
                category TEXT,
                additional_info TEXT
            )
        """)
        self.connection.commit()

    def add_snippet(self, language, title, code, category, additional_info):
        """
        Method to add a new snippet.

        :param language: Programming language of the snippet.
        :param title: Title of the snippet.
        :param code: Code of the snippet.
        :param category: Category of the snippet.
        :param additional_info: Additional information about the snippet.
        """
        if not self.snippet_exists(language, title, category):
            self.cursor.execute("""
                INSERT INTO snippets (language, title, code, category, additional_info)
                VALUES (?, ?, ?, ?, ?)
            """, (language, title, code, category, additional_info))
            self.connection.commit()
            print("Snippet created successfully.")
        else:
            print("Snippet with the same language, title, and category already exists.")

    def read_snippet(self, snippet_id):
        """
        Method to read a snippet by its ID.

        :param snippet_id: ID of the snippet.
        :return: Snippet if it exists, otherwise None.
        """
        self.cursor.execute("""
            SELECT * FROM snippets WHERE id = ?
        """, (snippet_id,))
        row = self.cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'language': row[1],
                'title': row[2],
                'code': row[3],
                'category': row[4],
                'additional_info': row[5]
            }
        return None

    def update_snippet(self, snippet_id, language=None,
                       title=None, code=None, category=None,
                       additional_info=None):
        """
        Method to update a snippet by its ID.

        :param snippet_id: ID of the snippet.
        :param language: Programming language of the snippet (to update).
        :param title: Title of the snippet (to update).
        :param code: Code of the snippet (to update).
        :param category: Category of the snippet (to update).
        :param additional_info: Additional information about the snippet (to update).
        :return: True if the update was successful, otherwise False.
        """
        self.cursor.execute("""
            SELECT * FROM snippets WHERE id = ?
        """, (snippet_id,))
        row = self.cursor.fetchone()
        if row:
            update_query = "UPDATE snippets SET "
            update_params = []
            if language:
                update_query += "language = ?, "
                update_params.append(language)
            if title:
                update_query += "title = ?, "
                update_params.append(title)
            if code:
                update_query += "code = ?, "
                update_params.append(code)
            if category:
                update_query += "category = ?, "
                update_params.append(category)
            if additional_info:
                update_query += "additional_info = ?, "
                update_params.append(additional_info)
            update_query = update_query.rstrip(", ")
            update_query += " WHERE id = ?"
            update_params.append(snippet_id)
            self.cursor.execute(update_query, tuple(update_params))
            self.connection.commit()
            return True
        return False

    def delete_snippet(self, snippet_id):
        """
        Method to delete a snippet by its ID.

        :param snippet_id: ID of the snippet.
        :return: True if the delete was successful, otherwise False.
        """
        self.cursor.execute("""
            DELETE FROM snippets WHERE id = ?
        """, (snippet_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def list_snippets(self):
        """Method to get a list of all the snippets."""
        self.cursor.execute("""
            SELECT * FROM snippets
        """)
        rows = self.cursor.fetchall()
        return [{
            'id': row[0],
            'language': row[1],
            'title': row[2],
            'code': row[3],
            'category': row[4],
            'additional_info': row[5]
        } for row in rows]

    def snippet_exists(self, language, title, category):
        """
        Method to check if a snippet already exists.

        :param language: Programming language of the snippet.
        :param title: Title of the snippet.
        :param category: Category of the snippet.
        :return: True if the snippet exists, otherwise False.
        """
        self.cursor.execute("""
            SELECT * FROM snippets WHERE language = ? AND title = ? AND category = ?
        """, (language, title, category))
        row = self.cursor.fetchone()
        return row is not None

    def get_languages(self):
        """Method to get a list of all the languages."""
        self.cursor.execute("""
            SELECT DISTINCT language FROM snippets
        """)
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]

    def get_categories(self):
        """Method to get a list of all the categories."""
        self.cursor.execute("""
            SELECT DISTINCT category FROM snippets
        """)
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]

    def get_snippets_by_language(self, language):
        """Method to get a list of all the snippets by language."""
        self.cursor.execute("""
            SELECT * FROM snippets WHERE language = ?
        """, (language,))
        rows = self.cursor.fetchall()
        return [{
            'id': row[0],
            'language': row[1],
            'title': row[2],
            'code': row[3],
            'category': row[4],
            'additional_info': row[5]
        } for row in rows]

    def get_snippets_by_category(self, category):
        """Method to get a list of all the snippets by category."""
        self.cursor.execute("""
            SELECT * FROM snippets WHERE category = ?
        """, (category,))
        rows = self.cursor.fetchall()
        return [{
            'id': row[0],
            'language': row[1],
            'title': row[2],
            'code': row[3],
            'category': row[4],
            'additional_info': row[5]
        } for row in rows]

    def get_snippets_by_language_and_category(self, language, category):
        """Method to get a list of all the snippets by language and category."""
        self.cursor.execute("""
            SELECT * FROM snippets WHERE language = ? AND category = ?
        """, (language, category))
        rows = self.cursor.fetchall()
        return [{
            'id': row[0],
            'language': row[1],
            'title': row[2],
            'code': row[3],
            'category': row[4],
            'additional_info': row[5]
        } for row in rows]

    def get_snippets_by_title(self, title):
        """Method to get a list of all the snippets by title."""
        self.cursor.execute("""
            SELECT * FROM snippets WHERE title = ?
        """, (title,))
        rows = self.cursor.fetchall()
        return [{
            'id': row[0],
            'language': row[1],
            'title': row[2],
            'code': row[3],
            'category': row[4],
            'additional_info': row[5]
        } for row in rows]


# Path: code_snippet_manager_test.py
