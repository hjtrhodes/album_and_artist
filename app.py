from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        user_task = input(('Please enter: all, find, create or delete - '))
        if user_task == 'all':
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()
            for artist in artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")
        else:
            pass

if __name__ == '__main__':
    app = Application()
    app.run()