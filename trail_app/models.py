from django.db import models
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class TrailFolders(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('portfolio-detail', args=[str(self.id)])
class State(models.Model):
    state_names = (
    ("Alabama", "Alabama"),
    ("Alaska", "Alaska"),
    ("Arizona", "Arizona"),
    ("Arkansas", "Arkansas"),
    ("California", "California"),
    ("Colorado", "Colorado"),
    ("Connecticut", "Connecticut"),
    ("Delaware", "Delaware"),
    ("Florida", "Florida"),
    ("Georgia", "Georgia"),
    ("Hawaii", "Hawaii"),
    ("Idaho", "Idaho"),
    ("Illinois", "Illinois"),
    ("Indiana", "Indiana"),
    ("Iowa", "Iowa"),
    ("Kansas", "Kansas"),
    ("Kentucky", "Kentucky"),
    ("Louisiana", "Louisiana"),
    ("Maine", "Maine"),
    ("Maryland", "Maryland"),
    ("Massachusetts", "Massachusetts"),
    ("Michigan", "Michigan"),
    ("Minnesota", "Minnesota"),
    ("Mississippi", "Mississippi"),
    ("Missouri", "Missouri"),
    ("Montana", "Montana"),
    ("Nebraska", "Nebraska"),
    ("Nevada", "Nevada"),
    ("New Hampshire", "New Hampshire"),
    ("New Jersey", "New Jersey"),
    ("New Mexico", "New Mexico"),
    ("New York", "New York"),
    ("North Carolina", "North Carolina"),
    ("North Dakota", "North Dakota"),
    ("Ohio", "Ohio"),
    ("Oklahoma", "Oklahoma"),
    ("Oregon", "Oregon"),
    ("Pennsylvania", "Pennsylvania"),
    ("Rhode Island", "Rhode Island"),
    ("South Carolina", "South Carolina"),
    ("South Dakota", "South Dakota"),
    ("Tennessee", "Tennessee"),
    ("Texas", "Texas"),
    ("Utah", "Utah"),
    ("Vermont", "Vermont"),
    ("Virginia", "Virginia"),
    ("Washington", "Washington"),
    ("West Virginia", "West Virginia"),
    ("Wisconsin", "Wisconsin"),
    ("Wyoming", "Wyoming")
    )
    
    state = models.CharField(max_length = 200, choices=state_names, blank = False)
    list_state = models.BooleanField(default=False)
    #about = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.state
    def get_absolute_url(self):
        return reverse('state-detail', args=[str(self.id)])
class Trail(models.Model):
    name = models.CharField(max_length=200, blank=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    location = models.CharField(max_length=200, blank=False)
    zip_code = models.IntegerField(blank=False)
    temperature = models.IntegerField()
    weather = models.TextField()
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='images/', blank=False)
    is_active = models.BooleanField(default=False)
   
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('trail-detail', args=[str(self.id)])
    

class User(models.Model):
    name = models.CharField(max_length=200)
    trailFolder = models.OneToOneField(TrailFolders, on_delete=models.CASCADE)
    manager = models.OneToOneField(User, null = True, on_delete= models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('portfolio-detail', args=[str(self.id)])
#List of choices for major value in database, human readable name
   
    #email = models.CharField("UCCS Email", max_length=200, blank =  False)
    #password = models.CharField("Password", max_length=200, blank = False)
    #def __str__(self):
    #    return self.name
    #def get_absolute_url(self):
    #    return reverse('user-detail', args=[str(self.id)])
    #state = models.OneToOneField(State, null=True, on_delete=models.CASCADE, unique=True)
    



class StateListView(generic.ListView):
    model = State
class StateDetailView(generic.DetailView):
    model = State

class TrailListView(generic.ListView):
    model = Trail
class TrailDetailView(generic.DetailView):
    model = Trail


class TrailUpdateView(generic.UpdateView):
    model =Trail
    fields = ('name', 'state', 'location', 'zip_code', 'temperature', 'weather', 'description', 'image', 'is_active', )
    success_url = reverse_lazy('state-list')
    template_name = 'trail_app/trail_update.html'
class TrailDeleteView(generic.DeleteView):
    model = Trail
    success_url = reverse_lazy('state-list')  # Redirect to home after deletion
    template_name = 'trail_app/trail_confirm_delete.html'


class ManagerAssessmentRecord(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.manager.username}-Score:{self.score}"
