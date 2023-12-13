from unittest import TestCase, main

from cat import Cat


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Pesho")

    def test_correct_initialization(self):
        self.assertEqual("Pesho", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_feed_cat_expect_fed_and_sleepy_cat_with_increased_size(self):
        expected_result = 1
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(self.cat.size, expected_result)

    def test_feed_test_twice_expect_double_increase_size(self):
        self.cat.eat()
        self.cat.fed = False
        self.assertEqual(2, self.cat.size)

    def test_feed_cat_when_cat_already_fed_raises_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual("Already fed.", str(ex.exception))

    def test_sleeping_cat_when_cat_is_fed_make_cat_not_sleepy(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

    def test_sleepy_cat_not_is_hungry_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))


if __name__ == '__main__':
    main()

# Create the following tests:
#     • The cat's size is increased after eating
#     • Cat is fed after eating
#     • Cat cannot eat if already fed, raises an error
#     • Cat cannot fall asleep if not fed, raises an error
#     • Cat is not sleepy after sleeping
