# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", default="22165592")
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default="aa2886eda514d8beaa98695cfe3060ff")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", default="1AZWarzkBuytpK2B6YRdYGfn2-pYxQSNrxycYQsQBphrPdZvlGbI91zERv2X4CRpUU54oJhUXqlAJHcRI6acQyg4YFSeyC7g8mWR2pgneQrtD4fq8zQdWslJFOOa7tvTEDS_FYbSyx8meBnPfrvfrBKxBfQun5PSLxfXioFw3aYjgzicwp1d3tQjzIa2WEuQc37km5OUM8TmSBQ6LPQGA7ZaZpFDtFsCdRxoH5KpqLDT_3KNRRUzfOnMHijqzwR025KZbmAUggYI2Ex3Gbf1jWo9LxbNqaLIMZDjpDtgNxlImZAYjh1v1X7ba1ggBQTwKFqH6VLy2aXfHiL5JGfu_py6fsJ67hkg=")
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default="redis-13617.c212.ap-south-1-1.ec2.cloud.redislabs.com:13617") or config("REDIS_URL", default=None))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", default="dev")
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default=None)
