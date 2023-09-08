from django.test import TestCase
from .models import Tag, ToDo
from datetime import datetime, date
from django.contrib.auth import get_user_model
from .forms import ToDoForm

User = get_user_model()
# Create your tests here.


class TagTestCase(TestCase):
    def setUp(self) -> None:
        self.first_tag = Tag.objects.create(name="Urgent")

    def test_tag_str(self):
        self.assertEqual(str(self.first_tag), self.first_tag.name)

    def test_tag_name(self):
        self.assertEqual("Urgent", self.first_tag.name)

    def tearDown(self) -> None:
        del self.first_tag


class ToDoTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username="suren", email="suren@gmail.com", password="123456"
        )
        self.first_todo = ToDo.objects.create(
            start_date=datetime.now(),
            end_date=datetime.now(),
            title="Test1",
            description="Desc1",
            todo_type="1",
            active=True,
            user=self.user,
        )
        self.second_todo = ToDo.objects.create(
            start_date=datetime.now(),
            end_date=datetime.now(),
            title="Test1",
            description="Desc1",
            todo_type="1",
            user=self.user,
        )

    def test_todo_active(self):
        self.assertEqual(self.first_todo.active, True)

    def test_todo_str(self):
        self.assertEqual(
            f"{self.first_todo.title} {self.first_todo.description}",
            str(self.first_todo),
        )

    def test_todo_missed_field_description(self):
        ToDo.objects.create(
            start_date=datetime.now(),
            end_date=datetime.now(),
            title="Test1",
            todo_type="1",
            active=True,
            user=self.user,
        )

    def test_todo_deafult_active(self):
        self.assertEqual(self.second_todo.active, False)

    def tearDown(self) -> None:
        del self.user
        del self.first_todo


class ToDoFormTestCase(TestCase):
    def setUp(self) -> None:
        self.form = ToDoForm()

    def test_form_labels(self):
        self.assertTrue(
            self.form.fields["todo_type"].label is None
            or self.form.fields["todo_type"].label == "todo type"
        )

    def test_form_start_date(self):
        form = ToDoForm(data={"start_date": datetime.now()})
        self.assertFalse(form.is_valid())

    def test_form_start_date2(self):
        form = ToDoForm(data={"start_date": datetime.now(), "end_date": datetime.now(), "todo_type": "2", "title": "title", "description": "test"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["start_date"], date.today())

    def tearDown(self) -> None:
        del self.form
