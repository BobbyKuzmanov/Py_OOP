from unittest import TestCase, main

from extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.integer_list = IntegerList(
            '50',
            1,
            False,
            2,
            3
        )

    def test_correct_initialization(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_operation_adds_integers_to_the_list(self):
        expected_data = self.integer_list.get_data() + [5]
        actual_data = self.integer_list.add(5)
        self.assertEqual(expected_data, actual_data)

    def test_add_operation_with_float_elements_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add(5.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_operation_without_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(100)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_with_valid_index_removes_element(self):
        expected = [1, 3]
        deleted_element = 2
        actual_deleted_element = self.integer_list.remove_index(1)
        self.assertEqual(expected, self.integer_list.get_data())
        self.assertEqual(deleted_element, actual_deleted_element)

    def test_get_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(100)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_with_valid_index_returns_correct_element(self):
        expected = 2
        actual = self.integer_list.get(1)
        self.assertEqual(expected, actual)

    def test_insert_on_valid_index_inserts_expected_inserted_element(self):
        expected_list = [1, 2, 4, 3]
        self.integer_list.insert(len(self.integer_list.get_data()) - 1, 4)

        self.assertEqual(expected_list, self.integer_list.get_data())

    def test_insert_element_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(100, 5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_float_element_on_valid_index_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(0, 5.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest(self):
        expected = 3
        actual = self.integer_list.get_biggest()
        self.assertEqual(expected, actual)

    def test_get_index(self):
        expected = 1
        actual = self.integer_list.get_index(2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
