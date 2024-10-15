from django.urls import path
from . import views

app_name = 'chatbot'  # This namespacing helps when including multiple apps.

urlpatterns = [
    # URL pattern for the main chatbot interface
    path('', views.index, name='index'),
    
    # URL pattern for sending messages
    path('send_message/', views.send_message, name='send_message'),
    
    # URL pattern for viewing forwarded messages
    path('get_sent_messages/', views.get_sent_messages, name='get_sent_messages'), 
]
