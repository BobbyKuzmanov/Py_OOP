from math import ceil


class PhotoAlbum:
    PHOTOS_ON_A_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_ON_A_PAGE))

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < PhotoAlbum.PHOTOS_ON_A_PAGE:
                self.photos[page].append(label)

                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"

        return "No more free slots"

    def display(self):
        result = ['-' * 11]

        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append("-" * 11)

        return "\n".join(result)


# Test Code:
album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

# Create a class called PhotoAlbum. Upon initialization, it should receive pages (int).
# It should also have one more attribute: photos (empty matrix) representing the album
# with its pages where you should put the photos.
# Each page can contain only 4 photos. The class should also have 3 more methods:
#     • from_photos_count(photos_count: int) - creates a new instance of PhotoAlbum.
#     Note: Each page can contain 4 photos.
#     • add_photo(label: str) - adds the photo in the first possible page and slot and
# return "{label} photo added successfully on page {page_number(starting from 1)} slot {slot_number(starting from 1)}".
# If there are no free slots left, return "No more free slots"
#     • display() - returns a string representation of each page and the photos in it. Each photo is marked with "[]",
#     and the page separation is made using 11 dashes (-). For example, if we have 1 page and 2 photos:
# -----------
# [] []
# -----------
# and if we have 2 empty pages:
# -----------
#
# -----------
#
# -----------

# Output:
# baby photo added successfully on page 1 slot 1
# first grade photo added successfully on page 1 slot 2
# eight grade photo added successfully on page 1 slot 3
# party with friends photo added successfully on page 1 slot 4
# [['baby', 'first grade', 'eight grade', 'party with friends'], []]
# prom photo added successfully on page 2 slot 1
# wedding photo added successfully on page 2 slot 2
# -----------
# [] [] [] []
# -----------
# [] []
# -----------
