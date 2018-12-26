#!/usr/bin/env python3

# posts current IP to #cf-racingteam channel on codingforce slack

import requests
import logging
import sys

# levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s:%(message)s")

URL = 'https://hooks.slack.com/services/<secret API key here>'

# working curl exsample
# curl -X POST -H 'Content-type: application/json'
#      --data '{"text":"Hello, World!"}'
#      https://hooks.slack.com/services/<secret API key here>

def post_to_slack(ip):
    if not ip:
        ip = 'unknown'
    data = {'text': 'IP-Address: {!s}'.format(ip)}
    logging.debug(data)

    try:
        r = requests.post(URL, json=data)
    except requests.exceptions.RequestException as e:
        logging.error(e)
        raise Exception('Could not post to slack')

    if r.text != 'ok':
        logging.error('returend status code: {!s}'.format(r.status_code))
        raise Exception('could not post to slack')
    else:
        return r

if len(sys.argv) < 1:
    err = 'required IP address missing'
    logging.error(err)
else:
    ipaddr = sys.argv[1]
    print(post_to_slack(ipaddr))
