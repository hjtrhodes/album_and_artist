from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection
from lib.album_repository import AlbumRepository
    
connection = DatabaseConnection()
connection.connect()
connection.seed("seeds/music_library.sql")

artist_repository = ArtistRepository(connection)
album_repository = AlbumRepository(connection)

find_with_album = artist_repository.find_with_albums(1)
print(find_with_album)