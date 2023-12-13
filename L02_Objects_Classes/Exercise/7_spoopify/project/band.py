from typing import List
from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)

        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        try:
           album = next(filter(lambda a: a.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."

        if album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album)

        return f"Album {album_name} has been removed."

    def details(self):
        albums = '\n'.join([a.details() for a in self.albums])

        return f"Band {self.name}\n" + \
               f"{albums}"

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34,False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())


# The Band class should receive a name (string) upon initialization. It also has an attribute albums (an empty list).
# The class has three methods:
#     • add_album(album: Album)
#         ◦ Adds an album to the collection and returns "Band {band_name} has added their newest album {album_name}."
#         ◦ If the album is already added, returns "Band {band_name} already has {album_name} in their library."
#     • remove_album(album_name: str)
#         ◦ Removes the album from the collection and returns "Album {name} has been removed."
#         ◦ If the album is published, return "Album has been published. It cannot be removed."
#         ◦ If the album is not in the collection, return "Album {name} is not found."
#     • details()
#         ◦ Returns the information of the band, with their albums, in this format:
# "Band {name}
#  {album details}
#  ...
#  {album details}"