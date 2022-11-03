import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from course.models import Course


class CourseTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="testuser",
            password="12345",
        )
        Course.objects.create(name="Python", code=123, owner=self.test_user)
        Course.objects.create(name="Docker", code=789, owner=self.test_user)

        course_test_num = 20
        self.mock_names = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(course_test_num)
        ]
        self.mock_codes = [
            int(
                "".join(
                    [
                        random.choice((string.digits))
                        for _ in range(random.randint(3, 9))
                    ]
                )
            )
            for _ in range(course_test_num)
        ]

        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            Course.objects.create(name=mock_name, code=mock_code, owner=self.test_user)

    def test_course_model(self):
        """Courses creation are correctly identified"""
        python_course = Course.objects.get(name="Python")
        docker_course = Course.objects.get(name="Docker")
        self.assertEqual(python_course.owner.username, "testuser")
        self.assertEqual(docker_course.owner.username, "testuser")
        self.assertEqual(python_course.code, 123)
        self.assertEqual(docker_course.code, 789)

    def test_course_list(self):
        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            course_test = Course.objects.get(name=mock_name)
            self.assertEqual(course_test.owner.username, "testuser")
            self.assertEqual(course_test.code, mock_code)
