# config.py

from os import environ as env

from dotenv import load_dotenv
load_dotenv()

REDIS_HOST = env['REDIS_HOST']
REDIS_PORT = env['REDIS_PORT']
REDIS_USERNAME = env['REDIS_USERNAME']
REDIS_PASSWORD = env['REDIS_PASSWORD']

TOKEN = env['TOKEN']
MANIFEST_URL = env['MANIFEST_URL']

JETTON = env['JETTON']
JETTON_SYMBOL = env['JETTON_SYMBOL']
BUY_LINK = env['BUY_LINK']