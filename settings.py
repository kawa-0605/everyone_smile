import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = '/Users/y.kawamura/dev/python/.env'
load_dotenv(dotenv_path)

CSK = os.environ.get("CONGNITIVE_SERVICE_KEY")
CSE = os.environ.get("CONFNITIVE_SERVICE_ENDPOINT")
