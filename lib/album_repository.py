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
        rows = self._connection.execute("SELECT * FROM albums WHERE id = %s;", [id])
        return [Album(row["id"], row["title"], row["release_year"], row["artist_id"]) for row in rows]

    def create(self, album):
        '''
        Method to create (add) an album to the albums table.
        '''
        self._connection.execute("INSERT INTO albums (id, title, release_year, artist_id) VALUES (%s, %s, %s, %s)", [album.id, album.title, album.release_year, album.artist_id])
        return None

    def delete(self, id):
        '''
        Method to delete a row from the albums table, reflecting the given ID.
        '''
        self._connection.execute('DELETE FROM albums WHERE id = %s', [id])
        return None

