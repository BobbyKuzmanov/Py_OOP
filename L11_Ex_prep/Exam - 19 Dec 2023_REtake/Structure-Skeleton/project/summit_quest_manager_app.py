from typing import List

from project.climbers.summit_climber import SummitClimber
from project.climbers.arctic_climber import ArcticClimber
from project.peaks.summit_peak import SummitPeak
from project.peaks.arctic_peak import ArcticPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        valid_types = ["ArcticClimber", "SummitClimber"]
        if climber_type not in valid_types:
            return f"{climber_type} doesn't exist in our register."

        for climber in self.climbers:
            if climber.name == climber_name:
                return f"{climber_name} has been already registered."

        if climber_type == "ArcticClimber":
            climber = ArcticClimber(climber_name)
        else:
            climber = SummitClimber(climber_name)

        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        valid_types = ["ArcticPeak", "SummitPeak"]
        if peak_type not in valid_types:
            return f"{peak_type} is an unknown type of peak."

        if peak_type == "ArcticPeak":
            peak = ArcticPeak(peak_name, peak_elevation)
        else:
            peak = SummitPeak(peak_name, peak_elevation)

        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = next((c for c in self.climbers if c.name == climber_name), None)
        if not climber:
            return f"Climber {climber_name} is not registered yet."

        peak = next((p for p in self.peaks if p.name == peak_name), None)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        recommended_gear = peak.get_recommended_gear()
        missing_gear = sorted(set(recommended_gear) - set(gear))

        if not missing_gear:
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(missing_gear)}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = next((c for c in self.climbers if c.name == climber_name), None)
        if not climber:
            return f"Climber {climber_name} is not registered yet."

        peak = next((p for p in self.peaks if p.name == peak_name), None)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            difficulty_level = peak.calculate_difficulty_level()
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {difficulty_level}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        climbed_peaks = [climber.conquered_peaks for climber in self.climbers if climber.conquered_peaks]
        total_peaks = sum(len(peaks) for peaks in climbed_peaks)

        climbers_stats = sorted(self.climbers, key=lambda x: (len(x.conquered_peaks), x.name), reverse=True)
        climbed_peaks_str = "\n".join([f"{peak}" for peak in climbed_peaks])

        return f"Total climbed peaks: {total_peaks}\n**Climber's statistics:**\n{climbed_peaks_str}"