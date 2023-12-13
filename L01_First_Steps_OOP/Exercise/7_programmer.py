class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if self.language == language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        if self.skills >= skills_needed:
            if self.language != new_language:
                previous_language = self.language
                self.language = new_language
                return f"{self.name} switched from {previous_language} to {new_language}"
            else:
                return f"{self.name} already knows {self.language}"
        else:
            needed_skills = skills_needed - self.skills
            return f"{self.name} needs {needed_skills} more skills"

programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))

# Create a class called Programmer. Upon initialization, it should receive - name (string), language (string),
# and skills (integer). The class should have two methods:
#     • watch_course(course_name, language, skills_earned)
#         ◦ If the programmer language is the same as the one on the course,
# increase his skills with the given amount and return a message "{name} watched {course_name}".)
#         ◦ Otherwise return "{name} does not know {language}".
#     • change_language(new_language, skills_needed)
#         ◦ If the programmer has the skills and the new language is not the same as his,
# change his language to the new one and return "{name} switched from {previous_language} to {new_language}".
#         ◦ If the programmer has the skills, but the given language is equal to his
# return "{name} already knows {language}".
#         ◦ In the last case, the programmer does not have enough skills, so
# return "{name} needs {needed_skills} more skills" and do not change his language.
#
# Output:
# John does not know Python
# John already knows Java
# John needs 50 more skills
# John watched Java: zero to hero
# John switched from Java to Python
# John watched Python Masterclass