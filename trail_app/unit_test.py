from django.test import TestCase, testcases
from django.contrib.auth.models import User
from trail_app.models import *
from django.urls import reverse
from trail_app.forms import *
class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password = "!QAZxsw2") 
        state = State.objects.create(name='Test State')

        self.trail = Trail.objects.create(
        name='Test Trail',
        state=state,
        location='Test Location',
        zip_code=12345,
        temperature=25,
        weather='Sunny',
        description='Test Description',
        image=r'C:\Users\Craig Lillemon\cs3300project\trail_app\static\images\cs3300Project.jpg',
        is_active=True,
        )
    def test_trail_fields(self):
        self.assertEqual(self.trail.name, 'Test Trail')
        self.assertEqual(self.trail.state.name, 'Test State')
        self.assertEqual(self.trail.location, 'Test Location')
        self.assertEqual(self.trail.zip_code, 12345)
        self.assertEqual(self.trail.temperature, 25)
        self.assertEqual(self.trail.weather, 'Sunny')
        self.assertEqual(self.trail.description, 'Test Description')
        self.assertEqual(self.trail.image, r'C:\Users\Craig Lillemon\cs3300project\trail_app\static\images\cs3300Project.jpg')
        self.assertTrue(self.trail.is_active)

