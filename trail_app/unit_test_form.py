from django.test import TestCase, testcases
from django.contrib.auth.models import User
from trail_app.models import *
from django.urls import reverse
from trail_app.forms import *
class TrailFormCreation(TestCase):
    def valid_form(self):
        state = State.objects.create(name='Test State')
        data = {'name': 'namesd', 'state':state, 'location':'somwhere', 'zip_code':80919, 'temperature':25, 'weather':'sunny', 'image': r'C:\Users\Craig Lillemon\cs3300project\trail_app\static\images\cs3300Project.jpg', 'is_active':True}
        form = TrailForm(data=data)
        self.assertTrue(form.is_valid())
    def failed_form(self):
        data= {'name':''}
        form = TrailForm(data=data)
        state = State.objects.create(name='Test State')
        self.assertTrue(form.is_valid())
        self.assertFalse(form.is_valid()) and self.assertIn('state', form.errors)
    def failed_form2(self):
        data= {'name': 'namesd', 'state':state, 'location':'somwhere', 'zip_code':80919, 'temperature':25, 'weather':'sunny', 'image': r'C:\Users\Craig Lillemon\cs3300project\trail_app\static\images\cs3300Project.jpg'}
        form = TrailForm(data=data)
        state = State.objects.create(name='Test State')
        self.assertTrue(form.is_valid())
        self.assertFalse(form.is_valid()) and self.assertIn('is_active', form.errors)