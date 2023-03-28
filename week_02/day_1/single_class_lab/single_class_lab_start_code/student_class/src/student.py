
class Student:
    def __init__(self, get_name, get_cohort):
        self.name = get_name
        self.cohort = get_cohort

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, language):
        return f"I love {language}"

