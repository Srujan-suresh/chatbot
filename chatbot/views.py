from django.shortcuts import render
from .forms import LeadForm
from django.views.decorators.csrf import ensure_csrf_cookie


def chat_home(request):
    return render(request, 'chat_home.html')


def chatbot_view(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')
    else:
        form = LeadForm()
    return render(request, 'chatbot.html', {'form': form})



@ensure_csrf_cookie
def chatbot_widget(request):
    return render(request, 'chatbot/widget.html')
