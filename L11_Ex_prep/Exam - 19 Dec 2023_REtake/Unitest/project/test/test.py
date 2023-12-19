import unittest
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(unittest.TestCase):

    def setUp(self):
        self.robot1 = ClimbingRobot('Mountain', 'Arm', 100, 200)
        self.robot2 = ClimbingRobot('Alpine', 'Leg', 150, 150)
        self.sample_software = {'name': 'RouteFinder', 'capacity_consumption': 50, 'memory_consumption': 100}
        self.large_software = {'name': 'AdvancedMapping', 'capacity_consumption': 200, 'memory_consumption': 250}

    def test_category_valid(self):
        self.assertEqual(self.robot1.category, 'Mountain')
        self.assertEqual(self.robot2.category, 'Alpine')

    def test_category_invalid(self):
        with self.assertRaises(ValueError):
            ClimbingRobot('Underwater', 'Arm', 100, 200)

    def test_get_used_capacity_initial(self):
        self.assertEqual(self.robot1.get_used_capacity(), 0)

    def test_get_available_capacity_initial(self):
        self.assertEqual(self.robot1.get_available_capacity(), 100)

    def test_get_used_memory_initial(self):
        self.assertEqual(self.robot1.get_used_memory(), 0)

    def test_get_available_memory_initial(self):
        self.assertEqual(self.robot1.get_available_memory(), 200)

    def test_install_software(self):
        result = self.robot1.install_software(self.sample_software)
        self.assertIn("successfully installed", result)
        self.assertEqual(self.robot1.get_used_capacity(), 50)
        self.assertEqual(self.robot1.get_used_memory(), 100)
        self.assertEqual(self.robot1.get_available_capacity(), 50)
        self.assertEqual(self.robot1.get_available_memory(), 100)

    def test_install_software_insufficient_capacity(self):
        result = self.robot1.install_software(self.large_software)
        self.assertIn("cannot be installed", result)
        self.assertEqual(self.robot1.get_used_capacity(), 0)
        self.assertEqual(self.robot1.get_used_memory(), 0)

    def test_install_software_insufficient_memory(self):
        self.sample_software['memory_consumption'] = 300
        result = self.robot1.install_software(self.sample_software)
        self.assertIn("cannot be installed", result)
        self.assertEqual(self.robot1.get_used_capacity(), 0)
        self.assertEqual(self.robot1.get_used_memory(), 0)

    def test_install_multiple_software(self):
        self.robot1.install_software(self.sample_software)
        result = self.robot1.install_software({
            'name': 'PowerOptimizer',
            'capacity_consumption': 30,
            'memory_consumption': 50
        })
        self.assertIn("successfully installed", result)
        self.assertEqual(self.robot1.get_used_capacity(), 80)
        self.assertEqual(self.robot1.get_used_memory(), 150)
        self.assertEqual(self.robot1.get_available_capacity(), 20)
        self.assertEqual(self.robot1.get_available_memory(), 50)


if __name__ == '__main__':
    unittest.main()
