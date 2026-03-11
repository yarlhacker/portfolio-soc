#!/usr/bin/env python
"""
Script pour initialiser les données du portfolio (superuser et données fictives)
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.contrib.auth import get_user_model
from main.models import Experience, Education, Certification, Skill
from datetime import date

User = get_user_model()

# Créer le superuser s'il n'existe pas
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('✅ Superuser créé : admin / admin123')
else:
    print('⚠️ Superuser admin existe déjà')

# Ajouter les données fictives s'il n'y en a pas
if not Experience.objects.exists():
    Experience.objects.create(
        title='Analyste SOC Senior',
        company='TechSecure Inc.',
        start_date=date(2022, 1, 1),
        description='Responsable de la surveillance des menaces, réponse aux incidents et automatisation des processus de sécurité.'
    )
    Experience.objects.create(
        title='Analyste Cybersécurité',
        company='DataGuard Solutions',
        start_date=date(2020, 6, 1),
        end_date=date(2021, 12, 31),
        description='Détection et analyse des vulnérabilités, gestion des IDS/IPS et scripting pour l\'automatisation.'
    )
    print('✅ Expériences ajoutées')
else:
    print('⚠️ Expériences existent déjà')

if not Education.objects.exists():
    Education.objects.create(
        degree='Master en Cybersécurité',
        institution='Université de Technologie',
        start_date=date(2018, 9, 1),
        end_date=date(2020, 5, 31),
        description='Spécialisation en sécurité des systèmes d\'information et analyse des menaces.'
    )
    Education.objects.create(
        degree='Licence en Informatique',
        institution='Université de Technologie',
        start_date=date(2015, 9, 1),
        end_date=date(2018, 6, 30),
        description='Bases solides en programmation et réseaux.'
    )
    print('✅ Formations ajoutées')
else:
    print('⚠️ Formations existent déjà')

if not Certification.objects.exists():
    Certification.objects.create(
        name='Certified Ethical Hacker (CEH)',
        issuer='EC-Council',
        date_obtained=date(2021, 3, 15),
        expiry_date=date(2024, 3, 15),
        credential_id='CEH-123456'
    )
    Certification.objects.create(
        name='CompTIA Security+',
        issuer='CompTIA',
        date_obtained=date(2020, 8, 20),
        expiry_date=date(2023, 8, 20),
        credential_id='SEC+-789012'
    )
    print('✅ Certifications ajoutées')
else:
    print('⚠️ Certifications existent déjà')

if not Skill.objects.exists():
    Skill.objects.create(name='SIEM (Splunk, ELK)', category='technical', level='Expert')
    Skill.objects.create(name='Python', category='technical', level='Avancé')
    Skill.objects.create(name='Bash Scripting', category='technical', level='Intermédiaire')
    Skill.objects.create(name='Analyse de menaces', category='technical', level='Expert')
    Skill.objects.create(name='Français', category='language', level='Natif')
    Skill.objects.create(name='Anglais', category='language', level='Courant')
    Skill.objects.create(name='Communication', category='soft', level='Avancé')
    Skill.objects.create(name='Travail d\'équipe', category='soft', level='Avancé')
    print('✅ Compétences ajoutées')
else:
    print('⚠️ Compétences existent déjà')

print('\n✅ Initiative de base de données terminée!')
