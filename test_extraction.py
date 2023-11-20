import unittest
from extraction import extract_time_from_message

class TestExtractTimeFromMessage(unittest.TestCase):

    def test_minutes(self):
        message = "in 40 minutes"
        result, matched_str = extract_time_from_message(message)
        self.assertEqual(result, 2400)
        self.assertEqual(matched_str, "in 40 minutes")

    def test_hours_and_minutes(self):
        message = "be back in 1h 50"
        result, matched_str = extract_time_from_message(message)
        self.assertEqual(result, 6600)
        self.assertEqual(matched_str, "in 1h 50")

    def test_seconds(self):
        message = "brb in 60 secs"
        result, matched_str = extract_time_from_message(message)
        self.assertEqual(result, 60)
        self.assertEqual(matched_str, "in 60 secs")

    def test_mins(self):
        message = "in 4 mins"
        result, matched_str = extract_time_from_message(message)
        self.assertEqual(result, 240)
        self.assertEqual(matched_str, "in 4 mins")

    def test_time_range(self):
        message = "in 30-40 minutes"
        result, matched_str = extract_time_from_message(message)
        self.assertEqual(result, 2400) # Using the maximum value in the range (40 minutes)
        self.assertEqual(matched_str, "in 30-40 minutes")

    def test_invalid_format(self):
        message = "invalid format"
        result, matched_str = extract_time_from_message(message)
        self.assertIsNone(result)
        self.assertIsNone(matched_str)

    def test_hours_only(self):
        message = "brb in 2 hours"
        result, matched_str = extract_time_from_message(message)
        self.assertEqual(result, 7200)
        self.assertEqual(matched_str, "in 2 hours")

    def test_minutes_only(self):
        message = "be back in 15 mins"
        result, matched_str = extract_time_from_message(message)
        self.assertEqual(result, 900)
        self.assertEqual(matched_str, "in 15 mins")

    def test_hours_with_invalid_minutes(self):
        message = "brb 2h invalid"
        result, matched_str = extract_time_from_message(message)
        self.assertEqual(result, 7200)
        self.assertEqual(matched_str, "brb 2h")

    def test_zero_time(self):
        message = "brb in 0 mins"
        result, matched_str = extract_time_from_message(message)
        self.assertEqual(result, 0)
        self.assertEqual(matched_str, "in 0 mins")

    def test_mixed_case(self):
        message = "Be Back In 1H 30 MinS"
        result, matched_str = extract_time_from_message(message)
        self.assertEqual(result, 5400)
        self.assertEqual(matched_str, "in 1h 30")

    def test_with_additional_minutes(self):
        message = "brb in 2h 30"
        result, matched_str = extract_time_from_message(message)
        self.assertEqual(result, 9000)
        self.assertEqual(matched_str, "in 2h 30")

    def test_multiple_time_patterns(self):
        message = "brb in 1h 30 for 20 mins"
        result, matched_str = extract_time_from_message(message)
        self.assertEqual(result, 5400)
        self.assertEqual(matched_str, "in 1h 30")

    def test_give_me_string(self):
        message = "give me 1 hour 58"
        result, matched_str = extract_time_from_message(message)
        self.assertEqual(result, 7080)
        self.assertEqual(matched_str, "give me 1 hour 58")

if __name__ == '__main__':
    unittest.main()

