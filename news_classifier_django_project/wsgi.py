import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_classifier_django_project.settings')
application = get_wsgi_application()
