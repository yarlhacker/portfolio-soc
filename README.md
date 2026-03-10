# Portfolio Analyste SOC

Ce projet est un site web portfolio moderne pour un Analyste SOC, inspiré du design de Brittany Chiang (brittanychiang.com). Développé avec Django et Tailwind CSS.

## Fonctionnalités

- **Design moderne** : Thème sombre avec accents verts, inspiré de portfolios contemporains.
- **Page unique** : Toutes les sections sur une seule page avec navigation smooth scroll.
- **Sections CV** : Expériences, Formation, Certifications, Compétences (techniques, comportementales, langues).
- **Animations** : Effets de fade-in au scroll pour une expérience fluide.
- **Responsive** : Design adaptatif pour tous les appareils.
- **Interface admin** : Gestion facile du contenu via Django Admin.
- **Base de données** : Modèles pour expériences, éducation, certifications et compétences.

## Technologies

- Django 6.0
- Tailwind CSS (via CDN)
- Font Inter
- Alpine.js pour interactions légères

## Installation

1. Cloner ou naviguer vers le répertoire.
2. Activer l'environnement virtuel : `.venv\Scripts\activate`
3. Installer les dépendances : `pip install -r requirements.txt`
4. Appliquer les migrations : `python manage.py migrate`
5. Créer un superuser : `python manage.py createsuperuser`
6. Lancer le serveur : `python manage.py runserver`

## Utilisation

- Site : http://127.0.0.1:8000/
- Admin : http://127.0.0.1:8000/admin/

Ajoutez vos expériences, formations, certifications et compétences via l'interface admin pour personnaliser le contenu.

## Personnalisation

- Modifiez les couleurs dans `base.html` (config Tailwind).
- Ajustez le contenu dans `home.html`.
- Ajoutez des sections ou modifiez les modèles selon vos besoins.

## Technologies

- Django
- Bootstrap 5
- SQLite (base de données par défaut)