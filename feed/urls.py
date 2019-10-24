from django.urls import path, re_path
from .views import (
    EventListView, 
    EventCreateView,
    EventUpdateView,
)
from . import views

urlpatterns = [
    path('', EventListView.as_view(), name='mainview'),
    path('event/new', EventCreateView.as_view(), name='create'),
    path('event/details/<int:pk>/update', EventUpdateView.as_view(), name='update'),
    #path('', views.index, name='mainview'),
    #path('event/<int:pk>/', EventDetailView.as_view(), name='details'),
    re_path(r'^event/details/(?P<id>\d+)/$', views.details, name='details'),
]