from django.urls import path
from . import views
from .views import chatbot_widget


urlpatterns = [
    path('', views.chat_home, name='chat_home'),              # Homepage
    path('chat/', views.chatbot_view, name='chat'),           # FIXED: Now points to the correct function
   path('chatbot-widget/', chatbot_widget, name='chatbot_widget'),

]



