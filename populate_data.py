import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Experience, Education, Certification, Skill
from datetime import date

# Expériences
Experience.objects.create(
    title='Analyste SOC Senior',
    company='TechSecure Inc.',
    start_date=date(2022, 1, 1),
    description='Responsable de la surveillance des menaces, réponse aux incidents et automatisation des processus de sécurité.'
)
# Ajouter les autres expériences, formations, etc.
print('Données ajoutées !')