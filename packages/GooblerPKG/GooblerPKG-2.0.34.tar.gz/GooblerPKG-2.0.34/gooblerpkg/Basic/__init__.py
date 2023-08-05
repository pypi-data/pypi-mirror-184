###################
### Goobler 2023 ##
###################
# Scripts made by Eric #

import requests
from ..Storage import commandsRegistered, registerCommand, getCommand, executeCommand

print("[Process] INITIALIZED")

class ctx: 
    def __init__(self):
        pass

    def send_message(self, channel, message, sender="My Bot"):
        resp = requests.get(f"https://goobl2.ericplayzyt.repl.co/api/messaging/send_message/s/{channel}", headers={"message": message, "sent_by": sender})

def command(function, name, **kwargs):
    registerCommand(name, function)

