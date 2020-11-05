"""
"""
from typing import Optional, Dict

from database import Database, Results


class EtymologyDatabase(Database):
    schema = '''CREATE TABLE IF NOT EXISTS word
                (id INTEGER PRIMARY KEY,
                word TEXT,
                date_added INT,
                date_modified INT);
                CREATE TABLE IF NOT EXISTS link
                (id INTEGER PRIMARY KEY,
                name INT,
                url TEXT,
                word_id INT,
                date_added INT,
                date_modified INT,
                FOREIGN KEY (word_id) REFERENCES photo (id));
            '''

    def add_word(self, word: str, date_added: Optional[str] = None, date_modified: Optional[str] = None) -> int:
        date_added, date_modified = self._dates(date_added, date_modified)
        params = (word, date_added, date_modified)
        new_id = self.insert('''INSERT INTO word(word, date_added, date_modified)
                                VALUES(?,?,?)''', params)
        return new_id

    def add_link(self, word_id: int, name: str, url, date_added: Optional[str] = None,
                 date_modified: Optional[str] = None) -> int:
        date_added, date_modified = self._dates(date_added, date_modified)
        params = (word_id, name, url, date_added, date_modified)
        new_id = self.insert('''INSERT INTO link(word_id, name, url, date_added, date_modified)
                                VALUES(?,?,?,?,?)''', params)
        return new_id

    def add_word_and_links(self, word: str, urls: Dict, date_added: Optional[str] = None,
                           date_modified: Optional[str] = None) -> None:
        word_id = self.add_word(word, date_added, date_modified)
        for name, url in urls.items():
            self.add_link(word_id, name, url, date_added, date_modified)
        return

    def get_word_all(self):
        cursor = self.query('''SELECT * FROM word''')
        return Results(cursor).fetchall_dict_factory()
