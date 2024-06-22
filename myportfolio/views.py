from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail

from .forms import ContactForm


def home(request):
    pass


class Contact(View):
    def get(self, request):
        form = ContactForm()
        return render(request, "contact.html", {"form": form})

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
        return render(request, "contact.html", {'form': form})


def thanks(request):
    return render(request, 'thanks.html')
