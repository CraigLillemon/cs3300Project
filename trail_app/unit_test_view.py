from django.test import TestCase, testcases, Client
from django.contrib.auth.models import User
from trail_app.models import *
from django.urls import reverse
from trail_app.forms import *
class ViewTestCase(TestCase):
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
    def test_index_view(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trail_app/index.html')
    def test_state_detail_view(self):
        client = Client()
        response = client.get(reverse('state-detail', kwargs={'pk': self.state.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trail_app/state_detail.html') 
        
    