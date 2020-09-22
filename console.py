import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repo as album_repo
import repositories.artist_repo as artist_repo

album_repo.delete_all()
artist_repo.delete_all()

artist_1 = Artist('Michael', 'Jackson')
artist_repo.save(artist_1)

artist_2 = Artist('Bullet for ', 'my Valentine')
artist_repo.save(artist_2)

artist_3 = Artist('Britney', 'Spears')
artist_repo.save(artist_3)

album_1 = Album('Thriller', 'Pop', artist_1)
album_repo.save(album_1)

album_2 = Album('Fever', 'Emo', artist_2)
album_repo.save(album_2)

album_3 = Album ('In the Zone', 'Pop', artist_3)
album_repo.save(album_3)

album_4 = Album("Scream Aim Fire", "Emo", artist_2)
album_repo.save(album_4)

res = album_repo.select_all()
for album in res:
    print(album.__dict__)

res = artist_repo.select_all()
for artist in res:
    print(artist.__dict__)

res = artist_repo.albums(artist_2)
for album in res:
    print(album.__dict__)

res = album_repo.artist(album_1)
print(res.__dict__)

artist_4 = Artist("Mikey", "Boy", 1)
artist_repo.update(artist_4)
res = artist_repo.select_all()
for artist in res:
    print(artist.__dict__)

album_repo.delete(1)
res = album_repo.select_all()
for album in res:
    print(album.__dict__)

found_artist = artist_repo.select(2)
print(found_artist.__dict__)




# pdb.set_trace()