from lib.album import Album

'''Constructs with fields'''
def test_album_constructs():
    album = Album(1, 'The White Album', 1968, 1)
    assert album.id == 1
    assert album.title == 'The White Album'
    assert album.release_year == 1968
    assert album.artist_id == 1


'''Construct with equality'''
def test_albums_are_equal():
    album1 = Album(1, 'Test Title', 1968, 3)
    album2 = Album(1, 'Test Title', 1968, 3)
    
    assert album1 == album2
    
    
'''Constructs so it looks pretty'''
def test_albums_format_nicely():
    album = Album(1, 'Test Title', 1968, 3)
    assert str(album) == "Album(1, Test Title, 1968, 3)"