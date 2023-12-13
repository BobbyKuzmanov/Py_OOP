import unittest

from project.railway_station import RailwayStation


class TestRailwayStation(unittest.TestCase):

    def test_name_setter_valid(self):
        station = RailwayStation("Grand Central")
        self.assertEqual(station.name, "Grand Central")

    def test_name_setter_invalid(self):
        with self.assertRaises(ValueError):
            RailwayStation("NY")

    def test_new_arrival_on_board(self):
        station = RailwayStation("Grand Central")
        station.new_arrival_on_board("Train A")
        self.assertIn("Train A", station.arrival_trains)

    def test_train_has_arrived(self):
        station = RailwayStation("Grand Central")
        station.new_arrival_on_board("Train A")
        result = station.train_has_arrived("Train A")
        self.assertEqual(result, "Train A is on the platform and will leave in 5 minutes.")
        self.assertIn("Train A", station.departure_trains)

    def test_train_has_arrived_wrong_order(self):
        station = RailwayStation("Grand Central")
        station.new_arrival_on_board("Train A")
        station.new_arrival_on_board("Train B")
        result = station.train_has_arrived("Train B")
        self.assertEqual(result, "There are other trains to arrive before Train B.")

    def test_train_has_left(self):
        station = RailwayStation("Grand Central")
        station.new_arrival_on_board("Train A")
        station.train_has_arrived("Train A")
        has_left = station.train_has_left("Train A")
        self.assertTrue(has_left)
        self.assertNotIn("Train A", station.departure_trains)

    def test_train_has_left_not_departed(self):
        station = RailwayStation("Grand Central")
        station.new_arrival_on_board("Train A")
        station.train_has_arrived("Train A")
        has_left = station.train_has_left("Train B")
        self.assertFalse(has_left)


# This is to run the tests
if __name__ == '__main__':
    unittest.main()
