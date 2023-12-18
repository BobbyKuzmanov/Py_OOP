import unittest
from project.truck_driver import TruckDriver


class TestTruckDriver(unittest.TestCase):

    def setUp(self):
        self.driver_one = TruckDriver('John', 1.5)
        self.driver_two = TruckDriver('Jane', 2.0)
        self.driver_three = TruckDriver('Alex', 2.5)

    def test_initialization(self):
        self.assertEqual(self.driver_one.name, 'John')
        self.assertEqual(self.driver_one.money_per_mile, 1.5)
        self.assertEqual(self.driver_one.available_cargos, {})
        self.assertEqual(self.driver_one.earned_money, 0)
        self.assertEqual(self.driver_one.miles, 0)

    def test_negative_earned_money(self):
        with self.assertRaises(ValueError) as ve:
            self.driver_three.earned_money = -100
        self.assertEqual("Alex went bankrupt.", str(ve.exception))

    def test_add_cargo_offer(self):
        result = self.driver_one.add_cargo_offer('New York', 500)
        self.assertEqual(result, 'Cargo for 500 to New York was added as an offer.')
        self.assertIn('New York', self.driver_one.available_cargos)
        self.assertEqual(self.driver_one.available_cargos['New York'], 500)

    def test_duplicate_cargo_offer(self):
        self.driver_one.add_cargo_offer('New York', 500)
        with self.assertRaises(Exception):
            self.driver_one.add_cargo_offer('New York', 1000)

    def test_drive_best_cargo_offer(self):
        self.driver_three.add_cargo_offer('Los Angeles', 1200)
        self.driver_three.add_cargo_offer('New York', 3000)
        result = self.driver_three.drive_best_cargo_offer()
        self.assertEqual(result, 'Alex is driving 3000 to New York.')
        self.assertEqual(self.driver_three.earned_money, 6125.0)
        self.assertEqual(self.driver_three.miles, 3000)

    def test_drive_best_cargo_offer_with_no_offers(self):
        result = self.driver_three.drive_best_cargo_offer()
        self.assertEqual(result, 'There are no offers available.')

    def test_eat_every_250_miles(self):
        self.driver_one.add_cargo_offer('New York', 250)
        self.driver_one.drive_best_cargo_offer()
        self.assertEqual(self.driver_one.earned_money, 375 - 20)

    def test_sleep_every_1000_miles(self):
        self.driver_two.add_cargo_offer('Austin', 1000)
        self.driver_two.drive_best_cargo_offer()
        self.assertEqual(self.driver_two.earned_money, 1875.0)

    def test_pump_gas_every_1500_miles(self):
        self.driver_one.add_cargo_offer('Chicago', 1500)
        self.driver_one.drive_best_cargo_offer()
        self.assertEqual(self.driver_one.earned_money, 1585.0)

    def test_repair_truck_every_10000_miles(self):
        self.driver_three.add_cargo_offer('Seattle', 10000)
        self.driver_three.drive_best_cargo_offer()
        self.assertEqual(self.driver_three.earned_money, 13250.0)

    def test_combo_activities_costs(self):
        self.driver_two.add_cargo_offer('Multiple', 10000)
        self.driver_two.drive_best_cargo_offer()
        expected_earnings = 8250.0
        self.assertEqual(self.driver_two.earned_money, expected_earnings)

    def test_repr(self):
        self.driver_one.add_cargo_offer('Paris', 10000)
        self.driver_one.drive_best_cargo_offer()
        expected_repr = "John has 10000 miles behind his back."
        self.assertEqual(self.driver_one.__repr__(), expected_repr)



if __name__ == '__main__':
    unittest.main()
