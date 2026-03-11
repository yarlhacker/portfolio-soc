#!/usr/bin/env python
"""
Script pour réinitialiser les credentials du superuser admin via Django shell
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Supprimer l'ancien admin s'il existe
if User.objects.filter(username='admin').exists():
    User.objects.filter(username='admin').delete()
    print("✅ Ancien superuser supprimé")

# Créer un nouveau superuser
user = User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin123'
)

# Vérifier que l'utilisateur a bien été créé avec les bonnes permissions
print(f"✅ Superuser créé avec succès!")
print(f"   Username: admin")
print(f"   Password: admin123")
print(f"   is_staff: {user.is_staff}")
print(f"   is_superuser: {user.is_superuser}")

# Vérifier le mot de passe
if user.check_password('admin123'):
    print("✅ Mot de passe vérifié: OK")
else:
    print("❌ ERREUR: Le mot de passe n'a pas pu être vérifié!")
    sys.exit(1)

print("\n✅ Réinitialisation complète du superuser admin!")
sys.exit(0)
