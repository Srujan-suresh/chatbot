from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat_home'),              # Homepage
    path('chat/', views.chatbot_view, name='chat'),           # FIXED: Now points to the correct function
   
]



