'''
Test file for album repository
'''
from lib.album_repository import AlbumRepository
from lib.album import Album

def test_get_all_albums_from_database(db_connection):
    '''
    When we call #all, we get all the albums in the database as instances.
    '''
    db_connection.seed('seeds/music_library.sql')
    repo = AlbumRepository(db_connection)
    result = repo.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]

def test_find_single_album_by_id(db_connection):
    '''
    When we call #find, we get a signle album instance returned to us.
    '''
    db_connection.seed('seeds/music_library.sql')
    repo = AlbumRepository(db_connection)
    result = repo.find(1)
    assert result == [Album(1, 'Doolittle', 1989, 1)]
