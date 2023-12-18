# concert_tracker_app.py
from project.band_members.singer import Singer
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ["Singer", "Drummer", "Guitarist"]:
            raise ValueError("Invalid musician type!")

        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")

        musician = None
        if musician_type == "Singer":
            musician = Singer(name, age)
        elif musician_type == "Drummer":
            musician = Drummer(name, age)
        elif musician_type == "Guitarist":
            musician = Guitarist(name, age)

        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next((m for m in self.musicians if m.name == musician_name), None)
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")

        band = next((b for b in self.bands if b.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = next((b for b in self.bands if b.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        if musician_name not in [m.name for m in band.members]:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members = [m for m in band.members if m.name != musician_name]
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next((b for b in self.bands if b.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        singer = next((m for m in band.members if isinstance(m, Singer)), None)
        drummer = next((m for m in band.members if isinstance(m, Drummer)), None)
        guitarist = next((m for m in band.members if isinstance(m, Guitarist)), None)

        if singer is None or drummer is None or guitarist is None:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if band.genre == "Rock":
            required_skills = {"Drummer": "play the drums with drumsticks", "Singer": "sing high pitch notes", "Guitarist": "play rock"}
        elif band.genre == "Metal":
            required_skills = {"Drummer": "play the drums with drumsticks", "Singer": "sing low pitch notes", "Guitarist": "play metal"}
        elif band.genre == "Jazz":
            required_skills = {"Drummer": "play the drums with drum brushes", "Singer": "sing high pitch notes and sing low pitch notes", "Guitarist": "play jazz"}
        else:
            raise ValueError("Invalid concert genre!")

        for musician in band.members:
            if not set(required_skills[musician.__class__.__name__]).issubset(set(musician.skills)):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = round((band.concert.audience * band.concert.ticket_price) - band.concert.expenses, 2)
        return f"{band_name} gained {profit}$ from the {band.concert.genre} concert in {concert_place}."
