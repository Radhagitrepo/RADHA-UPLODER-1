import os

API_ID = API_ID =  23303247

API_HASH = os.environ.get("API_HASH", "23623f737dc15708708c65a7297e1510")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7130247687:AAH62Amtb4TC2V63iwyNdccxzqL5Jo8gFwY")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6931140424))

LOG = -1002166457568,

# UPDATE_GRP = -1002223793550, # bot sat group

# auth_chats = [6931140424,6335525003]

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6931140424").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


