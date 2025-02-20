'''
Defines the AlbumRepository class
'''
from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM albums;")
        return [Album(row["id"], row["title"], row["release_year"], row["artist_id"]) for row in rows]

    def find(self, id):
        rows = self._connection.execute(f"SELECT * FROM albums WHERE id = {id};")
        return [Album(row["id"], row["title"], row["release_year"], row["artist_id"]) for row in rows]
