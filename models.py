from datetime import datetime

class Event:
    def __init__(self, title, date, location, description):
        self.title = title
        self.date = date
        self.location = location
        self.description = description

    def to_dict(self):
        return {
            "title": self.title,
            "date": self.date,
            "location": self.location,
            "description": self.description
        }

    @staticmethod
    def validate_date(date_str):
        try:
            datetime.strptime(date_str, '%m-%d-%Y')
            return True
        except ValueError:
            return False
