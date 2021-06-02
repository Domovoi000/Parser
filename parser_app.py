import json
import threading
import datetime

from parser.parser import parse
# from screen_in_base64.screen import *
from elasticDB.db_work import *


if __name__ == "__main__":
    URL = 'http://continewsnv5otx5kaoje7krkto2qbu3gtqef22mnr7eaxw3y6ncz3ad.onion'
    # List of leaks
    leaks = []

    def parsing():
        print('Start program ' + datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
        # Get all the records from the site.
        leak = parse(leaks, URL)

        # Save all leaks on JSON
        with open('leak.json', 'w') as file:
            json.dump(leak, file)

        # Save data in DB
        elastic_db_works(leak)

        # Start program every hour
        threading.Timer(60.0 * 60, parsing).start()

    parsing()

    # Get screenshot in base64 but only with firefox
    # get_screen_shot('some url')
    #
