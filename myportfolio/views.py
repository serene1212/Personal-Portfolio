from django.shortcuts import render, redirect
from django.views import View

from .forms import ContactForm
from .models import *


class Home(View):
    def get(self, request):
        form = ContactForm()
        user = User.objects.first()
        job_experience = user.job_experiences.all()
        educations = user.educations.all()
        skills = user.skills.all()
        interests = user.interests.all()
        courses = user.courses.all()
        projects = user.projects.all()
        contexts = {
            'form': form,
            'job_experiences': job_experience,
            'user': user,
            'educations': educations,
            'skills': skills,
            'interests': interests,
            'courses': courses,
            'projects': projects,

        }
        return render(request, 'myportfolio/index.html', context=contexts)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            Message.objects.create(name=name, email=email, message=message)

            return redirect('thanks')
        return render(request, "myportfolio/index.html", {'form': form})


def thanks(request):
    return render(request, 'myportfolio/thanks.html')
