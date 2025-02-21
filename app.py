'''
Entry point to music library application.
'''

from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

class Application:
    '''
    Runs the music library application
    '''
    def __init__(self) -> None:
        '''
        Initialises the connection to the database
        and seeds the database with data
        '''
        # Connect to the database
        self._connection = DatabaseConnection()
        self._connection.connect()
        # Seed with some seed data
        self._connection.seed("seeds/music_library.sql")

    def run(self) -> None:
        '''
        Retrieves artists and albums from the database
        Prints all artists and albums to the terminal.
        '''
        # Retrieve all artists
        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()

        # List them out
        for artist in artists:
            print(f"{artist.id}: {artist.name} ({artist.genre})")

        # Retrieve all albums
        album_repository: AlbumRepository = AlbumRepository(self._connection)
        albums = album_repository.all()

        # List the albums
        for album in albums:
            print(album)

if __name__ == '__main__':
    app = Application()
    app.run()
