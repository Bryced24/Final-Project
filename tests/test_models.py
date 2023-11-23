import unittest
from models import Event

class TestEvent(unittest.TestCase):

    def setUp(self):
        self.sample_event = Event("Sample Event", "12-25-2023", "Sample Location", "This is a sample description.")

    def test_to_dict(self):
        expected = {
            "title": "Sample Event",
            "date": "12-25-2023",
            "location": "Sample Location",
            "description": "This is a sample description."
        }
        self.assertEqual(self.sample_event.to_dict(), expected)

    def test_validate_date(self):
        self.assertTrue(Event.validate_date("12-31-2023"))
        self.assertFalse(Event.validate_date("2023-12-31"))

if __name__ == '__main__':
    unittest.main()
