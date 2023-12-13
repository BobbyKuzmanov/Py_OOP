import unittest

from project.student import Student

class TestStudentClass(unittest.TestCase):

    def setUp(self):
        self.student = Student("John")

    def test_enroll_new_course(self):
        result = self.student.enroll("Math", [90, 85, 88])
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses["Math"], [90, 85, 88])

    def test_enroll_existing_course_update_notes(self):
        self.student.enroll("Math", [90, 85, 88])
        result = self.student.enroll("Math", [95, 92], "Y")
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses["Math"], [90, 85, 88, 95, 92])

    def test_enroll_existing_course_no_update_notes(self):
        self.student.enroll("Math", [90, 85, 88])
        result = self.student.enroll("Math", [95, 92], "N")
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses["Math"], [90, 85, 88])  # Notes should not be updated

    def test_add_notes_existing_course(self):
        self.student.enroll("Math", [90, 85, 88])
        result = self.student.add_notes("Math", 92)
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.student.courses["Math"], [90, 85, 88, 92])

    def test_add_notes_non_existing_course(self):
        with self.assertRaises(Exception):
            self.student.add_notes("Physics", 75)

    def test_leave_course_existing_course(self):
        self.student.enroll("Math", [90, 85, 88])
        result = self.student.leave_course("Math")
        self.assertEqual(result, "Course has been removed")
        self.assertNotIn("Math", self.student.courses)

    def test_leave_course_non_existing_course(self):
        with self.assertRaises(Exception):
            self.student.leave_course("Physics")

if __name__ == '__main__':
    unittest.main()
