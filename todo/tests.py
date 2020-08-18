from django.test import TestCase
from .models import Todo

# Create your tests here.


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="Setup development environment",completed=True)
        Todo.objects.create(title="Develop website and add content")

    def test_first_todo(self):
        todo=Todo.objects.get(id=1)
        title = f'{todo.title}'
        completed=f'{todo.completed}'

        self.assertEqual(title,'Setup development environment')
        self.assertTrue(completed)
    
    def test_first_todo(self):
        todo=Todo.objects.get(id=2)
        title = f'{todo.title}'
        completed=f'{todo.completed}'

        self.assertEqual(title,'Develop website and add content')  
        self.assertEqual(completed,'False')
    