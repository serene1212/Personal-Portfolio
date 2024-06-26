from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail

from .forms import ContactForm
from .models import *


class Home(View):
    def get(self, request):
        form = ContactForm()
        contexts = {'form': form}

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            send_mail(
                f'Message from {name}',
                message,
                email,
                ['arshiarezagholi1212@gmail.com'],
            )
            return redirect('thanks')
        return render(request, "index.html", {'form': form})


def thanks(request):
    return render(request, 'thanks.html')
