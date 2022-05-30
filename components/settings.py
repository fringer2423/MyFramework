from os import path
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
STATIC_FILES_DIR = path.join(ROOT_DIR, 'staticfiles')
STATIC_URL = '/static/'
