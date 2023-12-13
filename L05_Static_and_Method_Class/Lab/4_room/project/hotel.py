class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @staticmethod
    def from_stars(stars_count: int):
        return f"{stars_count} stars Hotel"

    def add_room(self, room: "Room"):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        result = room.take_room(people)
        if not result:
            self.guests += people

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        result = room.free_room()
        if result:
            self.guests -= room.guests

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join([str(r.number) for r in self.rooms if not r.is_taken])}\n" \
               f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken])}"

# In the hotel.py file, create a class called Hotel. Upon initialization,
# it should receive a name (str).
# It should also have 2 more attributes: rooms (empty list of rooms) and guests (0 by default).
# The class should have 5 more methods:
#     • from_stars(stars_count: int) - creates a new instance with name "{stars_count} stars Hotel"
#     • add_room(room: Room) - adds the room to the list of rooms
#     • take_room(room_number, people)
#     - finds the room with that number and tries to accommodate the guests in the room
#     • free_room(room_number) - finds the room with that number and tries to free it
#     • status() - returns information about the hotel in the following format:
# "Hotel {name} has {guests} total guests
# Free rooms: {numbers of all free rooms separated by comma and space}
# Taken rooms: {numbers of all taken rooms separated by comma and space}"