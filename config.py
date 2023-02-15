import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27686030")

API_HASH = os.environ.get("API_HASH", "486e18582e097bbc7eee3c59204781c4")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6120841602:AAFUi8h3ZjWRLUuUjpcDmjwYlWq32FfuN4w") 

FORCE_SUB = os.environ.get("FORCE_SUB", "WebXBots") 

DB_NAME = os.environ.get("DB_NAME","cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://mhfghffsddfs:qanty9cqkXQoyril@cluster0.zjbn1t9.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '639521576').split()]

PORT = os.environ.get("PORT", "8080")
