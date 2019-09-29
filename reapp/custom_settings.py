import sys,os
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

# CELERY SETTING
# import djcelery
# djcelery.setup_loader()
# djcelery.setup_loader()
# CELERY_TIMEZONE = 'Europe/Istanbul'
# # CELERY_IMPORTS = ('erp.tasks',)
# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
# CELERY_BROKER_URL = 'amqp://localhost'
# CELERY_RESULT_BACKEND = 'django-db'
# CELERY_CACHE_BACKEND = 'django-cache'