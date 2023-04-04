import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "15671595")

API_HASH = os.environ.get("API_HASH", "bb8f36f9c39a24c7f8b2acbc7ea8c60a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6144136776:AAHX7p92ajDcQj_WdXytpyDt6sRr-twbGrg") 

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
