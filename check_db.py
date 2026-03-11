#!/usr/bin/env python
"""
Script pour vérifier l'état de la base de données
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.contrib.auth.models import User
from main.models import Experience, Education, Certification, Skill

print("=" * 60)
print("🔍 DIAGNOSTIC DE LA BASE DE DONNÉES")
print("=" * 60)

print("\n👤 UTILISATEURS :")
admins = User.objects.filter(username='admin')
print(f"  Nombre d'admin: {admins.count()}")
if admins.exists():
    admin = admins.first()
    print(f"  - Username: {admin.username}")
    print(f"  - Email: {admin.email}")
    print(f"  - is_staff: {admin.is_staff}")
    print(f"  - is_superuser: {admin.is_superuser}")
    print(f"  - is_active: {admin.is_active}")
    # Test du mot de passe
    if admin.check_password('admin123'):
        print(f"  - Mot de passe 'admin123': ✅ CORRECT")
    else:
        print(f"  - Mot de passe 'admin123': ❌ INCORRECT")
else:
    print(f"  ❌ AUCUN SUPERUSER 'admin' TROUVÉ!")

print(f"\n📊 DONNÉES :")
print(f"  - Expériences: {Experience.objects.count()}")
print(f"  - Formations: {Education.objects.count()}")
print(f"  - Certifications: {Certification.objects.count()}")
print(f"  - Compétences: {Skill.objects.count()}")

print("\n" + "=" * 60)
