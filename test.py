from os import environ as env
from dotenv import load_dotenv

load_dotenv()

print('API_KEY:  {}'.format(env['SERVER_NAME']))