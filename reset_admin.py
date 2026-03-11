#!/usr/bin/env python
"""
Script pour réinitialiser les credentials du superuser admin via Django shell
"""
import os
import sys
import django
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
    django.setup()
    
    from django.contrib.auth import get_user_model
    
    User = get_user_model()
    
    logger.info("🔄 Début de la réinitialisation du superuser...")
    
    # Supprimer l'ancien admin s'il existe
    admin_count = User.objects.filter(username='admin').count()
    if admin_count > 0:
        deleted_count, _ = User.objects.filter(username='admin').delete()
        logger.info(f"✅ Ancien superuser supprimé ({deleted_count} utilisateur(s))")
    else:
        logger.info("ℹ️ Aucun ancien superuser trouvé")
    
    # Créer un nouveau superuser
    logger.info("🔄 Création du nouveau superuser...")
    user = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123'
    )
    logger.info(f"✅ Superuser créé avec succès!")
    logger.info(f"   Username: admin")
    logger.info(f"   Password: admin123")
    logger.info(f"   is_staff: {user.is_staff}")
    logger.info(f"   is_superuser: {user.is_superuser}")
    logger.info(f"   is_active: {user.is_active}")
    
    # Vérifier le mot de passe
    if user.check_password('admin123'):
        logger.info("✅ Mot de passe vérifié: OK")
    else:
        logger.error("❌ ERREUR: Le mot de passe n'a pas pu être vérifié!")
        sys.exit(1)
    
    # Double vérification: recharger l'utilisateur depuis la base de données
    user_check = User.objects.get(username='admin')
    if user_check.check_password('admin123'):
        logger.info("✅ Vérification depuis la BD: OK")
    else:
        logger.error("❌ ERREUR: Le mot de passe n'a pas pu être vérifié depuis la BD!")
        sys.exit(1)
    
    logger.info("\n✅ Réinitialisation complète du superuser admin!")
    sys.exit(0)

except Exception as e:
    logger.error(f"❌ Erreur lors de la réinitialisation: {str(e)}", exc_info=True)
    sys.exit(1)
