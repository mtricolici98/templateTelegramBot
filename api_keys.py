import json
import os

# Incarca toate cheile din fisierul api_keys.json, care trebuie sa fie exclus din proiect

_KEYS_PATH = os.path.dirname(os.path.abspath(__file__))

_KEYS_FILE = os.path.join(_KEYS_PATH, 'api_keys.json')

TELEGRAM_API_KEY = ''
WEATHER_API_KEY = ''

_ALL_KEYS = ['TELEGRAM_API_KEY', 'WEATHER_API_KEY']


def load_keys():
    data = json.load(open(_KEYS_FILE))
    global TELEGRAM_API_KEY
    global WEATHER_API_KEY
    TELEGRAM_API_KEY = data['TELEGRAM_API_KEY']
    WEATHER_API_KEY = data['WEATHER_API_KEY']


def ensure_file_exists():
    if not os.path.exists(_KEYS_FILE):
        json.dump({k: '' for k in _ALL_KEYS}, open(_KEYS_FILE, 'w'))


ensure_file_exists()
load_keys()
