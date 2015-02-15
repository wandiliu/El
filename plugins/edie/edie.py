import time

import eliza

crontable = []
outputs = []

def process_message(data):
    if data['channel'].startswith("D"):
        outputs.append([data['channel'], "{}".format(eliza.respond(data['text'])) ])
