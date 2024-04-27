from django.forms import ModelForm
from .models import Trail, State
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TrailForm(ModelForm):
    class Meta:
        model = Trail
        fields = ('name', 'state', 'location', 'zip_code', 'temperature', 'weather', 'description', 'image', 'is_active', )
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']