#!/usr/bin/env python
"""
Script pour initialiser les données du portfolio (superuser et données fictives)
"""
import os
import sys
import django
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.contrib.auth import get_user_model
from main.models import Experience, Education, Certification, Skill
from datetime import date

User = get_user_model()

try:
    logger.info("🔄 Début de l'initialisation de la base de données...")
    
    # Créer le superuser s'il n'existe pas
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        logger.info('✅ Superuser créé : admin / admin123')
    else:
        logger.info('⚠️ Superuser admin existe déjà')
        # Vérifier et mettre à jour le mot de passe si nécessaire
        admin_user = User.objects.get(username='admin')
        if not admin_user.check_password('admin123'):
            admin_user.set_password('admin123')
            admin_user.save()
            logger.info('🔄 Mot de passe admin mis à jour')
except Exception as e:
    logger.error(f'❌ Erreur lors de la création du superuser: {str(e)}', exc_info=True)

try:
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
        logger.info('✅ Expériences ajoutées')
    else:
        logger.info('⚠️ Expériences existent déjà')
except Exception as e:
    logger.error(f'❌ Erreur lors de l\'ajout des expériences: {str(e)}', exc_info=True)

try:
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
        logger.info('✅ Formations ajoutées')
    else:
        logger.info('⚠️ Formations existent déjà')
except Exception as e:
    logger.error(f'❌ Erreur lors de l\'ajout des formations: {str(e)}', exc_info=True)

try:
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
        logger.info('✅ Certifications ajoutées')
    else:
        logger.info('⚠️ Certifications existent déjà')
except Exception as e:
    logger.error(f'❌ Erreur lors de l\'ajout des certifications: {str(e)}', exc_info=True)

try:
    if not Skill.objects.exists():
        Skill.objects.create(name='SIEM (Splunk, ELK)', category='technical', level='Expert')
        Skill.objects.create(name='Python', category='technical', level='Avancé')
        Skill.objects.create(name='Bash Scripting', category='technical', level='Intermédiaire')
        Skill.objects.create(name='Analyse de menaces', category='technical', level='Expert')
        Skill.objects.create(name='Français', category='language', level='Natif')
        Skill.objects.create(name='Anglais', category='language', level='Courant')
        Skill.objects.create(name='Communication', category='soft', level='Avancé')
        Skill.objects.create(name='Travail d\'équipe', category='soft', level='Avancé')
        logger.info('✅ Compétences ajoutées')
    else:
        logger.info('⚠️ Compétences existent déjà')
except Exception as e:
    logger.error(f'❌ Erreur lors de l\'ajout des compétences: {str(e)}', exc_info=True)

logger.info('✅ Initialisation de la base de données terminée!')
sys.exit(0)
