import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

#Delete all Artists / Albums
album_repository.delete_all()
artist_repository.delete_all()

#Create and Save Artist
artist_1 = Artist("Moderat")
artist_repository.save(artist_1)

#Create and Save Albums
album_1 = Album("Moderat", "Electronic", artist_1)
album_repository.save(album_1)
album_2 = Album("II", "Electronic", artist_1)
album_repository.save(album_2)
album_3 = Album("III", "Electronic", artist_1)
album_repository.save(album_3)

#Find Artists/Albums by their ID (select)
#print(album_repository.select(album_2.id))

#List All Artists
all_artists = artist_repository.select_all()
for artist in all_artists:
    print(artist.__dict__)

#List All Artists/Albums
all_albums = album_repository.select_all()
for album in all_albums:
    print(album.__dict__)
    print(album.artist.__dict__)

#List all the albums by an artist
#print(artist_repository.albums(artist_1.id))

#Edit Artists/Albums
# album_3 = Album("More D4ta", "Electronic", artist_1)
# album_repository.update(album_3)
# print(album.__dict__)

#Delete Artists/Albums
#albums = album_repository.delete(album_3.id)
#for album in albums:
#    print(album.__dict__)

pdb.set_trace()