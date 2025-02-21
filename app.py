'''
Entry point to music library application.
'''

from os import system, name
import sys

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

    def clear(self) -> None:
        '''
        Function to clear terminal screen.
        '''
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')


    def continue_menu(self) -> ([''] or None):
        '''
        Displays menu asking whether to continue / quit
        '''
        choice = ''
        while choice == '':
            print('\n\nWhat do you want to do?\n')
            print('\tm) Go to main menu')
            print('\n\tq) Quit')
            choice = input('\nChoose an option:\n\t')
            match choice:
                case 'q':
                    sys.exit()
                case 'm':
                    return ''
                case _:
                    choice = ''

    def print_artists(self) -> None:
        '''
        Prints all artists to the terminal
        '''
        self.clear()
        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()

        print('All artists:\n')
        for artist in artists:
            print(f"\t{artist.id}: {artist.name} ({artist.genre})")
        return None

    def print_albums(self)-> None:
        '''
        Prints all albums to the terminal
        '''
        self.clear()
        album_repository: AlbumRepository = AlbumRepository(self._connection)
        albums = album_repository.all()

        print('All albums:\n')
        for album in albums:
            print(f"\t{album.id}: {album.title} ({album.release_year})")
        return None

    def run(self) -> None:
        '''
        Runs application
        '''
        choice = ''
        while choice == '':
            self.clear()
            print('Welcome to the music library manager\n\n')
            print('What would you like to do?')
            print('\t1) List all albums')
            print('\t2) List all artists')
            print('\n\tq) Quit')
            choice = input('\nChoose an option:\n\t')
            match choice:
                case '1':
                    self.print_albums()
                    choice = self.continue_menu()
                case '2':
                    self.print_artists()
                    choice = self.continue_menu()
                case 'q':
                    sys.exit()
                case _:
                    choice = ''


if __name__ == '__main__':
    app = Application()
    app.run()
