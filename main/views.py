from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Project, Experience, Education, Certification, Skill

def home(request):
    experiences = Experience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-start_date')
    certifications = Certification.objects.all().order_by('-date_obtained')
    skills = Skill.objects.all()
    technical_skills = skills.filter(category='technical')
    soft_skills = skills.filter(category='soft')
    languages = skills.filter(category='language')
    context = {
        'experiences': experiences,
        'educations': educations,
        'certifications': certifications,
        'technical_skills': technical_skills,
        'soft_skills': soft_skills,
        'languages': languages,
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Simulation d'envoi
        messages.success(request, 'Message envoyé avec succès! (Simulation)')
        return render(request, 'home.html', context)
    return render(request, 'home.html', context)
