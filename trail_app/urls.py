from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('', views.index, name='login'),
path('state/', views.state_list, name = 'state-list'),
path('state/<int:pk>', views.state_detail, name = 'state-detail'),

path('state/user/<int:pk>', views.user_state_detail, name = 'user-state-detail'),

path('state/trail_form/<int:pk>', views.createTrail, name = 'trail-form'),
path('trail/<int:pk>/delete/', login_required(views.TrailDeleteView.as_view()), name='trail-delete'),
path('trail/<int:pk>/UPDATE/', login_required(views.TrailUpdateView.as_view()), name='trail-update'),
path('state/trail/<int:pk>', views.trail_detail, name = 'trail-detail'),
path('accounts/', include('django.contrib.auth.urls')),
path('accounts/register', views.register, name = 'register_page'),

path('accounts/logout/', views.logout_view, name='logout'),
]
