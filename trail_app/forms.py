from django.forms import ModelForm
from .models import Trail, State
class TrailForm(ModelForm):
    class Meta:
        model = Trail
        fields = ('name', 'state', 'location', 'zip_code', 'temperature', 'weather', 'description', 'image', 'is_active', )